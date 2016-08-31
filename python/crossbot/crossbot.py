from slackbot.bot import Bot
from slackbot.bot import listen_to
from slackclient import SlackClient
from slackbot_settings import API_TOKEN
import re

sc = SlackClient(API_TOKEN)

@listen_to('<#.*>')
def single_cell(message):
    """Listen for mention of any channel. When a channel is mentioned,
    post contents of message to that channel.
    """
    message_text = message.body['text']
    re_result = re.search('<#([a-zA-Z0-9]*)>', message_text)
    channel = re_result.group(1)

    sc.api_call(
            "chat.postMessage", channel=channel, text=message_text,
            username='crossbot', icon_emoji=':rage:'
    )

def main():
    bot = Bot()
    bot.run()


if __name__ == "__main__":
    main()
