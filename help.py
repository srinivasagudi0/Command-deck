features = """
COMMAND DECK // AVAILABLE COMMANDS

help / commands       Show available commands
time                  Show the current time
coin                  Flip a coin
joke                  Tell a programming joke
motivate              Display a motivational quote
open [app]            Open a Mac application
launch [app]          Open a Mac application
scan                   Check system condition
find [filename]        Find and open a file
recent files           Show recently modified files
protocol coding        Start the coding protocol
protocol study         Start the study protocol
protocol clean state   Prepare applications for shutdown
settings               Customize protocols and theme
exit                   Shut down Command Deck
"""


def help():
    return features.strip()