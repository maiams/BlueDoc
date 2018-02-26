"""create customer table

Revision ID: 0ffb5b99b12c
Revises: 
Create Date: 2018-02-26 17:56:09.344046

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0ffb5b99b12c'
down_revision = None
branch_labels = None
depends_on = None
document_type_enum = sa.Enum('RG', 'CPF', 'CNH', name='document_type_enum')


def upgrade():
    op.create_table(
        'customer',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(100), nullable=False),
        sa.Column('email', sa.String(100)),
        sa.Column('phone', sa.String(50)),
        sa.Column('document', sa.String(100)),
        sa.Column('document_type', document_type_enum),
        sa.Column('birth_date', sa.Date()),
    )


def downgrade():
    op.drop_table('customer')