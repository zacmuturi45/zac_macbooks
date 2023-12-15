"""Completed functionalities

Revision ID: e846f45af2cf
Revises: 29b60ed58450
Create Date: 2023-12-15 16:34:40.505102

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e846f45af2cf'
down_revision: Union[str, None] = '29b60ed58450'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
