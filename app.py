from help import help

while True:
    command = input("> ").lower()

    if command == "help":
        print(help())

    if command == "exit":
        exit()

    print("Unknown Command")