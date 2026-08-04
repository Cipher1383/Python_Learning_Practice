usr_inp = input("Please Enter a number to check: ")
proc_inp = int(usr_inp)
inp_len = len(usr_inp)

j= 0
for i in range(inp_len):
    rem = int(proc_inp % 10)
   # print(rem)
    j+=rem**inp_len
    proc_inp /= 10

if j == int(usr_inp):
    print("The Entered number is an Armstrong Number!!")
else:
    print("The Entered number is NOT an Armstrong Number!!")



