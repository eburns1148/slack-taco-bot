'''
Created on Apr 28, 2017

@author: Eric Burns
'''

from slackclient import SlackClient
import schedule
import time


class SlackTacoBot:
    
    def __init__(self, slackApiToken, channelName, userName, dailyTime):
        self.channelName = channelName
        self.userName = userName
        self.dailyTime = dailyTime
        
        self.slackClient = SlackClient(slackApiToken)
    
    def start(self):

        print('Slack Channel Name: #' + self.channelName)
        print('Slack User Name: @' + self.userName)
        
        schedule.every().day.at(self.dailyTime).do(self._sendTacos)
        print('Running SlackTacoBot everyday at ' + self.dailyTime)
        
        while True:
            schedule.run_pending()
            time.sleep(60)
        
    def _sendTacos(self):
        print('Sending TACOS to @' + self.userName + ' on channel #' + self.channelName)
    
        text = '<@'+ self.userName +'> :taco: :taco: :taco: :taco: :taco:'
    
        self.slackClient.api_call(
            "chat.postMessage",
            channel=self.channelName,
            text=text,
            as_user="true")

