#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys

sys.path.append(os.path.join(sys.path[0], 'src'))

from slack_taco_bot import SlackTacoBot

bot = SlackTacoBot(
    slackApiToken="ENTER YOUR SLACK API TOKEN",
    channelName="sampleChannel",
    userName="sampleUser",
    dailyTime="9:00"
    )

bot.start()