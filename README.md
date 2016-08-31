# slackbots-for-research
A collection of Slackbot scripts for research groups using http://Slack.com



## Python

Python bots are based on: https://github.com/lins05/slackbot

Also uses the official Slackbot client https://github.com/slackhq/python-slackclient

### Requirements:

- Python 2.7
- slackbot
- slackclient

#### Set up

To set up using [Conda](http://conda.pydata.org/miniconda.html):  

```bash
conda create --name slackbot --python=2.7  
source activate slackbot  
pip install slackbot  
pip install slackclient  
```

Create a file in the same directory as the python script for that bot, 
called `slackbot_settings.py`.
For example `python/crossbot/`. 

It should contain the following:

```python
API_TOKEN = "your API token"
```

You can get your API token by creating a new slackbot in Slack, and copying the API token.

#### Run

The bot needs to be running in order to respond to events.
You may wish to run it on a server using `screen` so it is up all the time.
(Naming you screen with -S is optional, but I like to do it so future me remembers what it is.)

```bash
screen -S crossbot
cd /path/to/slackbots-for-research/python
python crossbot.py
```

Then `ctrl-a d` to detach from screen, and it's safe to log off the server.
