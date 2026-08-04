usr_bal = 8000


def wthd_cash (usr_bal):
    wc_amt = float(input('Enter the Amount to Withdraw: '))
    while wc_amt > usr_bal:
        print("Balance low!!!... Cannot Withdraw the requested amount, Please try a Different Amount")
        wc_amt = float(input('Enter the Amount to Withdraw: '))

    usr_bal -= wc_amt
    print("Cash Withdraw Successful")
    print(f'Total Balance in your account is : {usr_bal}')

def add_cash(usr_bal):
    dep_amt = int(input('Enter the Amount to Deposit: '))
    usr_bal += dep_amt
    print(f'Total Balance in your account is : {usr_bal}')


print('Welcome to the Bank'.center(44,'*'))
usr_pin = int(input("Please Enter your PIN: "))
while usr_pin != 3498:
    print("You have Entered an Invalid PIN... Please try again")
    usr_pin = int(input("Please Enter your PIN: "))
bank_dict =  {1:"Balance Check",2:'Cash Withdrawal',3:'Cash Deposit'}

print('Banking Options'.center(44,'-'))
print('1. Check you Balance'.ljust(25))
print('2. Withdraw Cash'.ljust(25))
print('3. Deposit Cash'.ljust(25))
usr_opt = int(input("Please choose an Option: "))
while usr_opt not in (1,2,3):
    print('Invalid Choice. Please try again...')
    usr_opt = int(input("Please choose an Option: "))

print(f"you have chosen {bank_dict[usr_opt]} Option... ")
if usr_opt == 1:
    print(f'Total Balance in your account is : {usr_bal}')

elif usr_opt == 2:
    wthd_cash(usr_bal)

elif usr_opt == 3:
    add_cash(usr_bal)











