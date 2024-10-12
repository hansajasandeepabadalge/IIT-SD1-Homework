#Get the makrs as iinput and if the makrs is 50 or above pass otherwise week

marks = int(input("Enter your marks: "))

if marks >= 50: #if this boolean expression is true then execute if block
    print("pass")
else: #if it is false this else block execute
    print("weak")