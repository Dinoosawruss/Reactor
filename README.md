# Reactor
A simple bot that adds different reactions to set users

## HOW TO USE:
1) Download this bot and python (https://www.python.org/)
2) Go to https://discordapp.com/developers/applications/
3) Create an application
4) Create a bot and get token: `Bot > Add Bot > Token > Copy`
5) Paste Token into `TOKEN = 'X'` and replace the X in the python file
6) Open CMD
7) Type: `pip install -U git+https://github.com/Rapptz/discord.py@rewrite#egg=discord.py[voice]`
8) Go to python and run file
9) Invite your bot to discord
10) Your bot works!
If you have any issues with this simply create an issue

## HOW TO ADD USERS TO FILE
```json
{
  "users": [
    {
      "name": "Lots#3840",
      "react": "\ud83c\udfcf"
    },
	  {
      "name": "Dinoosawruss#5358",
      "react": "\ud83e\udd13"
    }
  ]
}
```
Your default JSON will look like this. 
To add a new user copy the **TOP** user and paste it on a new line after the comma
It should look like this:
```json
{
  "users": [
    {
      "name": "Lots#3840",
      "react": "\ud83c\udfcf"
    },
    {
      "name": "Lots#3840",
      "react": "\ud83c\udfcf"
    },
	  {
      "name": "Dinoosawruss#5358",
      "react": "\ud83e\udd13"
    }
  ]
}
```
Then sub out the `"name": "Lots#3840"` with the users discord name and number
```json
{
  "users": [
    {
      "name": "Lots#3840",
      "react": "\ud83c\udfcf"
    },
    {
      "name": "JohnDoe#0001",
      "react": "\ud83c\udfcf"
    },
	  {
      "name": "Dinoosawruss#5358",
      "react": "\ud83e\udd13"
    }
  ]
}
```
Then find the emoji you'd like to use
Then find the **UNICODE** for this emoji which can be found here:
https://gist.github.com/Vexs/629488c4bb4126ad2a9909309ed6bd71
It will look something like `\ud83e\udd13`
Simply change the `"\ud83c\udfcf"` to the unicode you found
```json
{
  "users": [
    {
      "name": "Lots#3840",
      "react": "\ud83c\udfcf"
    },
    {
      "name": "JohnDoe#0001",
      "react": "\ud83e\udd13"
    },
	  {
      "name": "Dinoosawruss#5358",
      "react": "\ud83e\udd13"
    }
  ]
}
```
After this your file should look something like this. If you have any errors please create an issue
