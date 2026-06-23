day = 7
match day:
    case 1|2|3|4|5:
        print("Weekdays")
    case 6|7:
        print("Weekends")
    case _:
        print("Invalid Input")