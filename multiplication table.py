#define function called multiplication table
def muliplication_table ():
    #input number and number of row
    number = int(input("Enter column / main number: "))
    number_row = int(input("Enter row / number that (has / have) to times: "))

    #for loop with range number_row
    for i in range (1, number_row + 1):
        print (number, "*", i, "=", number * i)
    
    #input continue or not
    continue_choice = input("Do you want to coninue? (y/n)\n")

    #if statement decide that want to continue or not
    if continue_choice == "y":
        muliplication_table()
    elif continue_choice == "n":
        print ("Good Bye!")
    else:
        print ("Error!")

#print This program can display multiplication table / Describe program plan
print ("This program can display multiplication table")

#called multiplication_table funcion
muliplication_table()