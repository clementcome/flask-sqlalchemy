"""user and training table

Revision ID: d97d6d5cb29d
Revises: 
Create Date: 2019-04-08 19:38:58.616384

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd97d6d5cb29d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=40), nullable=True),
    sa.Column('gender', sa.Enum('male', 'female', name='gender'), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_username'), 'user', ['username'], unique=False)
    op.create_table('training',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('training_type', sa.String(length=40), nullable=True),
    sa.Column('person_id', sa.Integer(), nullable=True),
    sa.Column('date', sa.DateTime(), nullable=True),
    sa.Column('duration', sa.Time(), nullable=True),
    sa.Column('distance', sa.Float(), nullable=True),
    sa.ForeignKeyConstraint(['person_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_training_date'), 'training', ['date'], unique=False)
    op.create_index(op.f('ix_training_training_type'), 'training', ['training_type'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_training_training_type'), table_name='training')
    op.drop_index(op.f('ix_training_date'), table_name='training')
    op.drop_table('training')
    op.drop_index(op.f('ix_user_username'), table_name='user')
    op.drop_table('user')
    # ### end Alembic commands ###