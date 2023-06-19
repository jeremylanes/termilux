import os
import socket
import subprocess

while True:
    command = input(f'[lane@{socket.gethostname()}]-[{os.getcwd()}]-$ ')
    if command == 'exit':
        break

    command_split = command.split(' ')
    if command_split[0] == 'cd' and len(command_split) == 2:
        try:
            os.chdir(command_split[1])
        except FileNotFoundError:
            print(f"No such file or directory: '{command_split[1]}")
    else:
        result = subprocess.run(command, shell=True, capture_output=True, universal_newlines=True)
        print(f'{result.stdout} {result.stderr}')

# ******************** Auteur ********************
# ----------------- Jeremy Lane -----------------

# ******************************* Porfolio *******************************
# ----------------- https://jeremylane.pythonanywhere.com/ -----------------
