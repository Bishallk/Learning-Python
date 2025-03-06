
#-----------Match Satatement--------|

#* The match statement in Python is part of structural pattern matching, introduced in Python 3.10. It provides a more powerful and flexible way to handle conditional logic, similar to switch/case statements in other languages.

def choose_day():
    
    day=int(input("Enter a number from 1 to 7: "))
    match(day):
        case 1:
            print("Sunday")
            choose_another()       
        case 2:
            print("Monday")
            choose_another()
        case 3:
            print("Monday")
            choose_another()
        case 4:
            print("Tuesday")
            choose_another()
        case 5:
            print("Thrusday")
            choose_another()
        case 6:
            print("Friday")
            choose_another()
        case 7:
            print("Saturday")
            choose_another()
        case _:
            print("Please Choose Number from 1 to 7")
            choose_day()

def choose_another():
    cont=input("Want to choose another day (y/n): ").lower()
    if cont=='y' or cont=="yes":
        choose_day()
    else:
        print("Thank You")
        return

choose_day()


#* can also use match with more complex data structures like lists and tuples.

def process_data(data):
    match data:
        case [1, 2, 3]:
            return "Matched [1, 2, 3]"
        case [x, y, z] if x == y == z:
            return f"Matched triple value: {x}"
        case _:
            return "No match"

print(process_data([1, 2, 3]))       
print(process_data([4, 4, 4]))       
print(process_data([1, 2, 4]))       