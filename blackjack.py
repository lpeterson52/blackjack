import random

class card:
    
    def __init__(self,suit,num):
        #1 is clubs, 2 is diamonds, 3 is hearts, 4 is spades
        self.suit = suit
        #number of card 1-10 is normal 11 is jack 12 is queen 13 is king
        self.num = num
    
    def getNum(self):
        return self.num
    
    def __str__(self):
        tempsuit = ""
        
        if(self.suit==1):
            tempsuit = "Club"
        elif(self.suit==2):
            tempsuit = "Diamond"
        elif(self.suit==3):
            tempsuit = "Heart"
        else:
            tempsuit = "Spade"
        
        if(self.num == 11):
            return "Card: Jack, Suit: " + tempsuit
        elif(self.num == 12):
            return "Card: Queen, Suit: " + tempsuit
        elif(self.num == 13):
            return "Card: King, Suit: " + tempsuit
        elif(self.num == 1):
            return "Card: Ace, Suit: " + tempsuit
        else:
            return "Card: " + str(self.num) + ", Suit: " + tempsuit
            
    

class deck:
    
    cards = []
    def __init__(self):
        for i in range(0,13):
            for j in range(0,4):
                self.cards.append(card(j + 1, i + 1))
                
    @classmethod            
    def printDeck(self):
        for i in range(0,len(self.cards)):
            print(self.cards[i])
            
    def shuffleDeck(self):
        random.shuffle(self.cards)
    
    def getDeck(self):
        return self.cards
    def refillDeck(self):
        self.__init__
    


class player:
    cards = []
    def __init__(self):
        self.cards = []
        
    def __str__(self):
        temp = "Player Cards | "
        for card in self.cards:
            temp = temp + str(card) + " | "
        return temp
            
            
    def numAces(self):
        sum = 0
        for card in self.cards:
            if(card.getNum() == 1):
                sum += 1
        return sum
                
        
    def sumOfCards(self):
        sum = 0
            
        for card in self.cards:
            if(card.getNum() == 1):
                sum += 11
            elif(card.getNum() > 10):
                sum += 10
            else:
                sum += card.getNum()
            
        if(self.numAces() > 0):
            for i in range(0,self.numAces()):
                if(sum > 21):
                    return sum - 10
                sum - 10
        return sum
            
    def drawCard(self, deck):
        self.cards.append(deck.pop(0))
            
    def addCard(self, card):
        self.cards.append(card)
    def dealCards(self, deck):
        self.cards.clear()
        self.cards.append(deck.pop(0))
        self.cards.append(deck.pop(0))
    
    
        

class dealer(player):
    
    def __init__(self):
        self.cards = []
        self.revealed = False
        
    
    
    def __str__(self):
        temp = "Dealer Cards | XXXX | "
        for i in range(1,len(self.cards)):
            temp = temp + str(self.cards[i]) + " | "
        return temp
    def printCards(self):
        for card in self.cards:
            print(card)       
            
    def shouldHit(self):
        sum = self.sumOfCards()
        if(sum < 17):
            return True
        return False
    
        



def main():
    running = True
    userTurn = True
    dealerTurn = False
    user = player()
    dealer1 = dealer()
    maindeck = deck()
    userBust = False
    amtOfChips = 500
    betAmt = 0
    betting = True
    maindeck.shuffleDeck()
    print()
    while(running):
        betting = True
        userTurn = True
        print("You have " + str(amtOfChips) + " chips")
        while(betting):
            
            userinput = input("How much would you like to bet: ")
            try:
                betAmt = int(userinput)
            except ValueError:
                print("Please enter a number")
            
            if(betAmt > amtOfChips):
                print("You don't have enough chips")
            elif(betAmt > 0):
                amtOfChips -= betAmt
                betting = False
        #If deck is close to being empty refill and shuffle
        if(len(maindeck.getDeck()) <= 4):
            maindeck.refillDeck()
            maindeck.shuffleDeck()
        user.dealCards(maindeck.getDeck())
        dealer1.dealCards(maindeck.getDeck())
        print(dealer1)
        #User Turn, asks user to hit or not
        while userTurn:
            print(user)
            print("Sum: " + str(user.sumOfCards()))
            userinput = input("Hit? (y or n)")
            if(userinput == "y"):
                user.drawCard(maindeck.getDeck())
                if(len(maindeck.getDeck()) == 0):
                    maindeck.refillDeck()
                    maindeck.shuffleDeck()
            else:
                userTurn = False
            if(user.sumOfCards() > 21):
                print("You Bust")
                userBust = True
                print(user)
                print(user.sumOfCards()) 
                userTurn = False
        
        dealerTurn = True
            
        while dealer1.sumOfCards() < 17 and userBust == False:
            dealer1.drawCard(maindeck.getDeck())
            if(len(maindeck.getDeck()) == 0):
                maindeck.refillDeck()
                maindeck.shuffleDeck()

        print()        
        print("---------------------------------")
        print()
        print("Dealer's Cards:")
        dealer1.printCards()
        print(dealer1.sumOfCards())

        if(dealer1.sumOfCards() > 21):
            print("Dealer Bust! You Win!")
            amtOfChips += 2 * betAmt
        elif(user.sumOfCards() > 21):
            print("User Bust! Dealer Wins!")
        elif(dealer1.sumOfCards() > user.sumOfCards()):
            print("Dealer Wins!")
        elif(dealer1.sumOfCards() < user.sumOfCards()):
            print("User Wins!")
            amtOfChips += 2 * betAmt
        else:
            print("Tie!")
            amtOfChips += betAmt
        if(amtOfChips <= 0):
            print("You are broke")
            running = False
        print()
        print()
    
        
        
    
main()
    