"""empty message

Revision ID: 27cb38ce6374
Revises: 34472beb56d4
Create Date: 2015-11-10 08:39:40.099556

"""

# revision identifiers, used by Alembic.
revision = '27cb38ce6374'
down_revision = '34472beb56d4'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('tags', 'owner_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('tags', 'owner_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    ### end Alembic commands ###