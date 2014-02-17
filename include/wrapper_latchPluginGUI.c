#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>


int main( void )
{
   execl("/usr/lib/openvpn/latch/latchPluginGUI.py", "latchPluginGUI.py", NULL);

   return 0;
}
