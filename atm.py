def account_menu():
    options = """
        Welcome to Hibs Banking services
        1 -> Create Account
        2 -> Check Acount
        3 -> Check Balance
        4 -> Deposit Money
        5 -> Withdraw Money
        6 -> Transfer Money
        7 -> Change Pin 
"""
    print(options)

    match(choice)
        case "1" :

accounts = []
def create_account(first_name,last_name,pin,phone_number,balance = 0.0 ):
    account_number =  phone_number[1:]
    accounts.append([first_name, last_name, account_number, pin, phone_number, balance])
    return accounts

def check_accounts():
    for account in accounts:
        print(f"Thank you for creating an account with us here is your bank details \nFull name:  {accounts[0]} {accounts[1]} \nAccount Number: {accounts[2]} \nPin: {accounts[3]} \nPhone Number: {accounts[4]} \n Account balance: {accounts[5]} ")


