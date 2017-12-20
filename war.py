import random 

class Player:
    def __init__(self,hand=[]):
        self.hand = hand 
        
    
    def play_card(self): 
        self.card = self.hand[0]
        self.hand.pop(0) 
        return(self.card) 
    
    def pickup(self,card,other):
        self.hand.append(card)
        self.hand.append(other) 
    

cards = ["2","3","4","5","6","7","8","9","10","11","12","13","1"]
suits = ["S","H","D","C"]

deck = []

for d in range(len(suits)):
    for c in range (len(cards)): 
        deck.append(cards[c]+suits[d])

random.shuffle(deck)

player1 = Player()

player2 = Player() 

player1.hand = deck[0:len(deck)/2]
player2.hand = deck[len(deck)/2:len(deck)]

print (player1.hand,len(player1.hand))
print (player2.hand,len(player2.hand)) 

game = True

while game == True: 
    
    if len(player1.hand) == 0 or len(player2.hand) == 0:
        game == False 
    
    p1 = player1.play_card()[0]
    p2 = player2.play_card()[0]
    

    if p1 > p2:
        player1.pickup(p1,p2)
        print ("p1",len(player1.hand)) 
        print("p2",len(player2.hand)) 
    elif p1 < p2: 
        player2.pickup(p2,p1)
        print ("p1",len(player1.hand)) 
        print("p2",len(player2.hand)) 
    elif p1 == p2:
        game = False 
        

print ("done") 
    
    
    
    
    
