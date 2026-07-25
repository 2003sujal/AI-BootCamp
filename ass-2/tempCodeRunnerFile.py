
    print("2. Remove Book")
    print("3. Search Book")
    print("4. Display Books")
    print("5. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        lib.add_book()

    elif choice == "2":
        lib.remove_book()

    elif choice == "3":
        lib.search_book()

    elif choice == "4":
        lib.display_books()

    elif choice == "5":
        print("Thank You!")
        break

    else:
        print("Invalid Choice")k