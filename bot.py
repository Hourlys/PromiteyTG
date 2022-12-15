from pyrogram import Client, filters
from pyrogram.errors import FloodWait

from pyrogram.types import ChatPermissions

import time
from time import sleep
import random
from pyrogram import Client
import logging
import os
import csv

api_id = #######
api_hash = "#########"

app = Client("my_account", api_id=api_id, api_hash=api_hash)

@app.on_message()
async def log(client, message):
    
    if (message.from_user):
        if(message.photo):
            file = await app.download_media(message)
            cwd = os.getcwd() 
            patch = cwd + "/message/" + str(message.chat.id) + "/" 

            name_file = file

            if(os.path.exists(patch + "chat.csv")):
                with open(str(patch) + 'chat.csv', 'a') as file:
                    writer = csv.writer(file)     
                    writer.writerow(
                       ( message.date, message.from_user.username,  "Фото(" + str(name_file) + ")" )
                    )
            else:
                with open(str(patch) + 'chat.csv', 'w') as file:
                    writer = csv.writer(file)     
                    writer.writerow(
                        ( message.date, message.from_user.username, "Фото(" + str(name_file) + ")")        
                    )  
                
        else:
            # ЛС проверка
            messagetype = message.chat.type
            if(str(messagetype) == "ChatType.PRIVATE"):   
                
                # Создание папки чата 
                parent_dir = "message/"
                directory = str(str(message.chat.id))

                print( parent_dir + directory )

                if os.path.exists(parent_dir + directory):
                    print("Have Folder")
                else:
                    path = os.path.join(parent_dir, directory) 
                    os.mkdir(path)
                    
                # Эмоджи
                if(message.sticker):


                    cwd = os.getcwd()
                    emoji = message.sticker.emoji
                    patch = cwd + "/message/" + str(message.chat.id) + "/" 
                    if (os.path.exists(patch + "chat.csv")):
                        with open(str(patch) + 'chat.csv', 'a') as file:
                            writer = csv.writer(file)     
                            writer.writerow(
                                ( message.date, message.from_user.username, emoji)
                            )
                    else:
                        with open(str(patch) + 'chat.csv', 'w') as file:
                            writer = csv.writer(file)     
                            writer.writerow(
                                ( message.date, message.from_user.username, emoji)
                                
                            )   

                    
                # Эмоджи казик
                if(message.dice):
                    
                    cwd = os.getcwd()
                    emoji = message.dice.emoji
                    patch = cwd + "/message/" + str(message.chat.id) + "/" 
                    if (os.path.exists(patch + "chat.csv")):
                        with open(str(patch) + 'chat.csv', 'a') as file:
                            writer = csv.writer(file)     
                            writer.writerow(
                                ( message.date, message.from_user.username, emoji)
                            )
                    else:
                        with open(str(patch) + 'chat.csv', 'w') as file:
                            writer = csv.writer(file)     
                            writer.writerow(
                                ( message.date, message.from_user.username, emoji)
                            )

                    
                #Сообщения Все
                else:

                    cwd = os.getcwd()
                    patch = cwd + "/message/" + str(message.chat.id) + "/" 
                    if (os.path.exists(patch + "chat.csv")):
                        with open(str(patch) + 'chat.csv', 'a') as file:
                            writer = csv.writer(file)     
                            writer.writerow(
                                ( message.date, message.from_user.username, message.text)
                                
                            )     
                    else:
                        with open(str(patch) + 'chat.csv', 'w') as file:
                            writer = csv.writer(file)     
                            writer.writerow(
                                ( message.date, message.from_user.username, message.text)
                                
                            )   
                    
    else:
        print(message)

    
app.run()