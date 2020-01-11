import random

###The Guess Game ###
name = input('Hello! , What is your name? ')
'''

'''
print('Well', name, ',I am thinking of a number between 1 and 20.''''
''')


def main():

 print('Take a guess: ')
 guess = int(input('What is your number? '))
 game(guess)





def game(guess):
    count = 1
    rand = random.randint(1,20)
    if (guess == rand):
     print( 'Good job, you have guessed my number in number in,',count,',guess''''

     ''')
     count +=1
     
    elif (guess < rand):
      print( '''Your guess is to low 

     ''')
      while count < 6:
       main()
       print('Nope, the number I was thinking of was: ',rand )
       count +=1

main()
