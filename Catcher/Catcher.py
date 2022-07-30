from rich.console import Console
from twoip import TwoIP
from getpass import getpass
from os import system
import socket



console = Console()
logo = '''[green]  ______     ___   .___________.  ______  __    __   _______ .______      
 /      |   /   \  |           | /      ||  |  |  | |   ____||   _  \     
|  ,----'  /  ^  \ `---|  |----`|  ,----'|  |__|  | |  |__   |  |_)  |    
|  |      /  /_\  \    |  |     |  |     |   __   | |   __|  |      /     
|  `----./  _____  \   |  |     |  `----.|  |  |  | |  |____ |  |\  \----.
 \______/__/     \__\  |__|      \______||__|  |__| |_______|| _| `._____|[/]'''

def getIpData(ip):
    twoip = TwoIP(key = None)
    data = twoip.geo(ip)
    return data

def connection():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, proto=0)
    sock.bind(('', 80))
    sock.listen()
    conn, addr = sock.accept()
    geo = getIpData(addr[0])
    console.print(f'''
|[red]IP:[/] [cyan]{geo["ip"]}[/]|
|[red]COUNTRY CODE:[/] [cyan]{geo["country_code"]}[/]|
|[red]COUNTRY:[/] [cyan]{geo["country"]}[/]|
|[red]REGION:[/] [cyan]{geo["region"]}[/]|
|[red]CITY:[/] [cyan]{geo["city"]}[/]|
|[red]ZIP CODE:[/] [cyan]{geo["zip_code"]}[/]|
        '''.strip(), style='green')


system("cls")
console.print("FOR CORRECT CONNECTION START NGROK (ngrok http 80) \n(PRESS ENTER TO START)", style='red')
getpass(prompt='', stream=None)
system("cls")
console.print(logo)
choose = console.input("[white]START SERVER? (Y\\N)[/]\n>")
while True:
    if choose.lower() == "y":
        try:
            connection()
            break
        except RuntimeError:
            console.print("PLEASE, TRY LATER", style='red')
            break
    elif choose.lower() == 'n'():
        break
    else:
        console.print("INCORRECT", style='red')
        break



