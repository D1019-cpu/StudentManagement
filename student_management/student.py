import student_management.data as d 


def add_student():
    """Add Student Function"""
    print('-'*40)
    print("Add Student".center(40, '-'))

    # struct of the student
    infor = {
        'id': '',
        'name': '',
        'age': '',
        'gender': '',
        'address': '',
        'CPA': ''
    }

    id = input("Enter ID of the student: ")
    while True:
        student = find_student(id)
        if student != False:
            id = input("ID already exist, Please re-enter: ")
        else:
            break
    
    infor['id'] = id

    # Name, age, gender, address, CPA
    infor['name'] = input("Enter name of the student: ") 
    infor['age'] = input("Enter age of the student: ")
    infor['gender'] = input("Enter gender of the student: ")
    infor['address'] = input("Enter address of the student: ")
    infor['CPA'] = input("Enter CPA of the student: ")       

    # adding data
    d.list_students.append(infor)
    
def find_student(id):
    """Find Student Function"""
    for index, item in enumerate(d.list_students):
        if d.list_students[index]['id'] == 'id':
            # if id match return index and data
            return [index,item]
    return False


def show_students():
    """Show List Students Function"""
    print('-'*40)
    for i in d.list_students:
        print(f"{i['id']:4} {i['name']:25} {i['age']:4} {i['gender']:7} {i['address']:15} {i['CPA']:8}")


def edit_student():
    """Edit Student Function"""
    print("-"*40)
    id = input("Enter ID of the student: ")
    student = find_student(id)
    if student != False:
        # return [index,item]
        # Edit Name, age, gender, address, CPA
        student[1]['name'] = input("Enter name of the student: ") 
        student[1]['age'] = input("Enter age of the student: ")
        student[1]['gender'] = input("Enter gender of the student: ")
        student[1]['address'] = input("Enter address of the student: ")
        student[1]['CPA'] = input("Enter CPA of the student: ") 
        d.list_students[student[0]] = student[1]
    else:
        print("ID of the student does not exist!!!")


def delete_student():
    """Delete Student Function"""
    print('-'*40)
    id = input("Enter ID of the student: ")
    student = find_student(id)
    if student != False:
        d.list_students.remove(student[1])
        print("Delete Student Successfully!")
    else:
        print("Deleted candidate could not be located.")