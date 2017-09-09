/*
HITZ'17 - Frida

Get Plaintext of Encryption process

*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int encrypt_decrypt(char* data, int size, int key)
{
    for (int i=0, runkey = key; i<size; i++, key++)
    {
        data[i] ^= runkey;
    }
}

int main()
{
    char *buffer;
    char namafile[256];
    char key;
    int  file_size, buffer_read;
    int  inopt;
    int  loop = 1;

    FILE *fin;

    printf("Address: %p\n", encrypt_decrypt);

    printf("Masukkan key: ");
    scanf("%d", &key);
    printf("Masukkan nama file: ");
    scanf("%s", namafile);

    fin  = fopen(namafile, "r");
    if (fin == NULL) {
        printf("Could not open input file");
        exit(1);
    }

    fseek(fin, 0, SEEK_END);
    file_size = ftell(fin);
    rewind(fin);

    buffer = (char*) malloc(sizeof(char) * file_size + 1);
    if (buffer == NULL) 
    {
        printf("Memory error");
        exit(2);
    }
    memset(buffer, 0, file_size + 1);
    buffer_read = fread(buffer, 1, file_size, fin);

    while (loop)
    {
        printf("[1] Print buffer\n");
        printf("[2] Encrypt buffer\n");
        printf("[3] Exit\n");

        while (!scanf("%d", &inopt));

        switch (inopt)
        {
            case 1:
                printf("Buffer: %s\n", buffer);
                break;
            case 2:
                encrypt_decrypt(buffer, file_size, key);
                break;
            case 3:
                loop = 0;
                break;
        }
    }

    fclose(fin);

    return 0;
}