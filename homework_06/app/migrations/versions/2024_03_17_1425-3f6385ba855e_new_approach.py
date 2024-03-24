"""new_approach

Revision ID: 3f6385ba855e
Revises: 
Create Date: 2024-03-17 14:25:33.233188

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3f6385ba855e'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:

    op.create_table('users',
    sa.Column('name', sa.String(length=32), nullable=False),
    sa.Column('email', sa.String(), nullable=True),
    sa.Column('username', sa.String(length=50), nullable=True),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_index(op.f('ix_users_username'), 'users', ['username'], unique=False)
    op.create_table('posts',
    sa.Column('title', sa.String(length=100), server_default='', nullable=False),
    sa.Column('body', sa.Text(), server_default='', nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('published_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )



def downgrade() -> None:

    op.drop_table('posts')
    op.drop_index(op.f('ix_users_username'), table_name='users')
    op.drop_table('users')

