name = input("whats your name?")
match name:
    case "Harry"|"Ron"|"Hermione":
        print("Griffindor")
    case _:
        print("who")    
