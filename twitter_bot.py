from cPickle import load
import tweepy
from os import remove

# Use the keys and secrets from twitter account
auth = tweepy.OAuthHandler('consumer_key', 'consumer_secret')
auth.set_access_token('access_key', 'access_secret')
api = tweepy.API(auth)

# Make sure all the lines are < 280 characters
lines = open("time_results.tsv").read().splitlines()
temp = lines[0].split('\t')

api.update_status(temp[1] + '\n' + temp[2] + '\n' + temp[3])

with open("time_results.tsv", 'w') as f:
    for line in lines[1:]:
        f.write(line + '\n')

if lines != []: 
    temp = lines[1].split('\t')
    time = temp[0].split(':')
    cron_job =  time[1] + " " + time[0] + " * * * sudo python twitter_bot.py\n"
            
    with open("/etc/cron.d/per_minute", 'w') as f:
        f.write(cron_job)

else:
    remove("/home/pi/bot/per_minute")