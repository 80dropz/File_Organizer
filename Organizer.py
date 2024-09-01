import time
import subprocess
from discord_webhook import DiscordWebhook
import os
import shutil




logfileread = open("filelog.txt", "r")
logfilereadline = logfileread.readlines()
numlines = len(logfileread.readlines())
file = open("log.txt", "r")
lines = file.readlines()

if len(lines) >= 2:
        webhook_url = lines[0].strip().split('Webhook: ')[1]
        directory_path = lines[1].strip().split('Directory: ')[1]
dircode = os.path.exists(directory_path + "/Code")
dirpic = os.path.exists(directory_path + "/Pictures")
dirmusic = os.path.exists(directory_path + "/Music")
dirgames = os.path.exists(directory_path + "/Games")
numoffiles = DiscordWebhook(webhook_url, content=f"{numlines} Files Found in {directory_path} Organizing now").execute()

for line in logfilereadline:
    line = line.strip()
    linenaked = line.split("= ")[1]
    linenakedlist = {linenaked}
    foldertest = directory_path + "/" + linenaked
    print(linenaked)
    if os.path.isdir(foldertest):
        DiscordWebhook(webhook_url, content=f"Folder Found Scanning Folder").execute()
        print("Folder Found")
        print("Scanning Folder")
        filesinfolder = os.listdir(foldertest)
        print(filesinfolder)
        for file in filesinfolder:
            print(file)
            extension2 = os.path.splitext(file)[1]
            filetest = foldertest + "/" + file
            if os.path.isdir(filetest):
                fileinfile = os.listdir(filetest)
                print(fileinfile)
            elif extension2 == ".exe":
                shutil.moveto(foldertest + "/" + file, dircode)
            elif extension2 == ".mp3":
                shutil.moveto(foldertest + "/" + file, dirmusic)
            elif extension2 == ".jpg":
                shutil.moveto(foldertest + "/" + file, dirpic)
            elif extension2 == ".png":
                shutil.moveto(foldertest + "/" + file, dirpic)
            elif extension2 == ".gif":
                shutil.moveto(foldertest + "/" + file, dirpic)
            elif extension2 == ".mp4":
                shutil.moveto(foldertest + "/" + file, dirpic)
            elif extension2 == ".py":
                shutil.moveto(foldertest + "/" + file, dircode)
            elif extension2 == ".js":
                shutil.moveto(foldertest + "/" + file, dircode)
            elif extension2 == ".html":
                shutil.moveto(foldertest + "/" + file, dircode)
            else:   
                print("nutton")

    else:
        print("File Found")
        time.sleep(.8)
