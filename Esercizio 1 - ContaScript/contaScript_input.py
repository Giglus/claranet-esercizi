import os
from collections import defaultdict

def contaScript(directory):
    interpreter_count = defaultdict(int)

    for root, dirs, files in os.walk(directory):
        for filename in files:
            if filename.endswith(".sh"):
                filepath = os.path.join(root, filename)
                with open(filepath, "r") as file:
                    first_line = file.readline().strip()
                    if first_line.startswith("#!"):
                        interpreter_count[first_line] += 1

    for interpreter, count in interpreter_count.items():
        print(f"{count} {interpreter}")

user_directory = input("Inserisci il PATH di una directory: ")
contaScript(user_directory)
