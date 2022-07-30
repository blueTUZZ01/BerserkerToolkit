from rich.console import Console
from rich.panel import Panel
from rich import box
import os

console = Console()
bx = box.ASCII
mainInfo = '''
Made by: [italic cyan]blueTUZZ_01, Qurizzz, Slash-02[/]
Version: [italic cyan]1.0[/]
Languages: [italic cyan]Python, Java[/]
'''
toolList = '''
[red]{1}[/]Malwarus
[red]{2}[/]Futunus
[red]{3}[/]Petidash
'''
logo = ''' ______  _______ _______ _______ _______ _______ _       _______ _______ 
(  ___ \(  ____ (  ____ |  ____ (  ____ (  ____ ) \    /(  ____ (  ____ )
| (   ) ) (    \/ (    )| (    \/ (    \/ (    )|  \  / / (    \/ (    )|
| (__/ /| (__   | (____)| (_____| (__   | (____)|  (_/ /| (__   | (____)|
|  __ ( |  __)  |     __|_____  )  __)  |     __)   _ ( |  __)  |     __)
| (  \ \| (     | (\ (        ) | (     | (\ (  |  ( \ \| (     | (\ (   
| )___) ) (____/\ ) \ \_/\____) | (____/\ ) \ \_|  /  \ \ (____/\ ) \ \__
|/ \___/(_______//   \__|_______|_______//   \__/_/    \(_______//   \__/[green]toolkit[/]'''
console.print(f'[bold magenta]{logo}[/]')
console.print(Panel.fit(f'[bold green]{mainInfo.strip()}[/]', box=bx))
console.print(Panel.fit(f'[bold green]{toolList.strip()}[/]', box=bx))


