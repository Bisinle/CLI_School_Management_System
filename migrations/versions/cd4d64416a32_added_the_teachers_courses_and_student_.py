"""added the teachers, courses and student tables

Revision ID: cd4d64416a32
Revises: b6e3212a72cf
Create Date: 2023-09-05 19:05:39.624823

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'cd4d64416a32'
down_revision: Union[str, None] = 'b6e3212a72cf'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('students',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(), nullable=True),
    sa.Column('last_name', sa.String(), nullable=True),
    sa.Column('gender', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('teachers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(), nullable=True),
    sa.Column('last_name', sa.String(), nullable=True),
    sa.Column('salary', sa.Integer(), nullable=True),
    sa.Column('bank_acount', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('courses',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('course_name', sa.String(), nullable=True),
    sa.Column('room', sa.Integer(), nullable=True),
    sa.Column('credit_hours', sa.Integer(), nullable=True),
    sa.Column('teachers_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['teachers_id'], ['teachers.id'], name=op.f('fk_courses_teachers_id_teachers')),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('courses')
    op.drop_table('teachers')
    op.drop_table('students')
    # ### end Alembic commands ###
