from slackbot.bot import Bot
from slackbot.bot import respond_to
import urllib
import json

@respond_to('thanks')
def love(message):
    message.reply('just doing my job!')

# Parse a Squarespae commerce page in JSON format and respond with tickets left.

@respond_to('tickets')
def totals(ret_message):
    message = []
    url = "http://www.abacbs.org/combineworkshops/?format=json"
    response = urllib.urlopen(url)
    obj = json.load(response)
    for i in obj['items']:
            message.append("\n-----")
            message.append(i['title'])
            for v in i['structuredContent']['variants']:
                message.append("--> variants ")
                message.append("SKU:"+v['sku'])
                if v['unlimited']:
                    message.append("Tickets left: infinite")
                else:
                    message.append("Tickets left:"+str(v['qtyInStock']))

                if (v['onSale']):
                    message.append("Price: ${0:.2f}".format(v['salePrice']/100.0))
                else:
                    message.append("Price: ${0:.2f}".format(v['price']/100.0))

    ret_message.reply('\n'.join(message))

def main():
    bot = Bot()
    bot.run()

if __name__ == "__main__":
    main()
