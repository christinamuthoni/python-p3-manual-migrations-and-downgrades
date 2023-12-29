"""Renaming birthday to birthyr

Revision ID: 907247bfaeb1
Revises: d91e64a9a0eb
Create Date: 2023-12-29 17:07:59.781840

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '907247bfaeb1'
down_revision = 'd91e64a9a0eb'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_column('birthday', 'birthyr')


def downgrade() -> None:
    op.rename_column('birthyr', 'birthday')
