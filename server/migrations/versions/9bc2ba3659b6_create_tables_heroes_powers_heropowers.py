"""Create tables heroes, powers, heropowers

Revision ID: 9bc2ba3659b6
Revises: 
Create Date: 2024-01-29 08:15:07.049382

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9bc2ba3659b6'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('heropowers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('strength', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('powers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('number_of_powers', sa.Integer(), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('heroes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('age', sa.Integer(), nullable=True),
    sa.Column('Power_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['Power_id'], ['powers.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('heroes')
    op.drop_table('powers')
    op.drop_table('heropowers')
    # ### end Alembic commands ###