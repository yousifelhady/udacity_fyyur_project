"""empty message

Revision ID: be4b75e8b211
Revises: 2231329e21b0
Create Date: 2020-12-22 22:00:37.808831

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'be4b75e8b211'
down_revision = '2231329e21b0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('artists', sa.Column('seeking_description', sa.String(length=200), nullable=True))
    op.add_column('artists', sa.Column('seeking_venue', sa.Boolean(), nullable=True))
    op.add_column('artists', sa.Column('website', sa.String(length=200), nullable=True))
    op.add_column('venues', sa.Column('seeking_description', sa.String(length=200), nullable=True))
    op.add_column('venues', sa.Column('seeking_talent', sa.Boolean(), nullable=True))
    op.add_column('venues', sa.Column('website', sa.String(length=200), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('venues', 'website')
    op.drop_column('venues', 'seeking_talent')
    op.drop_column('venues', 'seeking_description')
    op.drop_column('artists', 'website')
    op.drop_column('artists', 'seeking_venue')
    op.drop_column('artists', 'seeking_description')
    # ### end Alembic commands ###