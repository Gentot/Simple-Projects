#global variable
mylist=[]

def view_task_to_delete():
    for i in range(len(mylist)):
        print(f"{i+1}. {mylist[i]}")
def view_task():
    if len(mylist)==0:
        print("No tasks available")
        home=str(input("Back to homepage? (y/n)"))
        if home.lower()=='y':
            return 
        else:
            view_task()
    else:
        for i in range(len(mylist)):
            print(f"{i+1}. {mylist[i]}")

        home=str(input("Back to homepage? (y/n)"))
        if home.lower()=='y':
            return
        else:
            view_task()


def add_task():
    task = str(input("Enter a task: "))
    while True:
        add_notes= input("Do you wanna add some notes? (y/n)").lower()
        if add_notes in ('y','n'):
            notes=str(input("Enter your notes: ")) if add_notes=='y' else '' 
            mylist.append({task:notes})
            break
        else:
            print("Invalid input (y/n)")

def remove_task():
    view_task_to_delete()
    while True:
        task_to_remove = int(input("Enter the number you wanna remove: "))
        if task_to_remove >= 1 and task_to_remove <= len(mylist):
            del mylist[task_to_remove-1]
            break
        else:
            print("Invalid input (number out of range)")
        
def to_do_list():
    while True:
        print("To Do List Menu:\n ")
        print(" 1. View Task \n 2. Add a Task \n 3. Remove a Task\n 4. Exit \n")
        choice = input("Enter your choice: ")
        if choice == "1":
            view_task()
        elif choice== "2":
            add_task()
        elif choice == "3":
            remove_task()
        elif choice == "4":
            print("Exiting the program")
            return
        else:
            print("Invalid choice. Please choose a valid option.")


to_do_list()