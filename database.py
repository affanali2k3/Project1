
def list_maker():
    global list_of_students, list_of_rollno, list_of_faculty
    list_of_students = []
    list_of_rollno = []
    list_of_faculty = []
def store():
    global student_name, student_roll, student_faculty
    index_store = int(input("Which student`s data do you want to store\n"))
    student_name = str(input("Input student`s name\n"))
    student_roll = int(input("Input student`s roll.no\n"))
    student_faculty = str(input("Input student`s faculty\n"))

    f = open("record.txt", "a")
    # f.write(f"index_store,"Name: ", student_name, "| roll.no: ", student_roll, "| Faculty: ", student_faculty")
    f.write(f"{index_store}. Name: {student_name} | roll.no: {student_roll} | Faculty: {student_faculty}\n")
    # f.close()
    # list_of_students.insert(index_store - 1, student_name)
   
    # list_of_rollno.insert(index_store - 1, student_roll)
  
    # list_of_faculty.insert(index_store -1, student_faculty)


def show():
    index_show = int(input("Which students data do you want to see\n"))
    # print("Name is ", list_of_students[index_show - 1])
    # print("Faculty is ", list_of_faculty[index_show - 1])
    # print("Roll no. is ", list_of_rollno[index_show - 1])
    f = open("record.txt", "r")
    lines = f.readlines()
    print(lines[index_show-1])
    f.close()

def show_all():
    # for i in range(len(list_of_students)):
    #     print(f"Name of student {i+1} is {list_of_students[i]}")
    #     print(f"Faculty of student {i+1} is {list_of_faculty[i]} ")
    #     print(f"Roll no. of student {i+1} is {list_of_rollno[i]}\n")
    f = open("record.txt", "r")
    lines = f.readlines()
    for i in range(len(lines)):
        print(lines[i])
    f.close()
run_once = 0
show_up = 0
while True:
    if run_once == 0:
        list_maker()
    run_once += 1
    if show_up == 0:   
        choice_show = input("Do you want to contine?  Y/N  \n")

        if choice_show.upper() =="N":
            break
        elif choice_show.upper() == "Y":
            choice = input("Do you want to store or see\n")
            if choice == "store":
                store()
            elif choice == "see":
                choice_store = input("Do you want to see all data?  Y/N \n")
                if choice_store.upper() == "Y":
                    show_all()
                elif choice_store.upper() == "N":
                    show()
            else:
                print("Please select one of these\n")
            
        




