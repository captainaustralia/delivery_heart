""" Custom upgrade password length

Revision ID: 15d2b5ce941c
Revises: 240b95254f23
Create Date: 2023-02-23 19:36:53.569496

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "15d2b5ce941c"
down_revision = "240b95254f23"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.alter_column("user", "password", type_=sa.String(length=256))
    pass
    # ### end Alembic commands ###


def downgrade() -> None:
    pass
    # DO NOTHING
    # ### end Alembic commands ###
