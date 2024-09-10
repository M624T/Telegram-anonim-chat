from flask import Flask, request
import telebot
import config
import os  # Import os to access environment variables

app = Flask(__name__)
bot = telebot.TeleBot(config.TOKEN)

@app.route('/webhook', methods=['POST'])
def webhook():
    json_str = request.get_data(as_text=True)
    update = telebot.types.Update.de_json(json_str)
    bot.process_new_updates([update])
    return '', 200

@app.route('/')
def index():
    return 'Bot is running!'

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))  # Get port from environment variable or default to 10000
    bot.remove_webhook()
    bot.set_webhook(url=f'https://telegram-anonim-chat.onrender.com')  # Update with your actual Render URL
    app.run(host='0.0.0.0', port=port)  # Bind to the port specified by Render.com
