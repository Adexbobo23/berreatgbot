# Telegram Bot for Group Management

This is a simple Telegram bot that welcomes new members, bids farewell to members leaving the group, provides helpful commands, and handles anti-spam functionality. Additionally, it includes a community airdrop announcement feature and a `/groupinfo` command for group administrators.

## Features

* **Welcome new members**: Sends a personalized welcome message when a new member joins the group.
* **Airdrop Announcement**: After welcoming a new member, sends an airdrop message with a link to participate in the airdrop.
* **Goodbye message**: Sends a farewell message when a member leaves the group.
* **Anti-spam**: Automatically deletes messages containing bad words (customizable).
* **Command `/help`**: Lists available commands.
* **Command `/groupinfo`**: Provides group info (admin only).

## Installation

1. **Clone this repository** (or download the script):

   ```bash
   git clone https://github.com/your-username/telegram-bot.git
   cd telegram-bot
   ```

2. **Install dependencies**:

   You'll need Python 3.x and the `pyTelegramBotAPI` library. Install the required dependencies via `pip`:

   ```bash
   pip install pyTelegramBotAPI
   ```

3. **Create a bot on Telegram**:

   To use this bot, you need to create a bot on Telegram. Follow these steps:

   * Open Telegram and search for the **BotFather**.
   * Type `/newbot` and follow the instructions.
   * After creating the bot, you'll receive a **Bot Token**.

4. **Update the bot token**:

   Replace `YOUR_BOT_TOKEN` with your Telegram bot token in the script:

   ```python
   BOT_TOKEN = 'YOUR_BOT_TOKEN'
   ```

5. **Run the bot**:

   After updating the token, run the bot script:

   ```bash
   python bot.py
   ```

   The bot should now be running and responding to group events.

## How It Works

* When a new member joins the group, the bot sends a welcoming message and an airdrop announcement.
* When a member leaves the group, the bot sends a goodbye message.
* The bot checks all incoming messages for bad words and deletes them if found.
* It also listens for `/help` and `/groupinfo` commands to provide the appropriate responses.

## Commands

* `/help`: Shows a list of available commands.
* `/groupinfo`: Displays information about the group (admin only).

## Anti-Spam Feature

The bot has a simple anti-spam feature that deletes messages containing bad words. You can customize the list of bad words by modifying the `BAD_WORDS` list in the script:

```python
BAD_WORDS = ['spamword1', 'badword2', 'badlink']
```

## Customization

You can customize the bot by changing the following:

* **Welcome message**: Modify the `welcome_text` inside the `welcome_new_member` function.
* **Airdrop message**: Customize the airdrop message text and URL inside the same function.
* **Bad words**: Modify the `BAD_WORDS` list to add or remove words that you want to block.
* **Goodbye message**: Modify the `member_left` function for the farewell message.

## License

This bot is open-source and released under the MIT License.

