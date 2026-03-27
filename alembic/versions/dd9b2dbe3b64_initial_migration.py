"""initial_migration

Revision ID: dd9b2dbe3b64
Revises: 
Create Date: 2026-03-25 19:02:54.234292

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = 'dd9b2dbe3b64'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
