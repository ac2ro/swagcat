import socket , sys
from .prompt import RavePrompt as prompt , Colors

IPV4 = socket.AF_INET
TCP = socket.SOCK_STREAM


DIM = Colors.GRAY
PURPLE = Colors.PURPLE
END = Colors.END

class SwagCatListener():

    def __init__(self , port : int) -> None:
        self.port = port
        sock = socket.socket(IPV4 , TCP)
        sock.bind (('0.0.0.0' , port))
        self.socket = sock

    def start(self):

        sock = self.socket
        sock.listen(1)
        prompt.print_plus(f'Swag listening on {DIM}[{END}{PURPLE}0.0.0.0{END}{DIM}]{END} port {PURPLE}{self.port}{END}')

        try:
            while True:
                
                sock_client , (ip , port) = sock.accept()

                prompt.print_plus(f'Connection established from {PURPLE}{ip}{END} on port {PURPLE}{port}{END}')

            
        except KeyboardInterrupt:
            sock.close()
            sys.exit(0)


