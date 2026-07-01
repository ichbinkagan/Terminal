import os
from pathlib import Path

while True:
    CMD_Input = input(">> ").strip().split()

    if len(CMD_Input) == 0:
        continue

    command = CMD_Input[0]

    # CD
    if command == "cd":
        if len(CMD_Input) < 2:
            print("Usage: cd <folder>")
            continue

        try:
            os.chdir(CMD_Input[1])
            print("Current directory:", os.getcwd())
        except FileNotFoundError:
            print("Folder not found.")
        except Exception as e:
            print("Error:", e)

    # PWD
    elif command == "pwd":
        print(os.getcwd())

    # MKDIR
    elif command == "mkdir":
        if len(CMD_Input) < 2:
            print("Usage: mkdir <folder>")
            continue

        try:
            folder_name = " ".join(CMD_Input[1:])
            path = Path.cwd() / folder_name

            path.mkdir(parents=True, exist_ok=False)

            print("Folder created:", folder_name)

        except FileExistsError:
            print("Folder already exists.")
        except Exception as e:
            print("Error:", e)

    # LS
    elif command == "ls":
        try:
            for item in os.listdir():
                print(item)
        except Exception as e:
            print("Error:", e)

    # CLEAR
    elif command == "clear":
        os.system("cls" if os.name == "nt" else "clear")

    # EXIT
    elif command == "exit":
        print("Bye")
        break

    else:
        print("Unknown command.")