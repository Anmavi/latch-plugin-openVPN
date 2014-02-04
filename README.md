### LATCH PAM OPENVPN PLUGIN -- INSTALLATION GUIDE ###


#### PREREQUISITES ####

 * Openvpn version 2.3.2. (UNIX system - http://ubuntuguide.org/wiki/OpenVPN_server)

 * Auth-pam openvpn plugin. (included in openvpn source package)

 * Libraries: python3 python3-tk build-essential libpam0g-dev libcurl4-openssl-dev liblzo2-dev (apt-get install)

 * EasyGui (included in latch-plugin-pam-openvpn package)

* To get the "Application ID" and "Secret", (fundamental values for integrating Latch in any application), it’s necessary to register a developer account in Latch's website: https://latch.elevenpaths.com. On the upper right side, click on "Developer area".


#### INSTALLING THE PLUGIN IN OPENVPN ####

1. Go to "python" directory in plugin package, open and edit "latch-model.conf" file. Add your settings and save it in the same directory as "latch.conf".

2. Open a terminal. Change to "python" directory, where you have saved the "latch.conf" file. Run "sudo python3 install.py -f latch.conf".

3. Edit "/etc/init.d/openvpn" file. Add at the begginning "export LD_PRELOAD=/lib/x86_64-linux-gnu/libpam.so.0" (may be you need to use a different path. Look for "libpam.so.0" in your file system directory).

4. Open "server.conf". Add "plugin /usr/lib/openvpn/openvpn-auth-pam.so latch-login" (may be you need to use a different path. Look for "openvpn-auth-pam.so" in your file system directory).

5. Linux Restart Openvpn "sudo service openvpn restart".

Then, on the client, specify that the user enter a password by adding "auth-user-pass" to the "client.conf".
