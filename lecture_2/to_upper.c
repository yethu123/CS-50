#include <cs50.h>
#include <stdio.h>
#include <string.h>

int main(void)
{
    string s = get_string("before: ");
    printf("after:  ");
    for (int i = 0, n = strlen(s); i < n; i++)
    {
        if (s[i] >= 'a' && s[i] <= 'z')  //between
        {
            printf("%c", s[i] - ('a' - 'A'));//(a-A=97-65=32)y121-32=89"Y"
        }
        else
        {
            printf("%c", s[i]);
        }
    }
    printf("\n");
}