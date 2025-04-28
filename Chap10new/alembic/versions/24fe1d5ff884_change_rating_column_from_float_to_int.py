"""change rating column from float to int

Revision ID: 24fe1d5ff884
Revises: 0e9a219e7a00
Create Date: 2025-04-23 09:13:42.707805

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '24fe1d5ff884'
down_revision: Union[str, None] = '0e9a219e7a00'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.alter_column('books', 'rating',
        existing_type=sa.Float(),
        type_=sa.Integer(),
        existing_nullable=True
    )

def downgrade():
    op.alter_column('books', 'rating',
        existing_type=sa.Integer(),
        type_=sa.Float(),
        existing_nullable=True
    )
    
