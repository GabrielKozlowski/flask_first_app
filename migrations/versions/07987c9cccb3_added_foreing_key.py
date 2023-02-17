"""Added Foreing Key

Revision ID: 07987c9cccb3
Revises: 14eb9585eb49
Create Date: 2023-02-17 11:03:26.046591

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '07987c9cccb3'
down_revision = '14eb9585eb49'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('posts', schema=None) as batch_op:
        batch_op.add_column(sa.Column('poster_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(None, 'users', ['poster_id'], ['id'])
        batch_op.drop_column('author')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('posts', schema=None) as batch_op:
        batch_op.add_column(sa.Column('author', mysql.VARCHAR(length=255), nullable=True))
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('poster_id')

    # ### end Alembic commands ###
