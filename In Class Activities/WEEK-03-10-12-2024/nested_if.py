#Get the makrs as iinput and if the makrs is 50 or above pass otherwise week

marks = int(input("Enter your marks: "))

if 0 <= marks <= 100:
    if marks >= 50: #if this boolean expression is true then execute if block
        print("pass")
    else: #if it is false this else block execute
        print("weak")
else:
    print("Invalid Marks!!! Please enter a value between 0 and 100")