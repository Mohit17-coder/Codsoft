tasks = []

def addtask():
    task = input("Enter the task:")
    tasks.append(task)
    print(f"Task '{task}'added to the list.")

def show():
    if not tasks:
        print("There are no tasks currently.")
        return 0
    else:
        print("Current Tasks:")
        for i, task in enumerate(tasks):
            print(f"Task #{i+1}. {task}")


def deletetask():
        td = show()
        if td!=0:
            try:
                done = int(input("Enter the task # to delete:")) - 1
                if done < len(tasks):
                    tasks.pop(done)
                    print(f"Task '{done+1}' has been marked as done.")

                else:
                    print("Invalid Task Number!!!!")   
                
            except:
                print("Invalid input.") 
    
        

if __name__ == "__main__":
    print("Welcome!!!! \nCreate your own To Do List----")
    while True:
        print("Please Select one of the following options :")
        print("----------------------------------------------------------")
        print("1. Add a new task:")
        print("2. Mark the task as done:")
        print("3. Check your List:")
        print("4. Exit")

        choice = input("Enter your choice:")

        if( choice == "1"):
            n = int(input("Enter the number tasks you want to add:- "))
            for i in range(0,n):
                addtask()
        elif(choice == "2"):
            deletetask()
        elif( choice == "3"):
            show()
        elif(choice == "4"):
            break  
        else:
            print("ERROR!!! Please enter a suitable choice.")