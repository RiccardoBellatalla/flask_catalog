"""new db with users and products

Revision ID: 1b77fb0adece
Revises: 
Create Date: 2021-12-11 18:23:26.459800

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1b77fb0adece'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=64), nullable=True),
    sa.Column('email', sa.String(length=120), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.Column('company_name', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_company_name'), 'user', ['company_name'], unique=False)
    op.create_index(op.f('ix_user_email'), 'user', ['email'], unique=True)
    op.create_index(op.f('ix_user_username'), 'user', ['username'], unique=True)
    op.create_table('product',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('sku_seller', sa.String(length=64), nullable=True),
    sa.Column('ean_code', sa.String(length=16), nullable=True),
    sa.Column('brand', sa.String(length=64), nullable=True),
    sa.Column('product_title', sa.String(length=128), nullable=True),
    sa.Column('product_description', sa.String(length=2048), nullable=True),
    sa.Column('product_price', sa.Numeric(precision=10, scale=2), nullable=True),
    sa.Column('stock', sa.Integer(), nullable=True),
    sa.Column('img_1', sa.String(length=500), nullable=True),
    sa.Column('carrier', sa.String(length=64), nullable=True),
    sa.Column('shipping_price', sa.Numeric(precision=10, scale=2), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('img_1')
    )
    op.create_index(op.f('ix_product_brand'), 'product', ['brand'], unique=False)
    op.create_index(op.f('ix_product_ean_code'), 'product', ['ean_code'], unique=False)
    op.create_index(op.f('ix_product_sku_seller'), 'product', ['sku_seller'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_product_sku_seller'), table_name='product')
    op.drop_index(op.f('ix_product_ean_code'), table_name='product')
    op.drop_index(op.f('ix_product_brand'), table_name='product')
    op.drop_table('product')
    op.drop_index(op.f('ix_user_username'), table_name='user')
    op.drop_index(op.f('ix_user_email'), table_name='user')
    op.drop_index(op.f('ix_user_company_name'), table_name='user')
    op.drop_table('user')
    # ### end Alembic commands ###
