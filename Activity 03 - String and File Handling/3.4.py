try:
    with open("students.txt", "r") as file:
        contents = file.read()
        
        if not contents.strip():
            print("No students in the file.")
        else:
            print("Student Information:\n")
            print(contents)
except FileNotFoundError:
    print("The file does not exist.")
