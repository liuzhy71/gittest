#file object=open()
to_do_list=["Take a break","Go back to home","Go to a lecture"];
option_list={"Insert a new task":1,"Remove a task (by typing its content)":2,"Show all existing tasks":3,"close the program":4};

print("Insert the number correspending to the action you want to perform:");
for (things,order) in option_list.items():
    print("({}){}".format(order,things));
print("Your choice:");
option=int(input());

while option!=0:
    if option==1:
        print("Insert a new task.\nPlease type the task:");
        newtask=input();
        to_do_list.append(newtask);
        print("Now the new list:");
        i = 1;
        for things in to_do_list:
            print('(' + str(i) + ')' + things)
            i += 1;
    elif option==2:
        print("Remove a task (by typing its content).\nPlease type the task:");
        deltask=input();
        to_do_list.remove(deltask);
        print("Now the new list:\n");
        i = 1;
        for things in to_do_list:
            print('(' + str(i) + ')' + things)
            i += 1;
    elif option==3:
        print("Show all existing tasks.");
        i=1;
        for things in to_do_list:
            print('(' + str(i) + ')' + things)
            i += 1;
    else:
        print("Wrong input!");
    print("Press Enter to continue");
    input();
    import os
    n=os.system('cls')
    print("Insert the number correspending to the action you want to perform:\n");
    for (things, order) in option_list.items():
        print("({}){}".format(order, things));
    print("Your choice:");
    option = int(input());

