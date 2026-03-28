"""create_products_table

Revision ID: 54818d307ef8
Revises: dd9b2dbe3b64
Create Date: 2026-03-25 20:11:48.841457

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

revision: str = '54818d307ef8'
down_revision: Union[str, None] = 'dd9b2dbe3b64'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'products',
        sa.Column('id', sa.Integer(), primary_key=True, index=True),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('price', sa.Float(), nullable=False)
    )

def downgrade() -> None:
    op.drop_table('products')

