#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on Apr 28, 2017

@author: Eric Burns
'''

from slackclient import SlackClient

from datetime import datetime
import schedule
import time



class SlackTacoBot:
    
    def __init__(self, slackApiToken, channelName, userName, dailyTime):
        self.channelName = channelName
        self.userName = userName
        self.dailyTime = dailyTime
        
        self.slackClient = SlackClient(slackApiToken)
    
    def start(self):

        self._slackBotPrint('Slack Channel Name: #' + self.channelName)
        self._slackBotPrint('Slack User Name: @' + self.userName)
        
        schedule.every().day.at(self.dailyTime).do(self._sendTacos)
        self._slackBotPrint('Running SlackTacoBot everyday at ' + self.dailyTime)
        
        while True:
            schedule.run_pending()
            time.sleep(5)
        
    def _sendTacos(self):
        self._slackBotPrint('Sending TACOS to @' + self.userName + ' on channel #' + self.channelName)
    
        text = '<@'+ self.userName +'> :taco: :taco: :taco: :taco: :taco:'
    
        self.slackClient.api_call(
            "chat.postMessage",
            channel=self.channelName,
            text=text,
            as_user="true")
        
    def _slackBotPrint(self, message):
        print('[' + str(datetime.now()) + ']    ' + '[SlackTacoBot] : ' + message)
