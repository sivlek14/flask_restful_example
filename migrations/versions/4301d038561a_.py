"""empty message

Revision ID: 4301d038561a
Revises: 770528413ef2
Create Date: 2016-12-22 09:51:41.530605

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4301d038561a'
down_revision = '770528413ef2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('address',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=50), nullable=True),
    sa.Column('users_id_user', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['users_id_user'], ['users.id_user'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('address')
    # ### end Alembic commands ###
