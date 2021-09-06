import random
import random as ran 
n=int(input("Enter number of series you want paly: "))
user_w=0
comp_w=0
for i in range(n):
  user=input("Choose ODD or EVEN: ").lower()
  if user=="odd":
    comp="even"
  else:
    comp="odd"
  print("user choosed:-",user)
  print("computer choosed:-",comp)

  user_n = int(input("Enter any number between 1 to 6 including 1&6 :"))
  comp_n = ran.randint(1,6)
  
  print("User choosed:-",user_n)
  print("Computer choosed:-",comp_n)
  
  toss=user_n+comp_n
  print("toss :- ",toss)

  if toss%2==0:
    if comp=="even":
      print("Computer won the toss :) ")
      comp2=random.choice(("bat","ball"))
      print("Computer choose: ",comp2)
      if comp2=="bat":
          user2="ball"
      else:
          user2="bat"
    else:
      print("User won the toss :) ")
      user2=input("Choose bat or ball: ").lower()
      if user2=="bat":
          comp2="ball"
      else:
          comp2="bat"
  else:
    if comp=="odd":
      print("Computer won the toss :) ")
      comp2=random.choice(("bat","ball"))
      print("Computer choose: ",comp2)
      if comp2=="bat":
          user2="ball"
      else:
          user2="bat"
    else:
        print("user won the toss :) ")
        user2=input("choose bat or ball: ").lower()
        if user2=="bat":
            comp2="ball"
        else:
            comp2="bat"      

  counter_c = 0
  counter_u = 0
  def user_bat_comp_ball():
      global counter_c
      global counter_u
      comp_3=0
      user_3=1
      print("USER's BATTING---------")
      while comp_3 != user_3:       
          user_3 = int(input("Enter any number between 1 to 6 including 1&6 :"))
          comp_3 = ran.randint(1,6)
          print("User run :-",user_3)
          print("Computer run :-",comp_3)
          if(comp_3!=user_3):
              counter_u = counter_u + user_3  
      print("Total User's run :--",counter_u)

  def user_ball_comp_bat():
      global counter_c
      global counter_u
      comp_3=0
      user_3=1
      print("USER's BALLING---------")
      while comp_3 != user_3:
          user_3 = int(input("Enter any number between 1 to 6 including 1&6 :"))
          comp_3 = ran.randint(1,6)
          print("User run :-",user_3)
          print("Computer run :-",comp_3)
          if(comp_3!=user_3):
              counter_c = counter_c + comp_3
      print("Total Computer's run :--",counter_c)
 
  if comp2 == "bat":
      user_ball_comp_bat()
      user_bat_comp_ball()
      if counter_u > counter_c:
          print("........User Won........")
          user_w=user_w+1
      else:
          print("........Computer Won........")
          comp_w=comp_w+1
         
  if comp2 == "ball":
      user_bat_comp_ball()
      user_ball_comp_bat()
      if counter_u > counter_c:
          print("........User Won........")
          user_w=user_w+1
      else:
          print("........Computer Won........")
          comp_w=comp_w+1
print("Number match won by User: ", user_w)
print("Number match won by Computer: ", comp_w)
if user_w>comp_w:
  print("User won the series!!!!")
elif user_w==comp_w:
  print("Series tie!!!!")
else:
  print("Computer won the series!!!!")