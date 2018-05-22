from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, ImageSendMessage
)

app = Flask(__name__)

# Channel Access Token
line_bot_api = LineBotApi('4JjhYshgfiZfyUbgkOFWHBBIQ3WVDqb0Ri5LuutOvjm7bJrlcqVNyDVJivFodt49TKSCsBEt7lyFrUW0KA0lKoSKVhNKglF24Nv1YODnF4AqwDyGUOiAESyWU5R1nyvA0/o/8KpNOgkW/NDW89aMLAdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('49478320d999378e22e55573ad2c047c')

# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'

#等待訊息並攔截;後續產生的程式由此方法操控
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    print(event)
    #line用來傳遞event的方法
    message = TextSendMessagetext=event.message.text)
    line_bot_api.reply_message(
        event.reply_token,
        message)

import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
