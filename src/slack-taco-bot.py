'''
Created on Apr 28, 2017

@author: Eric Burns
'''

from slackclient import SlackClient
import schedule
import time

if __name__ == '__main__':
    pass

slackToken = input('Enter your Slack API Token: ')
slackClient = SlackClient(slackToken)

slackChannel = input('Enter the Slack Channel: #')
slackUserName = input('Enter the Slack User you would like to send 5 tacos to: @')
dailyTime = input('Enter the time would you like to send tacos everyday (Ex. 9:00): ')


def send5Tacos():
    username = slackUserName
    channel = slackChannel

    print('Sending tacos to @' + username + ' on channel #' + channel)
    
    text = '<@'+ slackUserName +'> :taco: :taco: :taco: :taco: :taco:'
    
    slackClient.api_call(
        "chat.postMessage",
        channel=channel,
        text=text,
        as_user="true")
    

schedule.every().day.at(dailyTime).do(send5Tacos)
print('Running SlackTacoBot every day at ' + dailyTime)

while True:
    schedule.run_pending()
    time.sleep(60)
