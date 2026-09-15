def setiings():
    while True:
        print("Type a number to select")
        print("1. General")
        print("2. Protocol")
        print("3. Theme")
        print("4. exit")

        while True:
            try:
                choice = int(input("Type a choice > "))
                break
            except:
                print("Choose between 1,2,3,4")
                continue

        if choice == 1:
            print("1. Change User Name")
            print("2. Confirm Before Closing application")
            print()
        elif choice == 2:
            pass
        elif choice == 3:
            pass
        elif choice == 4:
            break
        else:
            continue
