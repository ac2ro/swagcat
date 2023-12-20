import argparse
from core.prompt import RavePrompt as prompt
from core.listener import SwagCatListener

parser = argparse.ArgumentParser (
    prog = 'Swagcat',

    description = 'Swaggy shell catcher'
)

parser.add_argument('-p' , '--port' , help = 'Port to listen on')

args = parser.parse_args()

try:
    port = int(args.port)
except:
    prompt.print_min('Provide a valid port.')
    exit(0)



listener = SwagCatListener(port)

listener.start()

