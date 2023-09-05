"""added the student_course Association table 

Revision ID: 666e8ac48710
Revises: cd4d64416a32
Create Date: 2023-09-05 19:09:21.060450

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '666e8ac48710'
down_revision: Union[str, None] = 'cd4d64416a32'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('student_course',
    sa.Column('courses_id', sa.Integer(), nullable=True),
    sa.Column('students_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['courses_id'], ['courses.id'], name=op.f('fk_student_course_courses_id_courses')),
    sa.ForeignKeyConstraint(['students_id'], ['students.id'], name=op.f('fk_student_course_students_id_students'))
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('student_course')
    # ### end Alembic commands ###
