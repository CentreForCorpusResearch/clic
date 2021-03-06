"""empty message

Revision ID: 37ed83d4e343
Revises: 722dc77dd3
Create Date: 2015-11-05 18:12:35.273345

"""

# revision identifiers, used by Alembic.
revision = '37ed83d4e343'
down_revision = '722dc77dd3'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tags', sa.Column('owner_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'tags', 'user', ['owner_id'], ['id'])
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'tags', type_='foreignkey')
    op.drop_column('tags', 'owner_id')
    ### end Alembic commands ###
