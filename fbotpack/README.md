# FBotPack: A hyper-simplified, Python-centered package for rapid development of commands for this bot
Version: 0.0.1

### Introduction:
I like Python's syntax, so I didn't feel it necessary to generate a completely new programming language for developing new commands for this bot. Instead, FBotPack aims to boil Python and [discord.py](https://github.com/Rapptz/discord.py) down to a simple package of commands that do the majority of the work for the user.

### Basics:
The most important thing to note is that FBotPack stores the most recently referenced user, channel, server (guild), and message. If a value of any of these types is needed but not provided by the programmer, the cached values will be used.

When using this package to write a `MyCommands.py` file, be sure to begin the `MyCommands.py` document with 
```python
import fbotpack.utils as fbotpack
from botfiles.bot_data import servers
parser = fbotpack.Parser()
``` 
Obviously, the name of the parser variable can be anything. In this document the parser variable will be named `parser`.

#### Python variable types:
A string is a line of text that's enclosed by quotation marks. For example, `"I like pie"` is a string.

An integer is whole number. For example, `3` is an integer. `"I like pie"` is not an integer.

A boolean value is either `true` or `false`.

A list is a series of variables grouped together by square brackets, and separated by commas. For example, `["I", "want", 3, "pies"]` is a list.

A function is a series of instructions. `fbotpack.Parser.erase()` is a function.

### fbotpack.Parser Docs:
Arguments labeled `required` must be included when calling a function. Arguments labeled `optional` can be included when calling the function, but are not necessary.
#### function `fbotpack.Parser.say(required string message, optional boolean mention=False, optional list details=None)` :
`message` is the text that will be sent to the destination server and channel. `details` is a list with the items `[string server_name, string channel_name]`, where `server_name` is the name of the server that the message will be sent to, and `channel_name` is the name of the channel on the server that the message will be sent to. If boolean is True, the user who sent the message is mentioned at the beginning of the message using Discord `@` format.
For example: 
```python
parser.say(message="Hello", mention=False, details=["myserver", "mychannel"])
```
or
```python
parser.say(message="Hello", details=["myserver", "mychannel"])
```
would display the word `Hello` in the channel named `mychannel` on the server named `myserver`. 
```python
parser.say(message="Hello")
```
would display the word `Hello` in the server and channel where the trigger for the command came from.

#### function `fbotpack.Parser.erase(optional string details=None)` :
Optional argument `details` is a string that can contain any combination of `"m"`, `"u"`, and/or `"c"`. If `details` contains `"m"` or `details` is not given, the message that triggered the command is deleted. If `details` contains `"u"`, the user that sent the message is kicked from the guild. If `details` contains `"c"`, the channel that the message was sent to is deleted.
For example:
```python
parser.erase(details="mu")
```
would delete the message that triggered the command, and kick the user that sent the message.
```python
parser.erase(details="m")
```
or
```python
parser.erase()
```
would delete the message that triggered the command.

#### function `fbotpack.Parser.check_contains(required string target, required function do, optional boolean command=False)` :
`target` is the message that the parser will check to see if the message that triggered the command contains. If the message contains `target`, the parser performs the action defined by `do`. If `command` is True, then the target word must be directly preceded by the bot's prefix in order for the parser to perform the action defined by `do`.
For example:
```python
parser.check_contains(target="Hello", do=parser.say(message="Hello", mention=True))
```
would check to see if the message that triggered the command contains the word `Hello`. If so, the bot replies to the author of the message by mentioning them and saying "Hello".
