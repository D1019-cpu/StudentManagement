def isEmpty(s):
    return len(s) == 0


def isBlank(s):
    return len(s.strip()) == 0


# test isEmpty và isBlank
# s1 = ""
# s2 = "                   "
# print(isEmpty(s1))
# print(isBlank(s2))
# print(isBlank(s1))


def retrieve_data(filename):
    data = []
    try:
        with open(file=filename, mode='r', encoding='utf-8') as f:
            data = f.read()
    except IOError as e:
        print("Error Code:", e)
    return list(data)


def save_data(filename, data):
    data = str(data)
    try:
        with open(file=filename, mode='w', encoding='utf-8') as f:
            f.write(data)
            print("Save data successfully!!!")
    except IOError as e:
        print("Error Code:", e)


list_students = retrieve_data("data.txt")


def add_student():
    """Add Student Function"""
    print('-'*80)
    print("|", "Add Student".center(76, ' '), "|",sep=' ')
    
    # struct of the student
    infor = {
        'id': '',
        'name': '',
        'age': '',
        'gender': '',
        'address': '',
        'CPA': ''
    }

    print("|Enter ID of the student: ".ljust(78, ' '), "|", sep=' ')

    id = input("|ID: ")
    while not id.isdigit() or isBlank(id):
        id = input("|ID: ")
    
    while True:
        student = find_student(id)
        if student != False:
            id = input("|ID already exist, Please re-enter: ")
        else:
            break
    
    infor['id'] = id

    # Name, age, gender, address, CPA
    while True:
        print("|Enter name of the student: ".ljust(78, ' '), "|", sep=' ')
        infor['name'] = input("|Name: ")
        print("|Enter age of the student: ".ljust(78, ' '), "|", sep=' ') 
        infor['age'] = input("|Age: ")
        print("|Enter gender of the student: ".ljust(78, ' '), "|", sep=' ')
        infor['gender'] = input("|Gender: ")
        print("|Enter address of the student: ".ljust(78, ' '), "|", sep=' ')
        infor['address'] = input("|Address: ")
        print("|Enter CPA of the student: ".ljust(78, ' '), "|", sep=' ')
        infor['CPA'] = input("|CPA: ")   
        if all(infor.values()): break
        else:
            print("Fields must have values.")

    # adding data
    list_students.append(infor)
    save_data("data.txt", list_students)

    print("|", "Adding Student Successfully!".center(76, ' '), "|", sep=' ')
    print('-'*80)


def find_student(id):
    """Find Student Function"""
    for index, item in enumerate(list_students):
        if list_students[index]['id'] == id:
            # if id match return index and data
            return [index,item]
    return False


def show_students():
    list_students = retrieve_data("data.txt")
    print(list_students)
    print(type(list_students))
    """Show List Students Function"""
    print('-'*80)
    print("|", "List Students".center(76, ' '), "|", sep=' ')
    for i in list_students:
        print(f"| {i['id']:4} | {i['name']:25} | {i['age']:4} | {i['gender']:7} | {i['address']:13} | {i['CPA']:8} |")
    print('-'*80)


def edit_student():
    """Edit Student Function"""
    print("-"*80)
    print("|", "Edit Student".center(76, ' '), "|", sep=' ')

    print("|Enter ID of the student: ".ljust(78, ' '), "|", sep=' ') 

    id = input("|ID: ")
    while not id.isdigit() or isBlank(id):
        id = input("|ID: ")

    student = find_student(id)
    # print(student)
    if student != False:
        # return [index,item]
        # Edit Name, age, gender, address, CPA
        while True:
            print("|Enter name of the student: ".ljust(78, ' '), "|", sep=' ')
            student[1]['name'] = input("|Name: ") 

            print("|Enter age of the student: ".ljust(78, ' '), "|", sep=' ')
            student[1]['age'] = input("|Age: ")
            
            print("|Enter gender of the student: ".ljust(78, ' '), "|", sep=' ')
            student[1]['gender'] = input("|Gender: ")

            print("|Enter address of the student: ".ljust(78, ' '), "|", sep=' ')
            student[1]['address'] = input("|Address: ")
            
            print("|Enter CPA of the student: ".ljust(78, ' '), "|", sep=' ')
            student[1]['CPA'] = input("|CPA: ") 

            if all(student[1].values()): break
            else:
                print("Fields must have values.")
        
        list_students[student[0]] = student[1]
        save_data("data.txt",list_students)
    else:
        print("|", "ID of the student does not exist!!!".center(76, ' '), "|", sep=' ')
    print("-"*80)


def delete_student():
    """Delete Student Function"""
    print("-"*80)
    print("|", "Delete Student".center(76, ' '), "|", sep=' ')
    print("|Enter ID of the student: ".ljust(78, ' '), "|", sep=' ')

    id = input("|ID: ")
    while not id.isdigit() or isBlank(id):
        id = input("|ID: ")

    student = find_student(id)
    if student != False:
        list_students.remove(student[1])
        save_data("data.txt",list_students)
        print("|", "Delete Student Successfully!".center(76, ' '), "|", sep=' ')
    else:
        print("|", "Deleted candidate could not be located.".center(76, ' '), "|", sep=' ')
    print("-"*80)
   