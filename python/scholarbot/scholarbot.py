from slackbot.bot import Bot
from slackbot.bot import respond_to
from slackclient import SlackClient
from slackbot_settings import API_TOKEN
import re
from scholar_script import  ScholarQuerier,ScholarSettings,SearchScholarQuery

sc = SlackClient(API_TOKEN)

def scholar_wrapper():
    querier = ScholarQuerier()
    settings = ScholarSettings()
    querier.apply_settings(settings)

    query = SearchScholarQuery()

    return (querier,query)
    
@respond_to('doi (.*)')
def doi(message,something):
    message.reply('Try this link: {}'.format("http://dx.doi.org/"+something))

@respond_to('who cited (.*)')
def cited_by(message,something):
    querier, query = scholar_wrapper()
    query.set_words(something)

    querier.send_query(query)

    first_hit = querier.articles[0]
    message.reply('{}'.format(first_hit['url_citations']))

@respond_to('papers by (.*)')
def papers_by(message,something):
    querier, query = scholar_wrapper()
    query.set_author(something)

    querier.send_query(query)
    reply_text=""
    for a in querier.articles:
       reply_text += a.as_txt()+"\n" 
    message.reply('Response for author {}:{}'.format(something,reply_text))


@respond_to('first link(.*)')
def giveme(message, something):

    querier, query = scholar_wrapper()
    query.set_words(something)

    querier.send_query(query)
    # Print the URL of the first article found
    print(querier.articles[0]['url'])

    message.reply('First link for {} is {}'.format(something,querier.articles[0]['url']))


def main():
    bot = Bot()
    bot.run()


if __name__ == "__main__":
    main()
