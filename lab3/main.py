from dotenv import load_dotenv
import os
import asyncio

from gpt_helper import GPT4Helper
from telegram_bot_helper import TelegramBotHelper

load_dotenv()
openai_api_key=os.getenv("OPEN_API_KEY")
token = os.getenv("BOT_TOKEN")

chatbot = GPT4Helper(openai_api_key)
bot_helper = TelegramBotHelper(token, chatbot)

async def setup():
    await bot_helper.setup() 

loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)
loop.run_until_complete(setup())
bot_helper.run()