# Berseker Toolkit
## About toolkit 
Berserker toolkit contains 5 mother-hacker instruments:
- Futunus - generating wifi password using MAC address
- Catcher - social engineering tool for grabing IP 
- Malwarus - java backdoor, can converted to .jar file
- Petidash - sms bomber
- WatchDog - bruteforce tool for IP cameras
## Futunus
### Modules
- Pywifi - `pip install pywifi`
- Rich - `pip install rich`
- Comtypes - `pip install comtypes`

### Using
Start Futunus using `python Futunus.py`.  
__Functions:__
- Pin brute - start bruting pin code for wifi
- Show network list - showing network list
- Password brute - start bruting wifi password
- Info - showing info
## Catcher
### Modules
- Rich - `pip install rich`
- 2Ip - `pip install 2ip`
### Using
Start Catcher using `python Catcher.py`.
After server was started, make link using ngrok.
## Malwarus
### Functions
- Shell control
-  Other coming soon
### Preparation
build backdoor using `python Builder.py`.
If you need - convert `.java` file to `.jar`.
### Using
Start Malwarus using `java Malwarus.java`.
Then input port for listening and wait until connection.
If connection was successfully just input comands.
## Petidash
### Using
Start Petidash using `python Petidash.py`.
To start bombing just input phone number.
## Watch dog
### Modules
- Opencv - `pip install opencv-python`
- Rich - `pip install rich`
- Argparse - `pip install argparse`
### Using
Start WatchDog using `python WatchDog.py <IP> <PORT> <PROTOCOL>`.
If camera need password use  `python WatchDog.py <IP> <PORT> <PROTOCOL> -nps`.
###### If you will find any bugs, contact with me.
