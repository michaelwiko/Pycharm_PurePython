import string
def count_letters(text):
    count=0
    for charater in text:
        if character.lower() in string.ascii_letters:
            count += 1
    return count

