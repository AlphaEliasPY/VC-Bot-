"""
MIT License

Copyright (c) 2021 AlphaMusicRoBo

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import asyncio
from pyrogram import Client, idle, filters
import os
from config import Config
from utils import um, USERNAME, FFMPEG_PROCESSES
from pyrogram.raw import functions, types
import os
import sys
from threading import Thread
from signal import SIGINT
import subprocess
CHAT=Config.CHAT
AlphaMusic = Client(
    "AlphaMusic",
    Config.API_ID,
    Config.API_HASH,
    bot_token=Config.BOT_TOKEN,
    plugins=dict(root="plugins")
)
if not os.path.isdir("./downloads"):
    os.makedirs("./downloads")
def stop_and_restart():
    AlphaMusic.stop()
    os.system("git pull")
    os.execl(sys.executable, sys.executable, *sys.argv)


AlphaMusic.start()

@AlphaMusic.on_message(filters.command(["restart", f"restart@{USERNAME}"]) & filters.user(Config.ADMINS) & (filters.chat(CHAT) | filters.private))
async def restart(client, message):
    await message.reply_text("🔄 Wi8, actualización y reinicio del bot...")
    await asyncio.sleep(3)
    try:
        await message.delete()
    except:
        pass
    process = FFMPEG_PROCESSES.get(CHAT)
    if process:
        try:
            process.send_signal(SIGINT)
        except subprocess.TimeoutExpired:
            process.kill()
        except Exception as e:
            print(e)
            pass
        FFMPEG_PROCESSES[CHAT] = ""
    Thread(
        target=stop_and_restart
        ).start()    


AlphaMusic.send(
    functions.bots.SetBotCommands(
        commands=[
            types.BotCommand(
                command="start",
                description="Comprueba si el bot está vivo"
            ),
            types.BotCommand(
                command="help",
                description="Muestra mensaje de ayuda"
            ),
            types.BotCommand(
                command="play",
                description="Reproducir canción de youtube/archivo de audio"
            ),
            types.BotCommand(
                command="dplay",
                description="Reproducir canción de Deezer"
            ),
            types.BotCommand(
                command="player",
                description="Muestra la canción que se está reproduciendo actualmente con controles"
            ),
            types.BotCommand(
                command="playlist",
                description="Muestra la lista de reproducción"
            ),
            types.BotCommand(
                command="skip",
                description="Omitir la canción actual"
            ),
            types.BotCommand(
                command="join",
                description="Únete a VC."
            ),
            types.BotCommand(
                command="leave",
                description="Salir de VC"
            ),
            types.BotCommand(
                command="vc",
                description="Compruebe si la máquina virtual está unida"
            ),
            types.BotCommand(
                command="stop",
                description="Deja de reproducir"
            ),
            types.BotCommand(
                command="radio",
                description="Iniciar radio / transmisión en vivo"
            ),
            types.BotCommand(
                command="stopradio",
                description="Detiene la radio / transmisión en vivo"
            ),
            types.BotCommand(
                command="replay",
                description="Repetir desde el principio"
            ),
            types.BotCommand(
                command="clean",
                description="Limpia archivos RAW"
            ),
            types.BotCommand(
                command="pause",
                description="Pausa la canción"
            ),
            types.BotCommand(
                command="resume",
                description="Reanudar la canción pausada"
            ),
            types.BotCommand(
                command="mute",
                description="Mudo en VC"
            ),
            types.BotCommand(
                command="volume",
                description="Establecer volumen entre 0-200"
            ),
            types.BotCommand(
                command="unmute",
                description="Activar sonido en VC"
            ),
            types.BotCommand(
                command="restart",
                description="Actualiza y reinicia el bot"
            )
        ]
    )
)

idle()
AlphaMusic.stop()
