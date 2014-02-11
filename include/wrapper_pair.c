#include <stdio.h>
#include <stdlib.h>
#include <string.h>


int main(int arc, char **argv)
{
    if (arc == 2){
        if(strlen(argv[1]) == 6){
            char call[38]; 
            strncpy(call, "/usr/lib/openvpn/latch/pair.py ", 31);
            strncat(call, argv[1], 6);
            call[37] = '\0';
            system(call);
        }else{
            printf("Token not found\n");
        } 

    }else{
        printf("use 'pairOVPN <TOKEN>'\n");
    }

    return 0;
}
