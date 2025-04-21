"""Add column to book

Revision ID: e6e1a5fa00e3
Revises: 
Create Date: 2025-04-16 11:40:10.528294

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e6e1a5fa00e3'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('books', sa.Column('published_year', sa.Integer(), nullable=True))
    pass

def downgrade() -> None:
    op.drop_column('books', 'published_year')
    pass
