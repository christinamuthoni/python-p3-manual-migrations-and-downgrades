"""Renaming email to account

Revision ID: d91e64a9a0eb
Revises: 
Create Date: 2023-12-29 17:02:24.104296

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd91e64a9a0eb'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.alter_column('students', 'email', 'account')


def downgrade() -> None:
    op.alter_column('your_table', 'account', 'email')
