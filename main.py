# Starting point
acc = input('Hello. What are you here for today?\n (1) Check Current Balance\n (2) Deposit Money\n (3) Withdrawal Money\n (4) Create Account\n (5) Delete Account\n Please type the number of option in words in lowercase.')

account = bank = {} #List of accounts and data

# Check Current Balance
def one():
  print(f'{bank.name}, you currently have ${bank.money}.\n ')

# Deposit Money
def two():
  deposit = input('How much do you want to deposit?\n ')
  bank['money'] += {deposit} #amount added to the account
  print(f'{bank.name}, you currently have ${bank.money}.\n ')

# Withdrawal Money
def three():
  withdrawal = input('How much do you want to withsrawal?\n ')
  bank['money'] -= {withdrawal} #amount deducted from the account
  print(f'{bank.name}, you currently have ${bank.money}.\n ')

# Create Account
def four():
  account = {} #creates new account
  
  create_name = input('Account name:\n ') #make a name
  account['name'] = {create_name}
  
  initial_money = input('How much would you like to deposit into the new account?\n ') #Starting Money
  account['money'] = {initial_money}

# Delete Account
def five():
  delete_account = input('Insert the account you want to terminate.\n ')
  account.bank.remove[{delete_account}]
  print('Account has been removed')

# Loop back to starting point
acc = input('Hello. What are you here for today?\n (1) Check Current Balance\n (2) Deposit Money\n (3) Withdrawal Money\n (4) Create Account\n (5) Delete Account\n Please type the number of option in words in lowercase.')