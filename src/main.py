import logging
import signal
import sys
from contextlib import asynccontextmanager
from fastapi import FastAPI, Response, status,Depends, HTTPException
from src.database import check_db_connection, engine,SessionLocal, ProductDB
from src.logger import setup_json_logging
from sqlalchemy.orm import Session
from pydantic import BaseModel
from src.logger import logger

from alembic import command
from alembic.config import Config

logger = logging.getLogger(__name__)


def sigterm_handler(signum, frame):
    logger.info("SIGTERM received. Starting graceful shutdown...")
    engine.dispose()
    logger.info("Database connections closed.")
    sys.exit(0)


signal.signal(signal.SIGTERM, sigterm_handler)


@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Application starting up...")

    logger.info("Checking and applying database migrations...")
    try:
        alembic_cfg = Config("alembic.ini")
        command.upgrade(alembic_cfg, "head")
        logger.info("Database migrations applied successfully.")
    except Exception as e:
        logger.error(f"Failed to apply database migrations: {e}")
        sys.exit(1)

    yield

    logger.info("Initiating graceful shutdown...")
    engine.dispose()
    logger.info("Database connections closed. Shutdown complete.")

app = FastAPI(lifespan=lifespan)


@app.get("/health")
def health_check(response: Response):
    is_db_up = check_db_connection()
    if is_db_up:
        logger.info("Health check passed. DB is connected.")
        return {"status": "ok", "database": "connected"}
    else:
        logger.error("Health check failed. DB is unreachable.")
        response.status_code = status.HTTP_503_SERVICE_UNAVAILABLE
        return {"status": "error", "database": "disconnected"}


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


class ProductCreate(BaseModel):
    name: str
    price: float


class ProductResponse(ProductCreate):
    id: int



@app.post("/products/", response_model=ProductResponse)
def create_product(product: ProductCreate, db: Session = Depends(get_db)):
    db_product = ProductDB(name=product.name, price=product.price)
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    logger.info(f"Product created in DB with ID: {db_product.id}")
    return db_product


@app.get("/products/{product_id}", response_model=ProductResponse)
def get_product(product_id: int, db: Session = Depends(get_db)):
    db_product = db.query(ProductDB).filter(ProductDB.id == product_id).first()
    if db_product is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")
    return db_product


@app.put("/products/{product_id}", response_model=ProductResponse)
def update_product(product_id: int, product: ProductCreate,
                   db: Session = Depends(get_db)):
    db_product = db.query(ProductDB).filter(ProductDB.id == product_id).first()
    if db_product is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")

    db_product.name = product.name
    db_product.price = product.price
    db.commit()
    db.refresh(db_product)
    logger.info(f"Product updated in DB: {product_id}")
    return db_product


@app.delete("/products/{product_id}")
def delete_product(product_id: int, db: Session = Depends(get_db)):
    db_product = db.query(ProductDB).filter(ProductDB.id == product_id).first()
    if db_product is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")

    db.delete(db_product)
    db.commit()
    logger.info(f"Product deleted from DB: {product_id}")
    return {"deleted": True}