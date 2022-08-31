from linebot import LineBotApi
from linebot.models import TextSendMessage
from linebot.exceptions import LineBotApiError

line_bot_api = LineBotApi('SEJ26ZEb0DM7IUhv/BQNmczqT379XuPxxkUZ0s+bGq5iWKjW7DLihxWyzNerUNGN/PEZfOjeihuxtygdiv3KNuMrpcE1IgMX/XySPckk9oYBcmhS+UY4haRqORZrmW8VbQxKetjR8Xnj0vvuwGDogAdB04t89/1O/w1cDnyilFU=')

try:
    line_bot_api.reply_message('<reply_token>', TextSendMessage(text='Hello World!'))
except LineBotApiError as e:
    # error handle
    ...