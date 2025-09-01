from telegram import Bot, BotCommand, InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ApplicationBuilder, CallbackQueryHandler, CommandHandler, MessageHandler, filters, ContextTypes

STATIC_INFO = {
    "student": "IP-21 Horoshko Mykhailo",
    "technologies": "<b>Technologies</b>: Front-end, Back-end, Web technologies, Databases",
    "contacts": "tel: 068-037-86-34\nemail: goroshkomisha10092005@gmail.com"
}

class TelegramBotHelper:
    def __init__(self, token: str, chatbot):
        self.app = ApplicationBuilder().token(token).build()
        self.chatbot = chatbot
        self.user_state = {} 
        self.token = token

        self.app.add_handler(CommandHandler("start", self.start))
        self.app.add_handler(CommandHandler("menu", self.start))
        self.app.add_handler(CallbackQueryHandler(self.button_handler))
        self.app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), self.message_handler))
    
    async def setup(self):
        bot = Bot(self.token)
        await bot.set_my_commands([
            BotCommand("/start", "Show main menu"),
            BotCommand("/menu", "Back to main menu"),
        ])

    async def show_menu(self, query_or_update):
        keyboard = [
            [InlineKeyboardButton("Student", callback_data="student")],
            [InlineKeyboardButton("It-technologies", callback_data="technologies")],
            [InlineKeyboardButton("Contacts", callback_data="contacts")],
            [InlineKeyboardButton("Chat with GPT", callback_data="chat")],
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)

        if hasattr(query_or_update, "edit_message_text"):
            await query_or_update.edit_message_text("Choose an action:", reply_markup=reply_markup)
        else: 
            await query_or_update.message.reply_text("Choose an action:", reply_markup=reply_markup)

    async def start(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        self.user_state[update.effective_user.id] = "menu"
        await self.show_menu(update)

    async def button_handler(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        query = update.callback_query
        await query.answer()
        user_id = query.from_user.id

        if query.data == "chat":
            self.user_state[user_id] = "chat"
            await query.message.reply_text("You are now in GPT chat mode. Send me a message!")
        elif query.data in STATIC_INFO:
            await query.edit_message_text(
                STATIC_INFO[query.data],
                reply_markup=InlineKeyboardMarkup(
                    [[InlineKeyboardButton("Back", callback_data="back")]]
                ), 
                parse_mode="HTML"
        )
        elif query.data == "back":
            self.user_state[user_id] = "menu"
            await self.show_menu(query)

    async def message_handler(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        user_id = update.message.from_user.id
        state = self.user_state.get(user_id, "menu")

        if state == "chat":
            await context.bot.send_chat_action(chat_id=update.effective_chat.id, action="typing")
            reply = self.chatbot.ask(update.message.text)
            await update.message.reply_text(reply)
        elif state == "menu":
            await update.message.reply_text("Please choose an option from the menu using /start.")
        else:
            await update.message.reply_text("Press 'Back' to return to the main menu.")

    def run(self):
        self.app.run_polling()