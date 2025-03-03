records = []
filename = None

while True:
    print("\nSTUDENT RECORD MANAGEMENT SYSTEM")
    print("================================================")
    print("1. Open File")
    print("2. Save File")
    print("3. Save As File")
    print("4. Show All Students Record")
    print("5. Order by Last Name")
    print("6. Order by Grade")
    print("7. Show Student Record")
    print("8. Add Record")
    print("9. Edit Record")
    print("10. Delete Record")
    print("11. Exit")
    print("================================================")

    
    choice = input("Enter choice: ")
    print("================================================")

    if choice == "1":
        filename = input("Enter filename: ")
        try:
            with open(filename, "r") as file:
                records = eval(file.read())
            print("File loaded successfully.")
        except FileNotFoundError:
            print("File does not exist.")
        except Exception:
            print("Error loading file.")
    
    elif choice == "2":
        if filename:
            with open(filename, "w") as file:
                file.write(str(records))
            print("File saved successfully.")
        else:
            print("Use 'Save As' to specify a filename first.")
    
    elif choice == "3":
        filename = input("Enter new filename: ")
        with open(filename, "w") as file:
            file.write(str(records))
        print("File saved successfully.")
    
    elif choice == "4":
        for record in records:
            print(record)
    
    elif choice == "5":
        records.sort(key=lambda x: x[1][1])
        print("Records ordered by last name.")
    
    elif choice == "6":
        records.sort(key=lambda x: (0.6 * x[2] + 0.4 * x[3]), reverse=True) 
        print("Records ordered by grade.")
    
    elif choice == "7":
        id = input("Enter Student ID: ")
        for record in records:
            if record[0] == id:
                print(record)
                break
        else:
            print("Record not found.")
    
    elif choice == "8":
        id = input("Enter Student ID (6 digits): ")
        first_name = input("Enter First Name: ")
        last_name = input("Enter Last Name: ")
        standing = float(input("Enter Class Standing Grade: "))
        major_exam = float(input("Enter Major Exam Grade: "))
        records.append((id, (first_name, last_name), standing, major_exam))
        print("Record added successfully.")
    
    elif choice == "9":
        id = input("Enter Student ID to edit: ")
        for i in range(len(records)):
            if records[i][0] == id:
                first_name = input("Enter New First Name: ")
                last_name = input("Enter New Last Name: ")
                standing = float(input("Enter New Class Standing Grade: "))
                major_exam = float(input("Enter New Major Exam Grade: "))
                records[i] = (id, (first_name, last_name), standing, major_exam)
                print("Record updated successfully.")
                break
        else:
            print("Record not found.")
    
    elif choice == "10":
        id = input("Enter Student ID to delete: ")
        for i in range(len(records)):
            if records[i][0] == id:
                del records[i]
                print("Record deleted successfully.")
                break
        else:
            print("Record not found.")
    elif choice == "11":
        print("Exiting...")
        break
    
    else:
        print("Error Try Again.")
