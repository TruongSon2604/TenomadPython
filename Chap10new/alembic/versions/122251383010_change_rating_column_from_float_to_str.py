"""change rating column from float to str

Revision ID: 122251383010
Revises: 24fe1d5ff884
Create Date: 2025-04-23 09:15:44.695465

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '122251383010'
down_revision: Union[str, None] = '24fe1d5ff884'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    # Nếu cần, chuyển đổi dữ liệu sang chuỗi trước khi đổi kiểu
    op.execute("UPDATE books SET rating = CAST(rating AS CHAR)")


    op.alter_column('books', 'rating',
        existing_type=sa.Float(),
        type_=sa.String(length=50),
        existing_nullable=True
    )

def downgrade():
    op.execute("UPDATE books SET rating = CAST(rating AS DECIMAL(10, 2))")

    op.alter_column('books', 'rating',
        existing_type=sa.String(length=50),
        type_=sa.Float(),
        existing_nullable=True
    )