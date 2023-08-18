import student_management.student as s


action = 0
while action >= 0:
    print("Choose action")
    print("Enter 1: Add Student")
    print("Enter 2: Delete Student")
    print("Enter 3: Edit Student")
    print("Enter 4: Show List Students")
    print("Enter 0: Exit")

    try: 
        action = int(input(":"))
    except ValueError:
        raise ValueError("Please Enter A Number... Shut Down Program...")

    if action == 1:
        s.add_student()
    elif action == 2:
        s.delete_student()
    elif action == 3:
        s.edit_student()
    elif action == 4:
        s.show_students()
    else:
        print("Action out of range, please choose again!")
        
    if action == 0: break
