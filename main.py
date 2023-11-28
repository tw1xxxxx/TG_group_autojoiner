import asyncio 
from asyncio import sleep
import random
from pyrogram import Client, filters
import json
import os

chats1, chats2, joined = [], [], []
api_id = "29055558"
api_hash = "10d8f948b524c548dd4593136ce26aac"

with open('chats.txt', 'r', encoding= 'utf-8') as file: 
    chat_list = (file.read()).split(sep= " ")
    for i in range (len(chat_list)) : chats1.append(chat_list[i].replace('https://t.me/', ""))
    for i in range (len(chat_list)) : chats2.append(chats1[i].replace('/', ""))
async def connect():
    async with Client("test", api_id = api_id, api_hash = api_hash) as app:
        problem = 0
        i = 0
        for i in range(len(chat_list)):
            try:
                await sleep(random.randint(40 , 90))
                await app.join_chat(chat_id=f"@{chats2[i]}")
                joined.append(f"@{chats2[i]}")
                print(f"sucsesfully conected {chats2[i]} chat")
            except:
                problem +=1 
                print(f"Problem with {chats2[i]}")
        print(joined)
        print(f"Sucsesfuly connected {len(chat_list)-problem}\n{problem} Problems with connection")
asyncio.run(connect())