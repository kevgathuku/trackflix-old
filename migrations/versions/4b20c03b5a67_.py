"""empty message

Revision ID: 4b20c03b5a67
Revises: 6e39085a8c76
Create Date: 2016-08-03 15:02:14.042692

"""

# revision identifiers, used by Alembic.
revision = '4b20c03b5a67'
down_revision = '6e39085a8c76'

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.add_column('external_service', sa.Column('base_url', sa.String(length=120), nullable=True))
    with op.batch_alter_table('external_service') as batch_op:
        ### commands auto generated by Alembic - please adjust! ###
        batch_op.drop_column('prefix_url')
    op.add_column('person_external_id', sa.Column('url_prefix', sa.String(length=100), nullable=True))
    op.add_column('show_external_id', sa.Column('url_prefix', sa.String(length=100), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('show_external_id', 'url_prefix')
    op.drop_column('person_external_id', 'url_prefix')
    op.add_column('external_service', sa.Column('prefix_url', sa.VARCHAR(length=120), nullable=True))
    op.drop_column('external_service', 'base_url')
    ### end Alembic commands ###