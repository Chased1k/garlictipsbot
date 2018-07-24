# quantistipbot
Quantis tipbot built in Python. Probably ready for production use, but I'd give it a few days. Recoded from the ground up, this is version 2. Version 1 will never be spoken of again.

# Instructions

Coming soon. You can probably figure it out for now, the sql file is for MySQL so you will need that on your server. You will also need a full node of whatever software you're running, and the cli program as that's what we use for deposits and withdrawals. While this is for Quantis it could very easily be used for other cryptos.

Eventually we will have a config file where we can declare all this, for now just search quantis-cli in tipbot.py

Note the MySQL & Reddit config is in utils.py, you will need this information before you can use the bot.

Also note you will need to run the python programs in some kind of loop, in bash I just do this:
> while true; do /usr/bin/python /home/monotoko/build/reddit/tipbot.py; sleep 15; done

# ToDo
quantis-cli needs to be changed to quantisd
the location of quantisd needs to be changed in .json
location of quantisd needs to be changed in all files
quotes and fun stuff need to be customized to quantis
figure out the .sql file
figure out the mysql shiz
install all dependencies via pip (or pip3)
use the bash script suggested to keep bot running

# Testing

Happy to accept pull requests, especially people good with automated testing. It took me hours to manually test this, hours!
