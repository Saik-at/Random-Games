#!/usr/bin/env python
# coding: utf-8

# In[ ]:


for k in range(10000):
     list=[1,2,3,4,5,6,7,8,9]
     print(list[:3])
     print(list[3:6])
     print(list[6:])
     flag=0
     for i in range(1,10):
         print(" ")
         if(i%2!=0):
             l=int(input("Player 1 insert position where you want to insert"))
             print(" ")
             list[l-1]="X"
         else:
             l=int(input("Player 2 insert position where you want to insert"))
             print(" ")
             list[l-1]="O"
         print(list[:3])
         print(list[3:6])
         print(list[6:])
         if(((list[0]==list[1]) and (list[1]==list[2])) or ((list[3]==list[4]) and (list[4]==list[5])) or ((list[6]==list[7]) and (list[7]==list[8])) or ((list[0]==list[4]) and (list[4]==list[8])) or ((list[6]==list[4]) and (list[4]==list[2])) or ((list[0]==list[3]) and (list[3]==list[6])) or ((list[4]==list[1]) and (list[1]==list[7])) or ((list[8]==list[5]) and (list[5]==list[2]))):
             if(i%2!=0):
                 print(" ")
                 print("Player 1 won")
                 flag=1
                 break
             else:
                 print(" ")
                 print("Player 2 won")
                 flag=1
                 break
     if(i==9 and flag==0):
         print(" ")
         print("Draw")
     ch=int(input("Enter 1 if you want to continue playing, else enter 0"))
     if(ch==0):
            break
     else:
        
        continue


# In[ ]:




