def count_char():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        words = file_contents.split()
        print(f"{len(words)} words found in the document")

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        print(file_contents)

each_char = {}
def count_each_char():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        words = file_contents.split()
        for character in file_contents:
            lower_character = character.lower()
            if lower_character in each_char:
                each_char[lower_character] += 1
            else:
                each_char[lower_character] = 1
        for char in each_char:
            if char.isalpha():
                print(f"The '{char}' character was found {each_char[char]} times")

count_char()
print("")
count_each_char()