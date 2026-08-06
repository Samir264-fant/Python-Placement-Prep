#search for a number x in this tuple using loop
t = (1,4,9,16,25,36,49,64,81,100)
x = int(input("Enter a number to search: "))
for n in t:
    if n == x:
        found = True
        break
    if found:
        print(f"{x} is found in the tuple.")
    else:
        print(f"{x} is not found in the tuple.")