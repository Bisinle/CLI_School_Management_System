"""added course_id and student_id columns to grades table

Revision ID: 0f5830d29153
Revises: 06a9a4c90125
Create Date: 2023-09-07 21:01:40.411641

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0f5830d29153'
down_revision: Union[str, None] = '06a9a4c90125'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('grades', schema=None) as batch_op:
        batch_op.add_column(sa.Column('student_id', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('course_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(batch_op.f('fk_grades_course_id_courses'), 'courses', ['course_id'], ['id'])
        batch_op.create_foreign_key(batch_op.f('fk_grades_student_id_students'), 'students', ['student_id'], ['id'])

    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('grades', schema=None) as batch_op:
        batch_op.drop_constraint(batch_op.f('fk_grades_student_id_students'), type_='foreignkey')
        batch_op.drop_constraint(batch_op.f('fk_grades_course_id_courses'), type_='foreignkey')
        batch_op.drop_column('course_id')
        batch_op.drop_column('student_id')

    # ### end Alembic commands ###
