"""case end time

Revision ID: 3d1a641806c6
Revises: 59e80cb91ec
Create Date: 2014-03-09 12:36:34.575658

"""

# revision identifiers, used by Alembic.
revision = '3d1a641806c6'
down_revision = '59e80cb91ec'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('chunklist', sa.Column('end_time', sa.DateTime(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('chunklist', 'end_time')
    ### end Alembic commands ###
