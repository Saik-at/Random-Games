#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from termcolor import colored
import time
for m in range(1000):
    word=input("Hello Player 2, enter a 5 lettered word that Player 1 will guess. Enter a valid word, and in CAPITAL letters.")
    time.sleep(1)
    print("Now scroll down so that Player 1 cannot see the word you entered and return the laptop to Player 1")
    time.sleep(1)
    print("\n \n \n \n \n \n \n \n \n \n \n \n \n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print("Hello Player 1. You need to guess a 5 lettered word in 6 guesses. Enter in caps")
    time.sleep(2)
    print("At the end of each word guessed, the word you guessed will be displayed.") 
    print("Letters in the correct position in the word will be displayed in green.")
    print("Letters that are present in the word but are in incorrect position will be diplayed in yelow.")
    print("Letters that are not present in the word at all will be diplayed in red.")
    print("Enter in CAPITAL letters")
    print()
    time.sleep(2)
    ara=""
    for i in range(6):
         time.sleep(1)
         print()   
         print("Trial #",(i+1))
         time.sleep(1)   
         print()
         str=""
         gue=""
         k=0
         for j in range(5):
              time.sleep(1)  
              print("Guess letter in position #",(j+1))
              a=(input())
              str=str+a
              print(str,end="")
              for k in range(5-j):
                    print(end=" ")
              print()      
              if(a==word[0] or a==word[1] or a==word[2] or a==word[3] or a==word[4]):
                   if(a==word[j]):
                        time.sleep(0.25)
                        gue=gue+colored(a,'green',attrs=['reverse','blink'])+" "
                        time.sleep(1)
                        print()
                   else:
                        time.sleep(0.25)
                        gue=gue+colored(a,'yellow',attrs=['reverse','blink'])+" "
                        time.sleep(1)
                        print()
              else:
                   time.sleep(0.25)
                   gue=gue+colored(a,'red',attrs=['reverse','blink'])+" "
                   time.sleep(1)
                   print()
         ara=ara+gue+"  "       
         print(gue)
         time.sleep(1)
         if(str!= word and 1<=i<=4):
             print()   
             print("Your guesses till now are:")
             print(ara)
             time.sleep(1)
         if(str==word):
             print("Your guess was correct!")
             time.sleep(1)
             print("Congratulations Player 1! You won and you took ",(i+1),"tries to guess the word")
             break
         print() 
         if(i==5):
               print("This was wrong as well. The correct word is "+word)
               time.sleep(1.8)
               print("Congratulations Player 2! You won as Player 1 could not guess the word in 6 trials.") 
    time.sleep(2)
    print("Want to play again? Enter 1. To exit enter 0")
    inp=int(input())
    print()
    print()
    if(inp==0):
        break
    else:
        continue
        time.sleep(1.5)


# In[ ]:




