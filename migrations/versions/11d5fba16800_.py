"""empty message

Revision ID: 11d5fba16800
Revises: 
Create Date: 2021-05-31 10:31:26.246071

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '11d5fba16800'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('flower',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=200), nullable=False),
    sa.Column('att1', sa.Float(), nullable=False),
    sa.Column('att2', sa.Float(), nullable=False),
    sa.Column('att3', sa.Float(), nullable=False),
    sa.Column('att4', sa.Float(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('flower')
    # ### end Alembic commands ###
