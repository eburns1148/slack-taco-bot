# Slack Taco Bot

## Description

This Slack Bot is used to send 5 tacos to a specified user and channel at a specific time everyday

## Requirements
* Python 3
* Slack API Token (https://api.slack.com/custom-integrations/legacy-tokens)

## How to use

### Installation
* Clone this repository
* Run the ```pip3 install -r requirements.txt``` in the cloned directory
* Choose a method below


### Default - bot_runner.py
Requires file modifications to bot_runner.py

* Modify bot_runner.py
  * Set the Slack API Key
  * Set the Slack Channel Name without the '#' symbol
  * Set the Slack User Name without the '@' symbol
  * Set the scheduled time using 24-hr clock (Ex. 9:00 is 9:00AM, 13:00 is 1:00PM)
* Run bot_runner.py using ```python3 bot_runner.py```
* Sit back and eat tacos

### Wizard - bot_runner_wizard.py
Does not require file modifications to any file

* Run bot_runner_wizard.py using ```python3 bot_runner_wizard.py```
  * Enter all values with double quotes
  * Enter your Slack API Key
  * Enter the Slack Channel name without the '#' symbol
  * Enter the Slack Username without the '@' symbol
  * Enter the scheduled time using 24-hr clock (Ex. 9:00 is 9:00AM, 13:00 is 1:00PM)
* Sit back and eat tacos

