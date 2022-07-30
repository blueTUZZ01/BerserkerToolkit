from rich.console import Console
from rich.panel import Panel
import cv2
import argparse

console = Console()

parser = argparse.ArgumentParser(description='---')
parser.add_argument("IP", help='IP')
parser.add_argument("PORT", help='PORT')
parser.add_argument("PROTOCOL", help="CONNECTION PROTOCOL")
parser.add_argument('-nps', '--needPassword', action='store_true', help='USE IF CAMERA NEEDS PASSWORD')
args = parser.parse_args()

PORT = args.PORT
PROT = args.PROTOCOL
IP = args.IP


def withoutPass():
    stream = cv2.VideoCapture(f'{PROT}://{IP}:{PORT}/1')

    while True:
        r, f = stream.read()
        cv2.imshow("IP CAMERA STREAM", f)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cv2.destroyAllWindows()


def withPass():
    yorn = console.input('[red]DO YOU KNOW LOGIN AND PASSWORD? [red blink](Y/N)[/][/]: ')
    if yorn == 'y'.lower():
        login = console.input('[red]LOGIN: [/]')
        password = console.input('[red]PASSWORD: [/]')

        stream = cv2.VideoCapture(f'{PROT}:://{login}:{password}@{IP}:{PORT}/1')

    else:
        filename = console.input('[red]FILE NAME: [/]')
        brute = open(filename, 'r')
        passwords = brute.readLines()

        for password in passwords:
            console.print(password, style='white')
            try:
                stream = cv2.VideoCapture(f'{PROT}:://{login}:{password}@{IP}:{PORT}/1')
            except:
                pass
            else:
                break

    while True:
        r, f = stream.read()
        cv2.imshow("IP CAMERA STREAM", f)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cv2.destroyAllWindows()


if __name__ == '__main__':
    console.print('''[red]
O88       O88          O88            O88      O88O888b.            .dO888b. 
O88   o   O88          O88            O88      O88  "Y88b          d88P  Y88b 
O88  d8b  O88          O88            O88      O88    O88          O88    O88 
O88 dO88b O88  O888b.  O88O88 .dO888b O8888b.  O88    O88  .d88b.  O88        
O88dO8888bO88     "88b O88   d88P"    O88 "88b O88    O88 d88""88b O88  O8888 
O8888P YO8888 .dO88O88 O88   O88      O88  O88 O88    O88 O88  O88 O88    O88 
O888P   YO888 O88  O88 Y88b. Y88b.    O88  O88 O88  .d88P Y88..88P Y88b  d88P 
O88P     YO88 "YO88O88  "YO88 "YO888P O88  O88 O88O888P"   "Y88P"   "YO888P88  
[/]'''.strip())
    try:
        if args.needPassword:
            withPass()
        else:
            withoutPass()
    except cv2.error:
        console.print('[x]Connection failed!', style='magenta')
    else:
        console.print('[$]Connection successfully!', style='cyan')
