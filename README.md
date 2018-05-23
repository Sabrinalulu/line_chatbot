# Line Bot 
(This README.md is reference to [yaoandy107](https://github.com/yaoandy107/line-bot-tutorial))

A Python program presents how to create a LINE Bot SDK on Heroku.

If you want to use other languages to set up LINE BOT, check out LINE Bot SDK repositories as follows:
- [PHP](https://github.com/line/line-bot-sdk-php)
- [Go](https://github.com/line/line-bot-sdk-go)
- [Perl](https://github.com/line/line-bot-sdk-perl)
- [Ruby](https://github.com/line/line-bot-sdk-ruby)
- [Python](https://github.com/line/line-bot-sdk-python)
- [Node.js](https://github.com/line/line-bot-sdk-nodejs)

## At the very first

Verify you have already：

- created a Messaging API on LINE backend control panel [Official Guide](https://developers.line.me/en/docs/messaging-api/getting-started/)
- created a [Heroku](https://www.heroku.com) account (free)

## Implement

1. Log in [Heroku](https://dashboard.heroku.com/apps)，click New -> Create New App   
  ![](https://github.com/Sabrinalulu/line_chatbot/blob/master/pictures/create.png)
2. Set an App name you like and click Create App 
  ![](https://github.com/Sabrinalulu/line_chatbot/blob/master/pictures/create1.png)
3. Download [sample code](https://github.com/yaoandy107/line-bot-tutorial/archive/master.zip)
4. Enter [Line setting](https://developers.line.me/console/) to add new provider and select it
  ![](https://github.com/Sabrinalulu/line_chatbot/blob/master/pictures/line_panel.png)
5. Get **channel secret** and **channel access token**，if there aren't any texts，click Issue
6. Open sample code file: 'app.py' on your IDE ，input **channel secret** and **channel access token** into hint fields
  ![](https://github.com/Sabrinalulu/line_chatbot/blob/master/pictures/token1.png)
7. Use Heroku CLI to deploy the code onto Heroku（Please refer to [How to use Heroku CLI](#How-to-use-Heroku-CLI))
8. Use the below URL to set webhook URL on the app control panel(LINE)
  `{HEROKU_APP_NAME}.herokuapp.com/callback`
  NOTE：{HEROKU_APP_NAME} is the name which you set at step 2
  NOTE：If you would like to control which messages will be sent back, the webhooks has to be enabled. 
  NOTE："Allow bot to join group chats" controls group chatbot or one-to-one.
  ![](https://github.com/Sabrinalulu/line_chatbot/blob/master/pictures/setting.png)
9. Scan the QR Code on LINE “Channel settings” , your chatbot will be add into your friend list
10. Send text messages to the chatbot on LINE, verify it has been created successfully

## How to use Heroku CLI 
(Terminal)

1. Download and install [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli)、[Git](https://git-scm.com/)
2. Locate to your smaple code file
3. Login to Heroku
```shell＝
heroku login
```
4. Initialize git
(當有一個專案在網路上運行的，但從來沒做過版本管理，此時想為他做版本管理時，且已安裝git後的情況下。操作時，首先設定全域的使用者與e-mail)
``` shell=
$ git config --global user.name "user_name"
$ git config --global user.email "user_mail"
```
5. Set the file under git environment
```shell＝
git init
```
6. Login to heroku (Enter your email and password)
```shell＝
heroku login
```
7. Use git to link the local file and heroku
```shell＝
git remote add "heroku" https://git.heroku.com/{HEROKU_APP_NAME}.git
```
    Note：{HEROKU_APP_NAME} is name which you set at step 2
    Note：remove -v to make sure it is fine
7. Add all files under the sample code folder into the git list
```shell
git add .
```
8. Store the checkpoint
```shell
git commit -m "Init"
```
    Note：Any texts can be substitute for "Init" 
9. Push files on the git list to heroku, be careful to verify whether the process is sucessful
```shell
git push heroku master
```
**When updating the code, you just need to execute step 7,8,9**

## Explanation
```
You need two files to run the program on heroku
```
- Procfile：let heroku run code，web: {language} {file_name}，language: python，the file going to execute: app.py，so we change the original one to **web: python app.py**。
- requirements.txt：every package you need. Heroku will follow this file to install packages.

### app.py
Manipulate handle_message() to present differnt replies

![](https://i.imgur.com/DNeNbpV.png)


## Others
[Official Guide](https://github.com/line/line-bot-sdk-python#api)
### Basic Operation
#### Reply Message
```python
line_bot_api.reply_message(reply_token, 訊息物件)
```
#### Automatical send
bot needs a push method to implement，or it may pop out errors
```python
line_bot_api.push_message(push_token, 訊息物件)
```

### Sendind message objects

[Official Guide](https://devdocs.line.me/en/#send-message-object)

Modify handle_message() method in the sample code to present differnt functions.

#### TextSendMessage （文字訊息）
```python
message = TextSendMessage(text='Hello, world')
line_bot_api.reply_message(event.reply_token, message)
```
#### ImageSendMessage（圖片訊息）
```python
message = ImageSendMessage(
    original_content_url='https://example.com/original.jpg',
    preview_image_url='https://example.com/preview.jpg'
)
line_bot_api.reply_message(event.reply_token, message)
```

#### VideoSendMessage（影片訊息）
```python
message = VideoSendMessage(
    original_content_url='https://example.com/original.mp4',
    preview_image_url='https://example.com/preview.jpg'
)
line_bot_api.reply_message(event.reply_token, message)
```

#### AudioSendMessage（音訊訊息）
```python
message = AudioSendMessage(
    original_content_url='https://example.com/original.m4a',
    duration=240000
)
line_bot_api.reply_message(event.reply_token, message)
```
#### LocationSendMessage（位置訊息）
```python
message = LocationSendMessage(
    title='my location',
    address='Tokyo',
    latitude=35.65910807942215,
    longitude=139.70372892916203
)
line_bot_api.reply_message(event.reply_token, message)
```

#### StickerSendMessage（貼圖訊息）
```python
message = StickerSendMessage(
    package_id='1',
    sticker_id='1'
)
line_bot_api.reply_message(event.reply_token, message)
```

#### ImagemapSendMessage
```python
message = ImagemapSendMessage(
    base_url='https://example.com/base',
    alt_text='this is an imagemap',
    base_size=BaseSize(height=1040, width=1040),
    actions=[
        URIImagemapAction(
            link_uri='https://example.com/',
            area=ImagemapArea(
                x=0, y=0, width=520, height=1040
            )
        ),
        MessageImagemapAction(
            text='hello',
            area=ImagemapArea(
                x=520, y=0, width=520, height=1040
            )
        )
    ]
)
line_bot_api.reply_message(event.reply_token, message)
```

#### TemplateSendMessage - ButtonsTemplate （按鈕介面訊息）
```python
message = TemplateSendMessage(
    alt_text='Buttons template',
    template=ButtonsTemplate(
        thumbnail_image_url='https://example.com/image.jpg',
        title='Menu',
        text='Please select',
        actions=[
            PostbackTemplateAction(
                label='postback',
                text='postback text',
                data='action=buy&itemid=1'
            ),
            MessageTemplateAction(
                label='message',
                text='message text'
            ),
            URITemplateAction(
                label='uri',
                uri='http://example.com/'
            )
        ]
    )
)
line_bot_api.reply_message(event.reply_token, message)
```

#### TemplateSendMessage - ConfirmTemplate（確認介面訊息）
```python
message = TemplateSendMessage(
    alt_text='Confirm template',
    template=ConfirmTemplate(
        text='Are you sure?',
        actions=[
            PostbackTemplateAction(
                label='postback',
                text='postback text',
                data='action=buy&itemid=1'
            ),
            MessageTemplateAction(
                label='message',
                text='message text'
            )
        ]
    )
)
line_bot_api.reply_message(event.reply_token, message)
```

#### TemplateSendMessage - CarouselTemplate
```python
message = TemplateSendMessage(
    alt_text='Carousel template',
    template=CarouselTemplate(
        columns=[
            CarouselColumn(
                thumbnail_image_url='https://example.com/item1.jpg',
                title='this is menu1',
                text='description1',
                actions=[
                    PostbackTemplateAction(
                        label='postback1',
                        text='postback text1',
                        data='action=buy&itemid=1'
                    ),
                    MessageTemplateAction(
                        label='message1',
                        text='message text1'
                    ),
                    URITemplateAction(
                        label='uri1',
                        uri='http://example.com/1'
                    )
                ]
            ),
            CarouselColumn(
                thumbnail_image_url='https://example.com/item2.jpg',
                title='this is menu2',
                text='description2',
                actions=[
                    PostbackTemplateAction(
                        label='postback2',
                        text='postback text2',
                        data='action=buy&itemid=2'
                    ),
                    MessageTemplateAction(
                        label='message2',
                        text='message text2'
                    ),
                    URITemplateAction(
                        label='uri2',
                        uri='http://example.com/2'
                    )
                ]
            )
        ]
    )
)
line_bot_api.reply_message(event.reply_token, message)
```

#### TemplateSendMessage - ImageCarouselTemplate
```python
message = TemplateSendMessage(
    alt_text='ImageCarousel template',
    template=ImageCarouselTemplate(
        columns=[
            ImageCarouselColumn(
                image_url='https://example.com/item1.jpg',
                action=PostbackTemplateAction(
                    label='postback1',
                    text='postback text1',
                    data='action=buy&itemid=1'
                )
            ),
            ImageCarouselColumn(
                image_url='https://example.com/item2.jpg',
                action=PostbackTemplateAction(
                    label='postback2',
                    text='postback text2',
                    data='action=buy&itemid=2'
                )
            )
        ]
    )
)
line_bot_api.reply_message(event.reply_token, message)
```
