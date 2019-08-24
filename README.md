[![Codacy Badge](https://api.codacy.com/project/badge/Grade/8d2a348a96014c2a90b0f3ab62c0a2d7)](https://app.codacy.com/app/padkinsdev/funsies-bot?utm_source=github.com&utm_medium=referral&utm_content=padkinsdev/funsies-bot&utm_campaign=Badge_Grade_Dashboard)
[![CodeFactor](https://www.codefactor.io/repository/github/padkinsdev/funsies-bot/badge)](https://www.codefactor.io/repository/github/padkinsdev/funsies-bot)
[![Coverage Status](https://coveralls.io/repos/github/padkinsdev/funsies-bot/badge.svg?branch=master)](https://coveralls.io/github/padkinsdev/funsies-bot?branch=master)
[![Build Status](https://travis-ci.org/padkinsdev/funsies-bot.svg?branch=master)](https://travis-ci.org/padkinsdev/funsies-bot)

# funsies-bot
A Discord bot made using discord.py

### General Information
Bot hosted on Heroku with data stored in Amazon S3. Current version fetches a JSON file on load, and loads the entire file into memory, making this bot __*not*__ ideal for use on servers that have large member counts. JSON file is a substitute for an SQL database, but editing `required/userHandler.py` to work with SQL should not be overly difficult.

### Where are the commands?
All bot commands are found in `botfiles/myCommands.py`. `required` contains the utilities needed to make the bot run smoothly.

### Disclaimer
Funsies is still in active development, meaning that it is far from complete. Currently the bot is being developed by only one person, so it lacks proper formatting, comments, documentation, and optimization.
