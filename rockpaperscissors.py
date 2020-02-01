from random import randint

def rps():
    x = ("Rock", "Paper", "Scissors")
    comp = x[randint(0,2)]
    player = False
    char1 = "p" 
    char2 = "q"       
            
    while player == False:
        player = input("""Welcome to Rock, Paper, Scissors! Type 'p' to play or 'q' to quit: """)
        
        
        player = input("Select Rock, Paper, or Scissors: ")
            
        
        if player == comp:
            print("It's a tie! Press ")
                
        elif player == "Rock" and comp == "Paper":
            print("Computer chose paper, you lose.")
        elif player == "Paper" and comp == "Rock":
            print("Computer chose rock, you win!")
        elif player == "Scissors" and comp == "Paper":
            print("Computer chose paper, you win!")
        elif player == "Paper" and comp == "Scissors":
            print("Computer chose scissors, you lose.")
        elif player == "Rock" and comp == "Scissors":
            print("Computer chose scissors, you win!")
        elif player == "Scissors" and comp == "Rock":
            print("Computer chose rock, you lose.")
        elif player == "Rock" and comp == "Paper":
            print("Computer chose paper, you lose.")
        player = False
        comp = x[randint(0,2)]
     

rps()
    
