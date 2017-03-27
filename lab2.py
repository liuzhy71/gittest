from sys import argv

#file object=open();
to_do_list=["Take a break","Go back to home","Go to a lecture"];
option_list={"Insert a new task":1,"Remove a task (by typing its content)":2,"Show all existing tasks":3,"Remove a task by keywords":4,"Close the program":5};

def insert(to_do_list):
    print("Insert a new task.\nPlease type the task:");
    newtask = input();
    to_do_list.append(newtask);
    print("Now the new list:");
    i = 1;
    for things in to_do_list:
        print('(' + str(i) + ')' + things)
        i += 1;

def remove(to_do_list):
    print("Remove a task (by typing its content).\nPlease type the task:");
    deltask = input();
    to_do_list.remove(deltask);
    print("Now the new list:");
    i = 1;
    for things in to_do_list:
        print('(' + str(i) + ')' + things)
        i += 1;

def show(to_do_list):
    print("Show all existing tasks.");
    if (len(to_do_list)==0):
        print('The list is empty')
    else:
        temp_to_do_list=to_do_list[:]
        temp_to_do_list.sort()
        i = 1;
        for things in temp_to_do_list:
            print('(' + str(i) + ')' + things)
            i += 1

def remove_multiple_tasks(tasks_list):
    remove_list = []
    substring = input("Type the keywords to remove the task:\n")
    for single_task in tasks_list:
        if (substring in single_task):
            remove_list.append(single_task)
    if (len(remove_list)>0):
        for task_to_remove in remove_list:
            if (task_to_remove in tasks_list):
                tasks_list.remove(task_to_remove)
                print("The element "+task_to_remove+" was successfully removed")
    else:
        print("We did not find any tasks to delete!")

if __name__=='__main__':

    filename=''
    if (len(argv)>1):
        filename=argv[1]
        try:
            txt=open(filename)
            to_do_list=txt.read().splitlines()
            txt.close()
        except IOError:
            print("File not found! Use empty list instead.")

    print("Insert the number correspending to the action you want to perform:");
    for (things,order) in option_list.items():
        print("({}){}".format(order,things));
    string=input("Your choice:\n")
    while string.isdigit() != True:
        # if the string is not a number we will ask a new input
        string = input("Wrong input! Your choice:\n")
    option=int(string)

    while option!=5:
        if option==1:
            insert(to_do_list)
        elif option==2:
            remove(to_do_list)
        elif option==3:
           show(to_do_list)
        elif option == 4:
            remove_multiple_tasks(to_do_list)
        else:
            print("Wrong input!");
        print("Press Enter to continue");
        input();
        import os
        n=os.system('cls')
        print("Insert the number correspending to the action you want to perform:\n");
        for (things, order) in option_list.items():
            print("({}){}".format(order, things));
        string = input("Your choice:\n")
        while string.isdigit() != True:
            # if the string is not a number we will ask a new input
            string = input("Wrong input! Your choice:\n")
        option = int(string)

    if (filename!=""):
        try:
            txt = open(filename,'w')
            for single_task in to_do_list:
                txt.write(single_task+'\n')
            txt.close()
        except IOError:
            print('Problems in saving to do list.')
