# funsies-bot
A Discord bot made using discord.py

### General Information
Bot hosted on Heroku with data stored in Amazon S3. Current version fetches a JSON file on load, and loads the entire file into memory, making this bot __*not*__ ideal for use on servers that have large member counts. JSON file is a substitute for an SQL database, but editing `required/userHandler.py` to work with SQL should not be overly difficult.

### Where are the commands?
All bot commands are found in `botfiles/myCommands.py`. `required` contains the utilities needed to make the bot run smoothly.

### Disclaimer
Funsies is still in active development, meaning that it is far from complete. Currently the bot is being developed by only one person, so it lacks proper formatting, comments, documentation, and optimization.

### Collaboration
I am tentatively seeking collaborators for this bot. If you are interested in working with me, submit a pull request and indicate that this is the case. Any and all help is appreciated, including one-off contributions to the source code.
