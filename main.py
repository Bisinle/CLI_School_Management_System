from cli.student  import student_section
from cli.teachers  import teacher_command
from cli.courses  import courcommand
import click


@click.group()
def main():
    pass
   
    



if __name__ == '__main__':
    main.add_command(student_section)
    main.add_command(teacher_command)
    main.add_command(courcommand)
    main()