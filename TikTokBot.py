import telebot,random,requests

abc = "qwertyuiopasfdghjklzxcbvnm_1234567890"

token = f'5624999187:AAEtZu1AwC72C9bRzhrPsR4LfGt6tybKVuo'

bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
        
        msg0 =f"""
        7LeP BOT
        
By : @qdobop"""
        bot.reply_to(message,msg0)
                

@bot.message_handler(content_types=["text"])
def send_echo(message):
    bot.reply_to(message, "BOT STARTED")
    while True:
        #
        hea = {'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'accept-encoding':'gzip, deflate, br', 'accept-language':'en-US,en;q=0.9,ar;q=0.8','cache-control':'max-age=0', 'sec-ch-ua':'" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"', 'sec-ch-ua-mobile':'?0','sec-fetch-dest':'document', 'sec-fetch-mode':'navigate', 'sec-fetch-site':'same-origin', 'sec-fetch-user':'?1', 'upgrade-insecure-requests':'1', 'user-agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'}
        
        
        user = (''.join((random.choice(abc) for i in range(4))))
        tiko = f'https://www.tiktok.com/@{user}?'
        reqsnd = requests.get(tiko, headers=hea).status_code
        if reqsnd == 404:
            good = 'GOOD TIKTOK > {user}'
            print(good)
            bot.send_message(message.chat.id, good)
        elif reqsnd == 200:
            bad = f'BAD TIKTOK > {user}'
            print(bad)
            bot.send_message(message.chat.id, bad)
            
            
while True:
    try:
        bot.polling(none_stop=True)
    except Exception as e:
        print(e)
