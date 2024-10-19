"""¨
projekt_1.py: první projekt do Engeto Online Python Akademie
author: Monika Jedličková
email.mcmilica@centrum.cz
discord: monika_64143
"""
link = "-" * 39
registered = {
"bob" : "123",
"ann" : "pass123",
"mike" : "password123",
"liz" : "pass123"
}
username = input("Enter username:")
password = input("Enter password:")
if username in registered.keys() and registered.get(username) == password:
    print(f"user:", username)
    print(f"password:", password)
    print(link)
    print(f"Welcome to the app,", username)
    print("We have 3 texts to be analyzed.")
    print(link)
    TEXTS = ['''
    Situated about 10 miles west of Kemmerer,
    Fossil Butte is a ruggedly impressive
    topographic feature that rises sharply
    some 1000 feet above Twin Creek Valley
    to an elevation of more than 7500 feet
    above sea level. The butte is located just
    north of US 30N and the Union Pacific Railroad,
    which traverse the valley. ''',
    '''At the base of Fossil Butte are the bright
    red, purple, yellow and gray beds of the Wasatch
    Formation. Eroded portions of these horizontal
    beds slope gradually upward from the valley floor
    and steepen abruptly. Overlying them and extending
    to the top of the butte are the much steeper
    buff-to-white beds of the Green River Formation,
    which are about 300 feet thick.''',
    '''The monument contains 8198 acres and protects
    a portion of the largest deposit of freshwater fish
    fossils in the world. The richest fossil fish deposits
    are found in multiple limestone layers, which lie some
    100 feet below the top of the butte. The fossils
    represent several varieties of perch, as well as
    other freshwater genera and herring similar to those
    in modern oceans. Other fish such as paddlefish,
    garpike and stingray are also present.'''
    ]
    text = ""
    no_text = input("Enter a number of the text:")
    print("Enter a number btw 1 and 3 to select:", no_text)
    print(link)
    if no_text.isdigit():
        no_text = int(no_text)
        if no_text == 1 or no_text == 2 or no_text == 3:
            text = (TEXTS[no_text - 1])
            rt = text.replace(",\n", "").replace("\n", "").replace(".","").replace(",", "")
            words = rt.split(" ")
            replaced_text = []
            for word in words:
                if len(word):
                    replaced_text.append(word)
            number_words = len(replaced_text)
            print(f"There are", number_words, "words in the selected text.")
            sum_title_word = 0
            sum_uppercase = 0
            sum_lowercase = 0
            sum_digit = 0
            all_digit = []
            sum_all_digit = 0
            for word in replaced_text:
                if word[0].isupper():
                    sum_title_word += 1
                elif word.isupper():
                    sum_uppercase += 1
                elif word.islower():
                    sum_lowercase += 1
                elif word.isdigit():
                    sum_digit += 1
                    all_digit.append(word)
                    sum_all_digit += int(word)     
            print(f"There are", sum_title_word, "titlecase words.")
            print(f"There are", sum_uppercase, "uppercase words.")
            print(f"There are", sum_lowercase, "lowercase words.")
            print(f"There are", sum_digit, "numeric strings.")
            print(f"The sum of all the numbers", sum_all_digit)
            print(link)
            print("len  | occurences".upper(), " " * 15, "| nr.".upper())
            print(link)
            occurence = {}
            for word in replaced_text:
                len_w = len(word)
                if  len_w in occurence:
                    occurence[len_w] += 1
                else:
                    occurence[len_w] = 1
            sorted_len = dict(sorted(occurence.items()))
            for len_w, cnt_w in sorted_len.items():
                print(len_w, " " * (3 - len(str(len_w))),
                "|", "*" * cnt_w, " " * (25 - cnt_w), "|", cnt_w)
        elif no_text > len(TEXTS):
            print("Number out of the text, terminating the program..")
    else:
        print("Input is not the number, terminating the program..")
else:
    print("Unregistered user, terminating the program..")