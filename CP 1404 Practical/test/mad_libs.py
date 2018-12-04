prince = input("Enter a name (Male) : ")
lady = input("Enter a name (Female) : ")
positive_prince = input("Enter a positive adjective : ")
negative_lady = input("Enter a negative adjective : ")
positive_lady = input("Enter a positive adjective again : ")
negative_prince = input("Enter a negative adjective again : ")
negative_prince2 = input("Enter a negative adjective again (pls be more harsh) : ")
family_mmbr = input("Enter a family member : ")

print("\n")
print("Once upon a time, there's a young prince named " + prince + ".")
print("He was " + positive_prince.lower() + " but he's very " + negative_prince.lower())
print("Then one day, He met a young " + positive_lady.lower() + " lady named " + lady + ".")
print("Unfortunately, she doesn't like prince " + prince + " because he is very " + negative_prince.lower() +".")
print("Lady " + lady + " didn't even notice that prince " + prince + " is also really " + positive_prince.lower() + ". (Even though the lady is " + negative_lady.lower() + " as hell.)")
print("Maybe she didn't care about how " + positive_prince.lower() + " he is, because her " + family_mmbr.lower() + " said :\n\"You have to avoid " + negative_prince.lower() + " people like him. Btw he's also "+ negative_prince2.lower() + ".\"")


input()
