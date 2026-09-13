from help import help

while True:
    command = input("> ")

    if command == "help":
        print(help())
    