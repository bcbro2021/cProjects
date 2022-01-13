import os, sys

BLUE = '\033[94m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
RED = '\033[91m'
ENDCOLOR = '\033[0m'

def cprint(color,text):
    if color == "red":
        print(RED+text+ENDCOLOR)
    elif color == "yellow":
        print(YELLOW+text+ENDCOLOR)
    elif color == "green":
        print(GREEN+text+ENDCOLOR)
    elif color == "blue":
        print(BLUE+text+ENDCOLOR)

#title
cprint("yellow","""🇼‌🇪‌🇱‌🇨‌🇴‌🇲‌🇪‌""")
print("\n\n")

#app list
cprint("yellow","Choose the app you want to run: ")

#make directory if it doesnt exist
try:
    os.mkdir(".apps")
except FileExistsError:
    pass
#change directory
os.chdir(".apps")

#read and print apps
open("start.apps", "a").close()
while True:
    execs = []
    with open("start.apps", "r") as file:
        linenum = 0
        for line in file.readlines():
            if line.startswith("name:"):
                pr = line.split("name:")[1]
                cprint("green",f"{linenum}: {pr}")
                linenum += 1
            if line.startswith("exec:"):
                app = line.split("exec:")[1]
                execs.append(app)

    exec = input(f"{BLUE}Run: {ENDCOLOR}")
    if exec == "exit":
        os.system("clear")
        sys.exit()
    elif exec == "clear":
        os.system("clear")
    else:
        try:
            #change password
            password = ""
            with open("password","r") as file:
                password = file.readlines()[0].strip()
            passwordTest = input(f"{BLUE}Password: {ENDCOLOR}")
            if passwordTest == password:
                os.system("clear")
                os.system(f"terminator --execute {execs[int(exec)]}")
                cprint("green","\n\nProcess Completed!\n\n")
            else:
                os.system("clear")
                cprint("red","\n\nWrong Password!\n\n")
        except IndexError:
            os.system("clear")
            cprint("red","\n\nInvalid executable!\n\n")
        except ValueError:
            os.system("clear")
            cprint("red","\n\nInvalid App Id\n\n")
