#LATCH INSTALLATION GUIDE FOR OPENVPN


##PREREQUISITES
* OpenVPN version 2.2.x (UNIX system).

* Auth-pam OpenVPN plugin. (included in OpenVPN source package).

* Python

* C Compilator gcc and make

* Libraries: (libpam-dev, libcurl-dev, libssl-dev).

Installation in Debian/Ubuntu
```
sudo apt-get install libpam-dev libcurl-dev libssl-dev
```
Installation in RedHat/Fedora/Centos
```
yum install pam-devel libcurl-devel openssl-devel
```

* tkinter library installed if GUI is used (optional).

Installation in Debian/Ubuntu
```
sudo apt-get install python-tk
```
Installation in RedHat/Fedora/Centos
```
sudo yum install tkinter
```

* To get the **"Application ID"** and **"Secret"**, (fundamental values for integrating Latch in any application), it’s necessary to register a developer account in [Latch's website](https://latch.elevenpaths.com). On the upper right side, click on **"Developer area"**.


##DOWNLOADING THE OPENVPN PLUGIN
* When the account is activated, the user will be able to create applications with Latch and access to developer documentation, including existing SDKs and plugins. The user has to access again to [Developer area](https://latch.elevenpaths.com/www/developerArea), and browse his applications from **"My applications"** section in the side menu.

* When creating an application, two fundamental fields are shown: **"Application ID"** and **"Secret"**, keep these for later use. There are some additional parameters to be chosen, as the application icon (that will be shown in Latch) and whether the application will support OTP  (One Time Password) or not. For OpenVPN the OTP must be disabled.


* From the side menu in developers area, the user can access the **"Documentation & SDKs"** section. Inside it, there is a **"SDKs and Plugins"** menu. Links to different SDKs in different programming languages and plugins developed so far, are shown.


##INSTALLING THE PLUGIN IN OPENVPN
* Go to **"python"** directory in plugin package, open and edit **"latch-model.conf"** file. Add **"Application ID"** and **"Secret"** data, generated before and save it in the same directory as **"latch.conf"**.

* cd to the top-level directory of the plugin, and use the command to install it:
```
sudo ./install
```

* Open **"server.conf"**. Add **"plugin /[path-to-file openvpn-auth-pam.so]/openvpn-auth-pam.so openvpn"** to use it.

* Linux Restart OpenVPN

For Debian/Ubuntu,
```
sudo service openvpn restart
```
For RedHat/Fedora/CentOS,
```
sudo service openvpn restart
```

##UNINSTALLING THE PLUGIN IN OPENVPN
* Open a terminal. Change to **"python"** directory. Run:
```
sudo python uninstall.py
```

* Open **"server.conf"**. Delete or comment ('#') **"plugin /[path-to-file openvpn-auth-pam.so]/openvpn-auth-pam.so openvpn"**.

* Linux Restart OpenVPN

For Debian/Ubuntu,
```
sudo service openvpn restart
```
For RedHat/Fedora/CentOS,
```
sudo service openvpn restart
```

##USE OF LATCH MODULE FOR THE USERS
**Latch does not affect in any case or in any way the usual operations with an account. It just allows or denies actions over it, acting as an independent extra layer of security that, once removed or without effect, will have no effect over the accounts, which will remain with their original state.**

The user needs the Latch application installed on the phone, and follow these steps:

* **Step 1:** There are two options:
    * Option A. Pairing with command line: Just open a console and execute **“pairOVPN + TOKEN GENERATED BY LATCH”**.
    * Option B. Pairing with GUI: In a console, execute **“latchOVPN”**. A new windows will appear. Pressing on **“Pair”**, a new window will appear, where the user may introduce the token generated by the mobile app.

* **Step 2:** From the Latch app on the phone, the user has to generate the token, pressing on **“generate pairing code to add service"** at the bottom of the application.

* **Step 3:** The user has to type the characters generated on the phone into the text box displayed on the web page. Click on **"OK"** button.

* **Step 4:** Now the user may lock and unlock the account, preventing any unauthorized access.
