def main():
    print("Welcome to Build your Own Pizza\n")
    print("Choose from the below Options.....\n")
    var_size = input("Choose the Size:(Enter 1 or 2 or 3.. 1.Small 2.Medium 3.Large : ")
    while var_size not in ["1","2","3"]:
        print("Invalid Option Selected")
        var_size = input("Choose the Size:(Enter 1 or 2 or 3.. 1.Small 2.Medium 3.Large : ")

    var_base =input ("Choose your base ... 1.Classic Crust 2.Thin and Crispy 3.Deep Pan : ")
    while var_base not in ["1","2","3"]:
        print("Invalid Option Selected")
        var_base = input("Choose your base ... 1.Classic Crust 2.Thin and Crispy 3.Deep Pan : ")

    var_top =input("How many Toppings would you like ?:")
    var_eat_choice = input("Please Choose: 1.Eat-In 2.Take-away : ")
    while var_eat_choice not in ["1","2"]:
        print("Invalid Option Selected")
        var_eat_choice = input("Please Choose: 1.Eat-In 2.Take-away : ")

    var_disc = input("please Enter the Discount Code : ")
    if var_disc != 'PIZZ4':
        print("Discount Code is not Valid,No Discount will be Applied...")
        act_disc = 0
    else:
        act_disc = 1

    calc_price(int(var_size),int(var_base),float(var_top),int(var_eat_choice),int(act_disc))


def calc_price(p_size,p_base,p_top,p_eat_choice,p_disc):
    if p_size ==1:
        p_size =6
    elif p_size ==2:
        p_size= 8
    else:
        p_size= 10
    if p_base == 1:
        p_base = 0
    elif p_base == 2:
        p_base = 1
    else:
        p_base = 2
    p_top *= 1.5

    if p_eat_choice == 1:
        p_eat_choice = 2
    total = p_size + p_base + p_top + p_eat_choice
    print(total)
    if p_disc == 1:
        gross_price = (total * 20) /100
        print(gross_price)
    else:
        gross_price = 0
        print(gross_price)
    net_price = total - gross_price

    print(f"Your Total Price for your Pizza is : {net_price}$")

if __name__ == "__main__":
    main()


