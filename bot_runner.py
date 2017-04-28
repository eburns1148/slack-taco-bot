

from slack_taco_bot import SlackTacoBot

bot = SlackTacoBot(
    slackApiToken="ENTER YOUR SLACK API TOKEN",
    channelName="sampleChannel",
    userName="sampleUser",
    dailyTime="9:00"
    )

bot.start()