"""Rename password_hash to password

Revision ID: d3cfbddf12d8
Revises: 9acf9247ac4a
Create Date: 2024-04-17 13:34:59.923273

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd3cfbddf12d8'
down_revision = '9acf9247ac4a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('password', sa.String(length=128), nullable=False))
        batch_op.drop_column('password_hash')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('password_hash', sa.VARCHAR(length=60), nullable=False))
        batch_op.drop_column('password')

    # ### end Alembic commands ###
