def my_hang():
    my_list=["py","java","css","html","edu"]
    words=random.choice(my_list)
    turn=10
   
    your_guess=''

    val_guess=(set(" abcdefghijklmnopqrstuvwxyz "))

    while len(words)>0:
        new_word=""

        for index in words:
            if index in your_guess:
                new_word=new_word+index
                
            else:
                new_word=new_word+"_ "
               
         
        if new_word==words:
            print(new_word)
            print("wow!","*** you won ***")
            break
            

        print("please guess the word:-",new_word)

        guess=input()
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
        if guess in val_guess:
            your_guess=your_guess+guess
            
        else:
            print("please enter vaild chractor!!")
            
            guess=input()

        if guess not in words:
            turn=turn-1
            

            if turn == 9:
                print("9 turns left !!!")
                print("        +-------+")
                print("          |     |          ")
                print("                |          ")
                print("                |          ")
                print("                |          ")   
                print("                |          ")
                print("                =========  ")


            if turn == 8:
                print("8 turns left !!!")
                print("        +-------+")
                print("          |     |          ")
                print("          O     |          ")
                print("                |          ")
                print("                |          ")   
                print("                |          ")
                print("                =========  ")


            if turn == 7:
                print("7 turns left !!!")
                print("        +-------+")
                print("          |     |          ")
                print("          O     |          ")
                print("         /      |          ")
                print("                |          ")   
                print("                |          ")
                print("                =========  ")


            if turn == 6:
                print("6 turns left !!!")
                print("        +-------+")
                print("          |     |          ")
                print("          O     |          ")
                print("         /|     |          ")
                print("                |          ")   
                print("                |          ")
                print("                =========  ")


            if turn == 5:
                print("5 turns left !!!")
                print("        +-------+")
                print("          |     |          ")
                print("          O     |          ")
                print("         /|\    |          ")
                print("                |          ")   
                print("                |          ")
                print("                =========  ")


            if turn == 4:
                print("4 turns left !!!")
                print("        +-------+")
                print("          |     |          ")
                print("          O     |          ")
                print("         /|\    |          ")
                print("                |          ")   
                print("                |          ")
                print("                =========  ")


            if turn == 3:
                print("3 turns left !!!")
                print("        +-------+")
                print("          |     |          ")
                print("          O     |          ")
                print("         /|\    |          ")
                print("          |     |          ")   
                print("                |          ")
                print("                =========  ")


            if turn == 2:
                print("2 turns left !!!")
                print("        +-------+")
                print("          |     |          ")
                print("          O     |          ")
                print("         /|\    |          ")
                print("          |     |          ")   
                print("         /      |          ")
                print("                =========  ")


            if turn == 1:
                print("only 1 turn left !!! hangman on his last breath")
                print("        +-------+")
                print("          |     |          ")
                print("          O     |          ")
                print("         /|\    |          ")
                print("          |     |          ")   
                print("         / \    |          ")
                print("                =========  ")


            if turn == 0:
                print("you loose")
                print("you let a good man die")
                print("the word was",words)
                break
        else:
            turn = turn-1

your_name=input("what is your name:- ")

print("hello...welcome! ",your_name)
print("**---------**----------**")
print("**---------***----------**")

print("**guess you word in 10 attempts:--**")
my_hang()
