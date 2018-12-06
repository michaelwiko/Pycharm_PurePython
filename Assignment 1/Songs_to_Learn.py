import csv

def name(name):
    name = input("Please enter your name : ")
    print("Hi " + name + "!" + " Welcome back.")
    return name

def menu():
    data = new_song + learned_song
    data.sort()
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
        print("List of songs ( * = new songs ):")
        song_list(data, new_song, learned_song)
    elif entry == "A" or entry == "a" :
        print("Can't add anything.")
    elif entry == "C" or entry == "c" :
        print("How do you complete without a song?")
    elif entry == "Q" or entry == "q" :
        print("Bye " + main_name + " ! See you soon.")

def become_list():
    input_file = open("songs.csv", "r")
    number = 0
    for line in input_file:
        song=line.strip().split(",")
        if song[3] == "n":
            song = [number, song[0], song[1], song[2]]
            new_song.append(song)
        elif song[3] == "y":
            song = [number, song[0], song[1], song[2]]
            learned_song.append(song)
        number += 1
    input_file.close()
    print("{} items loaded from songs.csv".format(len(new_song + learned_song)))

def song_list(data, new_song, learned_song):
    for each in data:
        if each in new_song:
            print("{}.{} {:35} -  {:32} ({:4})".format(char[0], "*", char[1], char[2], char[3]))
        elif each in learned_song:
            print("{}.{} {:35} -  {:32} ({:4})".format(char[0], " ", char[1], char[2], char[3]))



new_song = []
learned_song = []
data = []
main_name = name(name)
menu()