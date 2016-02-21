"""Create user table

Revision ID: 4bafdb464737
Revises:
Create Date: 2016-02-21 12:24:46.640894

"""

# revision identifiers, used by Alembic.
revision = '4bafdb464737'
down_revision = None
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.create_table(
        'user',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('user_id', sa.String(255), nullable=False),
        sa.Column('name', sa.String(64), nullable=False, unique=True),
        sa.Column('email', sa.String(255))
    )


def downgrade():
    op.drop_table('user')
