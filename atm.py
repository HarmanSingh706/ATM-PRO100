class Atm (object):
    
    def __init__(self,cardnumber,pinnumber):
        self.cardnumber=cardnumber
        self.pinnumber=pinnumber

    def checkBalance(self):
        print("Your Current Balance is $7635.20")

    def withdrawBalance(self,amount):
        amountAfterWithdrawl = 7635.20 - amount
        print("You have withdrawn "+str(amount) +". You have $"+ str(amountAfterWithdrawl)+ " left in your account")

def main():
    cardNumber = int(input("Type your card number here: "))
    pinNumber = int(input("Enter your pin here: "))

    createNewUser = Atm(cardNumber, pinNumber)

    print("Would you like to Withdraw? Or would you like to check your balance?")
    print("Tip: Type '2' to withdraw and to check your balance type '1'")
    action = int(input("Good Morning! What would you like to do today?"))

    if (action == 1):
        createNewUser.checkBalance()
    elif(action == 2):
        amount = int(input("Enter the amount of money you would like to withdraw "))
        createNewUser.withdrawBalance(amount)
    else:
        print("Please Enter A Valid Action.")

if __name__ == "__main__":
    main()