alp = input("Enter alphabet: ")
match alp:
    case "a"|"e"|"i"|"u":
        print("Vowel")
    case _:
        print("Constant")
