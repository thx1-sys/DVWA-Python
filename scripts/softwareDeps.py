import subprocess
import re

def run_sqlmap(url):
    command = f"sqlmap -u {url} --dbs"
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    output = ""
    while True:
        line = process.stdout.readline()
        if line == b'' and process.poll() is not None:
            break
        if line:
            output += line.decode()

    # Extract database names
    databases = re.findall(r"\[\*\] (.+)", output)
    for db in databases:
        print(db)

    rc = process.poll()
    return rc

# Use the function
run_sqlmap("../SQLmap/req4.txt")