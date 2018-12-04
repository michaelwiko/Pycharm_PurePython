def name(name):
    name = input("Please enter your name : ")
    print("Hi " + name + "!" + " Welcome back.")
    return name

def menu():
    print("|--------------------------------------|")
    print("| Songs to Learn 1.0 - by Michael Wiko |")
    print("|--------------------------------------|")
    print("0 songs are loaded...")
    print("Menu:\nL - List of Songs\nA - Add new song\nC - Complete a song\nQ - Quit this program")
    entry = input(">>> ")
    while entry not in ('L', 'l', 'A', 'a', 'C', 'c', 'Q', 'q'):
        print("Invalid input")
        entry = input(">>> ")
    if entry == "L" or entry == "l" :
        print("{}.{} {:35} -  {:32} ({:4})".format(0, "*", "Heartbreak Hotel", "Elvis Presley", 1956))
        print("{}.{} {:35} -  {:32} ({:4})".format(1, " ", "Somebody That I Used to Know", "Gotye featuring Kimbra", 2012))
        print("{}.{} {:35} -  {:32} ({:4})".format(2, "*", "Macarena", "Los Del Rio", 1996))
        print("{}.{} {:35} -  {:32} ({:4})".format(3, "*", "I Want To Hold Your Hand", "The Beatles", 1964))
        print("{}.{} {:35} -  {:32} ({:4})".format(4, " ", "Boom Boom Pow", "The Black Eyed Peas", 2009))
        print("{}.{} {:35} -  {:32} ({:4})".format(5, "*", "My Sharona", "The Knack", 1979))
    elif entry == "A" or entry == "a" :
        print("Can't add anything.")
    elif entry == "C" or entry == "c" :
        print("How do you complete without a song?")
    elif entry == "Q" or entry == "q" :
        print("Bye " + main_name + " ! See you soon.")


main_name = name(name)
menu()