"""
MIT License

Copyright (c) 2021 UltronRoBo

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

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram import Client, filters
from utils import USERNAME, um
from config import Config
U=USERNAME
CHAT=Config.CHAT
msg=Config.msg
HOME_TEXT = "<b>Hemlo, [{}](tg://user?id={})\n\nSoy AndroidCaveMusic, un robot de música para reproducir música en canales y grupos 24*7.\n\nIncluso puedo transmitir Youtube en vivo en su chat de voz.\n\nPegar /help conocer los comandos disponibles.</b>"
HELP = """
<b>Agregue el bot y la cuenta de usuario en su grupo con derechos de administrador.
Iniciar un chat de voz.
Use /play <nombre de la canción> o use / play como respuesta a un archivo de audio o enlace de youtube.
También puedes usar /dplay <nombre de la canción> para reproducir una canción de Deezer. </b>
**Comandos comunes**:
**/play** Responde a un archivo de audio o enlace de YouTube para reproducirlo o usa / reproduce <nombre de la canción>.
**/dplay** Reproduce música de Deezer, usa / dplay <nombre de la canción>
**/player** Muestra la canción que se está reproduciendo actualmente.
**/help** Mostrar ayuda para los comandos
**/playlist** Muestra la lista de reproducción.
** Comandos de administrador **:
**/skip** [n] ... Omitir actual on donde n>= 2
**/join** Únete al chat de voz.
**/leave** Dejar el chat de voz actual
**/vc** Compruebe qué VC está unido.
**/stop** Deja de jugar.
**/radio** Iniciar radio.
**/stopradio** Detiene la transmisión de radio.
**/replay ** Juega desde el principio.
**/clean** Elimina archivos PCM RAW no utilizados.
**/pause** Pausa la reproducción.
**/resume** Reanudar la reproducción.
**/volume** Cambiar volumen (0-200).
**/mute** Mute en VC.
**/unmute** Activar sonido en VC.
**/restart** Actualiza y reinicia el Bot.
"" "



@Client.on_message(filters.command(['start', f'start@{U}']))
async def start(client, message):
    buttons = [
        [
        InlineKeyboardButton('⚙️ Support Group', url='https://t.me/AndroidCave'),
    ],
    [
        InlineKeyboardButton('🧑‍💻 Developer', url='https://t.me/AlphaElias'),
        InlineKeyboardButton('🗃 Source', url='https://github.com/UltronRoBo/UltronMusic/'),
    ],
    [
        InlineKeyboardButton('👨🏼‍🦯 Help', callback_data='help'),
        
    ]
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    k=await message.reply(HOME_TEXT.format(message.from_user.first_name, message.from_user.id), reply_markup=reply_markup)
    await um.delete(k)
    await um.delete(message)



@Client.on_message(filters.command(["help", f"help@{U}"]))
async def show_help(client, message):
    buttons = [
        [
            InlineKeyboardButton('⚙️ Support Group', url='https://t.me/AndroidCave'),
        ],
        [
            InlineKeyboardButton('🧑‍💻 Developer', url='https://t.me/AlphaElias'),
            InlineKeyboardButton('🗃 Source', url='https://github.com/UltronRoBo/UltronMusic/'),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    if msg.get('help') is not None:
        await msg['help'].delete()
    msg['help'] = await message.reply_text(
        HELP,
        reply_markup=reply_markup
        )
    await um.delete(message)
