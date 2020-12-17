# if you change credits, you get anal cancer and get murdered by russians in 3 days.
"""
Support chatbox for pmpermit.
Used by incoming messages with trigger as /start
Will not work for already approved people.
"""
import asyncio
import io 
import telethon.sync
from telethon.tl.functions.users import GetFullUserRequest
import userbot.plugins.sql_helper.pmpermit_sql as pmpermit_sql
from telethon import events, errors, functions, types
from userbot import ALIVE_NAME
from userbot.utils import admin_cmd


DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Set ALIVE_NAME in heroku vars"
PREV_REPLY_MESSAGE = {}


@command(pattern=r"\/start", incoming=True)
async def _(event):
    chat_id = event.from_id
    userid = event.sender_id
    if not pmpermit_sql.is_approved(chat_id):
        chat = await event.get_chat()
        if event.fwd_from:
            return
        if event.is_private:
         
         PM = ("`Hello. You are accessing the availabe menu of my peru master,`"
               f"{DEFAULTUSER}.\n"
               "__ඔයා ඉන්බොක්ස් ආපු හේතුව දැනගන්න පුලුවන්ද?__\n"
               "**ඉන්බොක්ස් ආපු හේතුව තෝරන්න.:**\n\n"
               "`1`. චැට් කරන්න.\n"
               "`2`. දෙයක් අහගන්න.\n"

               "`3`. උදව්වක් ඉල්ලගන්න.\n"
               "`4`. වෙන දේකට.\n")
         ONE = ("__හරි. ඔයාගෙ ඉල්ලීම යැව්වා.ඉන්බොක්ස් ආපු ගමන් මැසේජ් එකක් දාවි.ඔන්ලයින් එනකන් ඉන්න හොදේ පොඩ්ඩක්.__\n\n"
                "**⚠️ ස්පෑම් කරන්න try කරන්න එපා ප්ලීස්.. ⚠️**\n\n"
                "__Use__ `/start` __to go back to the main menu.__")
         TWO = (" `███████▄▄███████████▄  \n▓▓▓▓▓▓█░░░░░░░░░░░░░░█\n▓▓▓▓▓▓█░░░░░░░░░░░░░░█\n▓▓▓▓▓▓█░░░░░░░░░░░░░░█\n▓▓▓▓▓▓█░░░░░░░░░░░░░░█\n▓▓▓▓▓▓█░░░░░░░░░░░░░░█\n▓▓▓▓▓▓███░░░░░░░░░░░░█\n██████▀▀▀█░░░░██████▀  \n░░░░░░░░░█░░░░█  \n░░░░░░░░░░█░░░█  \n░░░░░░░░░░░█░░█  \n░░░░░░░░░░░█░░█  \n░░░░░░░░░░░░▀▀ `\n\ මම මේකට කැමති නෑ.සොරි. ඔන්ලයින් ඇවිත් අන්බ්ලොක් කරනකල් ඔයාව බ්ලොක් කරන්න වෙනවා.තරහ වෙන්න එපා.**")
         FOUR = ("__හරි හරි.එයා තාම මැසේජ් එක දැක්කෙ නෑ.දැකපු ගමන් රිප්ලයි එකක් දාවි ඔයාට..__\n __අනිත් හේතුව එයාට දැනටමත් මැසේජ් පිරිල තියෙන්නෙ.ඒව කියවන්නත් ඕනනේ එයා.😶__\n **⚠️ ප්ලීස් ස්පෑම් කරන්න එපා.. ⚠️**")
         FIVE = ("`⚠️ අනේ ප්ලීස් .ස්පෑම් කරන්න එපා. ⚠️.**")
         LWARN = ("**⚠️ ස්පෑම් කරන්න එපා.හරිද?එයා එනකල් ඉන්න ඔන්ලයින්. ⚠️.**\n__Use__ `/start` __to go back to the main menu.__")
     
        async with borg.conversation(chat) as conv:
         await borg.send_message(chat, PM)
         chat_id = event.from_id
         response = await conv.get_response(chat)
         y = response.text
         if y == "1":
             await borg.send_message(chat, ONE)
             response = await conv.get_response(chat)
             await event.delete()
             if not response.text == "/start":
                 await response.delete()
                 await borg.send_message(chat, LWARN)
                 response = await conv.get_response(chat)
                 await event.delete()
                 await response.delete()
                 response = await conv.get_response(chat)
                 if not response.text == "/start":
                     await borg.send_message(chat, TWO)
                     await asyncio.sleep(3)
                     await event.client(functions.contacts.BlockRequest(chat_id))
         elif y == "2":
             await borg.send_message(chat, LWARN)
             response = await conv.get_response(chat)
             if not response.text == "/start":
                 await borg.send_message(chat, TWO)
                 await asyncio.sleep(3)
                 await event.client(functions.contacts.BlockRequest(chat_id))
         

         elif y == "3":
             await borg.send_message(chat, FOUR)
             response = await conv.get_response(chat)
             await event.delete()
             await response.delete()
             if not response.text == "/start":
                 await borg.send_message(chat, LWARN)
                 await event.delete()
                 response = await conv.get_response(chat)
                 if not response.text == "/start":
                     await borg.send_message(chat, TWO)
                     await asyncio.sleep(3)
                     await event.client(functions.contacts.BlockRequest(chat_id))
         elif y == "4":
             await borg.send_message(chat,FIVE)
             response = await conv.get_response(chat)
             if not response.text == "/start":
                 await borg.send_message(chat, LWARN)
                 response = await conv.get_response(chat)
                 if not response.text == "/start":
                     await borg.send_message(chat, TWO)
                     await asyncio.sleep(3)
                     await event.client(functions.contacts.BlockRequest(chat_id))
         else:
             await borg.send_message(chat, "`You have entered an invalid command. Please send /start again or do not send another message if you do not wish to be blocked and reported.`")
             response = await conv.get_response(chat)
             z = response.text
             if not z == "/start":
                 await borg.send_message(chat, LWARN)
                 await conv.get_response(chat)
                 if not response.text == "/start":
                     await borg.send_message(chat, TWO)
                     await asyncio.sleep(3)
                     await event.client(functions.contacts.BlockRequest(chat_id))

