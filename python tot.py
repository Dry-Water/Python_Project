def begin_story(): 
    user_name = input("Please enter your name")
    print('You find yourself in the middle of a forest.',
    'What do you do?')
    user_response = int(input('1. Stay there \n2. go north \n3. go east \n4. go south \n5. go west'))
    choice_one(user_response, user_name)
    choice_two(user_response, user_name)
    choice_three(user_response, user_name)
    choice_four(user_response, user_name)

def choice_one(user_response, user_name):
    #1. You press the door open button to exit as soon as possible. 
    if (user_response == 1):
        print("You hear a hissing sound, maybe staying there is not the greatest idea")
        user_response = int(input("1. You died a horrible death."))
       
    #2. You punch the man. 
def choice_two (user_response, user_name):
  
     if (user_response == 2):
        print('You walked until you saw a fault. It spans for miles. It is impossible for you to cross over in any way.')
        user_response = int(input("1. try to jump over anyway \n2. find way down \n3. go east \n4. go south \n5. go west"))
     if(user_response == 1):
           print('You close your eyes and take a big leap forward. It seems you are flying, but when you open your eyes, you are indeed falling to your death. In a matter of seconds, you land face first on the cold, hard, rocky ground, dying instantly.')
     elif(user_response == 2):
             print('There seems to be different levels of elevation at the walls around the cliff, but a rope or ladder is required')
             user_response = int(input('1. try to jump over anyway\n2. find way down \n3. go east \n4. go south \n5. go west'))
             

     elif(user_response == 3):
        print("You stop in front of a man in front of a simplistic shack. He exclaims, good day, would you like anything from my shack?")
        user_response = int(input("1.ask what he sells")) 
        choice23_one()
        
     elif (user_response == 4):
        print('You find yourself in the middle of a forest.',
    'What do you do?')
        user_response = int(input('1. Stay there \n2. go north \n3. go east \n4. go south \n5. go west'))
        choice_one(user_response, user_name)
        choice_two(user_response, user_name)
        choice_three(user_response, user_name)
        choice_four(user_response, user_name)
        
     elif(user_response == 5):
       print('You find a hole, but it looks more like a cave. You feel an immense pressure and a bright light.')
       user_response = int(input('1.choices TBD'))

def choice23_one():
  int(input('1. A golden sword \n2. A lizard \n3. A gag card'))

      
def choice_three(user_response, user_name):
  
     if(user_response == 3):
       print('You tripped on a root while walking, tumbling to an open area in a forest. There is no way to get back where you were it seems, but you did conveniently land on an abandoned camping ground. What do you do?')
       user_response = int(input('1. go north \n2. go east \n3. go west\n4. feel the ground\n5. Set up camp'))
       choice3_two(user_response, user_name)
       choice3_one(user_response, user_name)
       choice3_three(user_response, user_name)
       choice3_four(user_response, user_name)
       choice3_five(user_response, user_name)
  
def choice3_one(user_response, user_name):
        print('A rusty, wore-down sword is on the ground; the foliage is becoming more prominent')
        user_response = int(input('choices TBD'))
        

        
       
def choice2_four(user_response, user_name):
      if(user_response == 4):
        print('You find a white house. What do you do?')
      user_response = int(input('choices TBD'))
begin_story()
  