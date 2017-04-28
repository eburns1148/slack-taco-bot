

from slack_taco_bot import SlackTacoBot


slackApiToken = input('Enter your Slack API Token: ')
channelName = input('Enter the Slack Channel: #')
userName = input('Enter the Slack User you would like to send 5 tacos to: @')
dailyTime = input('Enter the time would you like to send tacos everyday (Ex. 9:00): ')

bot = SlackTacoBot(
    slackApiToken=slackApiToken,
    channelName=channelName,
    userName=userName,
    dailyTime=dailyTime
    )

bot.start()