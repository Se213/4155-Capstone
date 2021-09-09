"""add flash cards

Revision ID: 2e8e19b9b551
Revises: e4e735c9ad59
Create Date: 2021-04-29 12:50:43.471522

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2e8e19b9b551'
down_revision = 'e4e735c9ad59'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('flash_card',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('question', sa.String(length=100), nullable=True),
    sa.Column('choice_1', sa.String(length=100), nullable=True),
    sa.Column('choice_2', sa.String(length=100), nullable=True),
    sa.Column('choice_3', sa.String(length=100), nullable=True),
    sa.Column('choice_4', sa.String(length=100), nullable=True),
    sa.Column('correct_choice', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('question')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('flash_card')
    # ### end Alembic commands ###
