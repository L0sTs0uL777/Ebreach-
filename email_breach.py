import requests 
import sys 
from InquirerPy import inquirer 
from rich.panel import Panel 
from rich.console import Console 
from rich.align import Align 
import re 
import time 
import json 
import os 

os.system("clear") 

banner = Align.center(r"""                                       
         )                          )  
 (    ( /(  (      (     )       ( /(  
 )\   )\()) )(    ))\ ( /(   (   )\()) 
((_) ((_)\ (()\  /((_))(_))  )\ ((_)\  
| __|| |(_) ((_)(_)) ((_)_  ((_)| |(_) 
| _| | '_ \| '_|/ -_)/ _` |/ _| | ' \  
|___||_.__/|_|  \___|\__,_|\__| |_||_| 
                                       """) 

console = Console() 
panel = Panel(banner,title="Created by L0sTS0ul3",border_style="bold green") 

console.print(panel,style="bold red")

dis = "This tool is made  for education purpose only "

panel = Panel(dis,subtitle="Disclaimer",border_style="bold blue") 

console.print(panel,style="bold green")
print()

email = console.input("[bold cyan]Enter the target email = [/bold cyan]").strip() 

def is_email_valid(mail):
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9._%+-]+\.[a-zA-Z]{2,}$"
    return re.match(pattern,email) is not None 

run = is_email_valid(email) 

def main_code(mail):
    url = f"https://hackmyip.com/api/breach?email={mail}"
    try :
       resp = requests.get(url).json() 
    except :
       console.print("Possible Error",style="bold red") 
       console.print("1.Network Problem [Check your network]",style="bold red") 
       console.print("2.Server Not Reachable [Try after sometime ]",style="bold red") 
       return 
    if resp["data"]["services"] == [] :
        console.print("="*59,style="green") 
        console.print(Align.center("Report",style="bold red"))
        console.print("="*59,style="green") 
        console.print() 
        console.print(f"Email => {email}",style="bold blue")
        console.print() 
        console.print(f"Sucess => {resp["success"]}",style="bold blue")
        console.print()
        console.print(f"Breached => No Breach Found",style="bold blue")
        console.print()
        console.print(f"Breaches => {resp["data"]['breaches']}",style="bold blue") 
        console.print()
        console.print(f"Risk => {resp["data"]["risk"]["level"]}",style="bold blue")
        console.print()
        console.print(f"Password => {resp["data"]['passwords']}",style="bold blue") 
        console.print() 
        console.print("="*59,style="green") 
        console.print()
        console.print("="*59,style="green")
    elif resp["data"]["services"] != [] :
        console.print("="*59,style="green") 
        console.print(Align.center("Report",style="bold red")) 
        console.print("="*59,style="green") 
        console.print()
        console.print(f"Email => {email}",style="bold blue") 
        console.print()
        console.print(f"Sucess => {resp['success']}",style="bold blue") 
        console.print()
        console.print(f"Breached => Breach Found",style="bold blue") 
        console.print()
        console.print(f"Breaches => {resp["data"]['breaches']}",style="bold blue") 
        console.print()
        console.print(f"Risk => {resp["data"]["risk"]["level"]}",style="bold blue") 
        console.print()
        console.print(f"Password => {resp["data"]['passwords']}",style="bold blue") 
        console.print()
        console.print(f"Plateforms => {resp["data"]["services"]}",style="bold blue") 
        console.print() 
        console.print("="*59,style="green")
        console.print()
        console.print("="*58,style="green")
        console.print()
    confirm = inquirer.confirm("Do you want to store the data :").execute()
    console.print(confirm) 
    if confirm == True :
        if not os.path.exists("results"):
            os.mkdir("results")
        with open(f"results/{email}.json","w") as f:
            json.dump(resp,f,indent=4) 
            console.print("Data stored in result directory !")
    return 


def rprint(mess):
    for c in mess + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(8.0 / 100) 

if run == False : 
    console.print() 
    console.print("Wrong email format",style="bold red") 
else :
    #console.print("Its running")
    console.print() 
    rprint("Searching..............")
    main_code(email) 
