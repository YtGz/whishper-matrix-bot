import os
import simplematrixbotlib as botlib

matrix_server = "https://matrix.datawarp.dev"
username = os.get_env("USERNAME")
password = os.get_env("PASSWORD")
creds = botlib.Creds(matrix_server, username, password)
bot = botlib.Bot(creds)
PREFIX = '!'

@bot.listener.on_message_event
async def echo(room, message):
    print(message)
    match = botlib.MessageMatch(room, message, bot, PREFIX)
    if match.is_not_from_this_bot() and match.prefix() and match.command("echo"):
        await bot.api.send_text_message(
            room.room_id, " ".join(arg for arg in match.args())
        )

def main() -> int:
    bot.run()
    return 0
