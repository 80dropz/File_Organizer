from discord_webhook import DiscordWebhook
from tkinter import *
import customtkinter
import os
from os import listdir
import time
import random
from customtkinter import filedialog
import subprocess
if not os.path.exists("log.txt"):
    subprocess.run("setup.py", shell=True)
    exit()
else:
    logr = open("log.txt", "r")
    logrl = logr.read()
    logread = logr.readlines()
direntered = False
webhook_entered = False
wanttochange = False






def organize():
    entries = os.listdir(directory_path)
    filelog = open("filelog.txt", "w")

    filenuwd = 0
    folders = {}
    executables = {}

    for entry in entries:
        filenuwd += 1
        fullfilename = f"File#{filenuwd}"
        print(f"{fullfilename} = {entry}")
        filelog.write(f"{fullfilename} = {entry}\n")

































def dirask():
    global dir
    global wanttochange
    global direntered
    if direntered == False:
        dir = filedialog.askdirectory()
        direntered = not False
        check2.configure(text="Directory: Found", text_color="green")
        log = open("log.txt", "a")
        log.write(f"\nDirectory: {dir}")
        log.close()
    elif wanttochange == True:
        dir = filedialog.askdirectory()
        check2.configure(text="Directory: Changed", text_color="green")
        log = open("log.txt", "a")
        log.write(f"Directory: {dir}")
        log.close()
    else:
        errorlbl.configure(text="Already found directory if you would like to change click Directory button again", text_color="red")
        wanttochange = not False
        
def change():
    changewha = customtkinter.CTk()
    changewha.geometry("200x200")
    changewha.title("Change")

    webhookchange = customtkinter.CTkEntry(changewha, placeholder_text="Enter new webhook", fg_color="Blue")
    webhookchange.place(relx=0.5, rely=0.3, anchor=CENTER)

    changebtn = customtkinter.CTkButton(changewha, text="Change directory", command=change, fg_color="green")
    changebtn.place(relx=0.5, rely=0.5, anchor=CENTER)

    exitbtn = customtkinter.CTkButton(changewha, text="Exit", command=changewha.destroy(), fg_color="red")
    exitbtn.place(relx=0.1, rely=0.1, anchor=CENTER)


    changewha.mainloop()

def maindestroy():
    main.destroy()
def verifysetdestroy():
    verifyset.destroy()
def vertifysetting():
    global verifyset
    verifyset= customtkinter.CTk()
    verifyset.geometry("200x200")
    verifyset.title("Settings")

    webhookcheck = customtkinter.CTkLabel(verifyset, text=f"Webhook: {webhook_url}", text_color="red")
    webhookcheck.place(relx=0.5, rely=0.2, anchor=CENTER)

    dircheck = customtkinter.CTkLabel(verifyset, text=f"Directory: {directory_path}", text_color="red")
    dircheck.place(relx=0.5, rely=0.4, anchor=CENTER)

    goodbtn = customtkinter.CTkButton(verifyset, text="Correct", command=verifysetdestroy, fg_color="green")
    goodbtn.place(relx=0.5, rely=0.6, anchor=CENTER)

    badbtn = customtkinter.CTkButton(verifyset, text="Change", command=change, fg_color="Red")
    badbtn.place(relx=0.5, rely=0.8, anchor=CENTER)

    verifyset.mainloop()
def verify():
    if codes in checkcodeentry.get():
        checks1.configure(text="Webhook: Found", text_color="green")
        log = open("log.txt", "a")
        log.write(f"Webhook: {webhook}")
        log.close()
        checkcode.destroy()
    else:
        errorlbl2.configure(text="Wrong code", text_color="red")

def verifywebhook():
    global webhook
    global checkcodeentry
    global code
    global errorlbl2
    global checkcode
    global codes
    webhook = webhookentery.get()
    code = random.randint(1000, 9999)
    codes = str(code)
    webhooktest = DiscordWebhook(url=webhook, content=code)
    webhooktest.execute()
    checkcode = customtkinter.CTk()
    checkcode.geometry("200x200")
    checkcode.title("Code")

    checkcodeentry = customtkinter.CTkEntry(checkcode, placeholder_text="Enter code")
    checkcodeentry.place(relx=0.5, rely=0.5, anchor=CENTER)

    checkbtn = customtkinter.CTkButton(checkcode, text="Verify", command=verify)
    checkbtn.place(relx=0.5, rely=0.6, anchor=CENTER)

    errorlbl2 = customtkinter.CTklabel(checkcode, text=" ", text_color="red")
    errorlbl2.place(relx=0.5, rely=0.7, anchor=CENTER)
    checkcode.mainloop()

main=customtkinter.CTk()
main.geometry("500x400")
main.title("Sending code")


header = customtkinter.CTkLabel(main, text="File Organizer", font=("Arial", 28))
header.place(relx=0.5, rely=0.2, anchor=CENTER)

webhookentery = customtkinter.CTkEntry(main, placeholder_text="Webhook")
webhookentery.place(relx=0.15, rely=0.05, anchor=CENTER)

direntry = customtkinter.CTkButton(main, text="Directory", command=dirask)
direntry.place(relx=0.15, rely=0.14, anchor=CENTER)

checks1 = customtkinter.CTkLabel(main, text="Webhook: Not found", text_color="red")
checks1.place(relx=0.85, rely=0.1, anchor=CENTER)
check2 = customtkinter.CTkLabel(main, text="Directory: Not found", text_color="red")
check2.place(relx=0.85, rely=0.17, anchor=CENTER)


webhooksetup = customtkinter.CTkButton(main, text="Verify webhook", command=verifywebhook)
webhooksetup.place(relx=0.15, rely=0.23, anchor=CENTER)
errorlbl = customtkinter.CTkLabel(main, text=" ", text_color="red")
errorlbl.place(relx=0.5, rely=0.9, anchor=CENTER)
exitbtn = customtkinter.CTkButton(main, text="Exit", command=maindestroy, fg_color="red")
exitbtn.place(relx=0.85, rely=0.0, anchor=N)

checkfileadir = customtkinter.CTkButton(main, text="Check settings", command=vertifysetting)
checkfileadir.place(relx=0.1, rely=0.8, anchor=CENTER)

organizebtn = customtkinter.CTkButton(main, text="Organize", command=organize)
organizebtn.place(relx=0.5, rely=0.8, anchor=CENTER)
if "Webhook: " in logrl and "Directory: " in logrl:
    with open("log.txt", "r") as file:
        lines = file.readlines()

        if len(lines) >= 2:
            webhook_url = lines[0].strip().split('Webhook: ')[1]
            directory_path = lines[1].strip().split('Directory: ')[1]
    webhook_entered = not False
    direntered = not False

    checks1.configure(text="Webhook: Found", text_color="green")
    check2.configure(text="Directory: Found", text_color="green")
elif "Webhook: " in logrl:
    webhook_entered = not False
    checks1.configure(text="Webhook: Found", text_color="green")
elif "Directory: " in logrl:
    direntered = not False
    check2.configure(text="Directory: Found", text_color="green")
else:
    subprocess.run("setup.py", shell=True)

main.mainloop()
