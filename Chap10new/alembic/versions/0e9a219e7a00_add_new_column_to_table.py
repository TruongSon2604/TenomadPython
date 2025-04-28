"""add new column to table

Revision ID: 0e9a219e7a00
Revises: e6e1a5fa00e3
Create Date: 2025-04-23 09:09:59.552896

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0e9a219e7a00'
down_revision: Union[str, None] = 'e6e1a5fa00e3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('books', sa.Column('genre', sa.String(255), nullable=True))
    op.add_column('books', sa.Column('rating', sa.Float(), nullable=True))
    pass


def downgrade() -> None:
    op.drop_column('books', 'genre')
    op.drop_column('books', 'rating')
    pass
