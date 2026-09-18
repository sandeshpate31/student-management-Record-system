from record_service import (
    add_record,
    view_records,
    search_record,
    update_record,
    delete_record
)


def display_menu():
    print("\n==============================")
    print(" STUDENT RECORD MANAGEMENT")
    print("==============================")
    print("1. Add Record")
    print("2. View Records")
    print("3. Search Record")
    print("4. Update Record")
    print("5. Delete Record")
    print("6. Exit")
    print("==============================")


def main():
    while True:
        display_menu()

        choice = input("Enter your choice: ")

        if choice == "1":
            add_record()

        elif choice == "2":
            view_records()

        elif choice == "3":
            search_record()

        elif choice == "4":
            update_record()

        elif choice == "5":
            delete_record()

        elif choice == "6":
            print("Thank you for using the application.")
            break

        else:
            print("Invalid choice. Please select 1-6.")


if __name__ == "__main__":
    main()