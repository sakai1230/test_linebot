from linebot import LineBotApi
from linebot.models import TextSendMessage

CHANNEL_ACCESS_TOKEN = 'SEJ26ZEb0DM7IUhv/BQNmczqT379XuPxxkUZ0s+bGq5iWKjW7DLihxWyzNerUNGN/PEZfOjeihuxtygdiv3KNuMrpcE1IgMX/XySPckk9oYBcmhS+UY4haRqORZrmW8VbQxKetjR8Xnj0vvuwGDogAdB04t89/1O/w1cDnyilFU='
line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)

def main():
    USER_ID = 'Uc61807301977299f45ab29dbe3437d5f'
    messages = TextSendMessage(text='やあ')
    line_bot_api.push_message(USER_ID, messages)

if __name__ == "__main__":
    main()