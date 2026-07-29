print("Multiplication Table".center(40,"*"))
usr_num = int(input("Please Enter the number to generate the Multiplication table: "))
for i in range(1,11):
    print(f"{usr_num} * {i} = {usr_num*i}")
