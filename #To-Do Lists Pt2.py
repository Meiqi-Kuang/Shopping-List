#To-Do Lists Pt2 

Shoppinglist = ["Orange", "Apple"]
#Adds items to shopping list
def add():
    x = input("What would you like to add?")
    Shoppinglist.append(x)
    print(Shoppinglist)
#Views items in shopping list
def View():
    print(Shoppinglist)
#Crosses out item on shopping list
def Mark():
    z = input("What would you like to mark?")
    y = Shoppinglist.index(z)
    Shoppinglist[y] = (z + " ✓")
#Removes items on shopping list
def Remove():
    a = input("What would you like to remove?")
    Shoppinglist.remove(a)
    print(Shoppinglist)
#Exits shopping list
def Exit():
    quit()
#Clears all items from the list
def Clear():
    Shoppinglist.clear()
#Print the number of items in list
def Print():
    print(len(Shoppinglist))
#Prints the number of Items on the list
def Sort():
    Shoppinglist.sort()
    print(Shoppinglist)



def Shop():
    while True:

        print("1.Add Item \n2.View List \n3.Mark Item \n4.Remove Item \n5.Clear \n6.Print \n7.Sort \n8.Exit")
        c = input("Choose Option:")
        if c == "8":
            quit()
        if c == "1":
            add()
        if c == "2":
            View()
        if c == "3":
            Mark()
        if c == "4":
            Remove()
        if c == "5":
            Clear()
        if c == "6":
            Print()
        if c == "7":
            Sort()

Shop()