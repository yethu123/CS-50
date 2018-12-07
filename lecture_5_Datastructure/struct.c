#include <cs50.h>
#include <stdio.h>
#include <string.h>

#include "struct.h"





int main(void)
{
    // allocate space for students
    int enrollment = get_int("enrollment: ");
    student students[enrollment];

    // prompt for students' names and dorms
    for (int i = 0; i < enrollment; i++)
    {
        students[i].name = get_string("name: ");
        students[i].dorm = get_string("dorm: ");
    }

    // print students' names and dorms
    for (int i = 0; i < enrollment; i++)
    {
        printf("%s is in %s.\n", students[i].name, students[i].dorm);
    }
    FILE *file = fopen("students.csv", "w");
if (file)
/*{
    for (int i = 0; i < enrollment; i++)
    {
        fprintf(file, "%s,%s\n", students[i].name, students[i].dorm);
    }
    fclose(file);
*/}
}