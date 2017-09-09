#include <stdio.h>
#include <stdlib.h>

char data[5][10] = {"This","Is","Frida","Testing","Arguments"};

void fungsi(char* str)
{
    printf("I got word %s\n", str);
}

int main()
{
    int idx  = 0;
    time_t t;

    srand((unsigned) time(&t));

    printf("fungsi() is at %p\n", fungsi);
    while (1)
    {
        idx = rand() % 5;
        fungsi(data[idx]);
        sleep(1);
    }


}