tasks = []

while True:
    print("1-Qoshish")
    print("2-Korish")
    print("3-Chiqish")

    choice = input("Tanlang: ")

    if choice == "1":
        task = input("Vazifa: ")
        tasks.append(task)

    elif choice == "2":
        for task in tasks:
            print(task)

    elif choice == "3":
        break

    else:
        print("Xato buyruq")

print("Dastur tugadi")
