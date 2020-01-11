'''def main():
    number = float(input('Enter a number: '))
    checkNum(number)

def checkNum(number):
    print('The number entered is: ',number)
    if number % 2 == 0:
        print(number, 'is an even number')
    else:
        print(number, 'is an odd number')
main()



def main():
    hours = float(input('how many hours did you work'))
    rate = float(input('whats your hourly rate?'))
    overtime = float(hours - 40 * 1.5 + (hours * rate))
    pay =  float(hours * rate)
    

    calWage(hours,pay,overtime)
    
def calWage(hours,pay,overtime):
    if hours > 40:
        print('your pay is ', overtime)
    else:
        print('your pay is ',pay )
    
    
    
main()




def main():
    num = float(input('Enter a number'))
    numType(num)

def numType(num):
    if num < 0:
        print('You have entered a negative number ')
    elif num > 0:
         print('You have entered a positive number ')
    if num == 0:
        print('you have entered 0 ')
main()










salary = float(input('Enter salary '))
def loanShark():
    if salary >= 30000:
       years_on_the_job = float(input('Enter amount of years worked '))
       if years_on_the_job >= 2:
        print('  Congratulations you qualify ')

       else:
         print('Unfourtunately, you are inelligable, you must have worked for at least teo consecutive years ')
    else:
      print('Unfourtunately, you are inelligable, you must earn at least 30,000$ ')

      
loanShark()






def gradeConvert():
    grade = float(input('Enter your grade: '))
    if grade < 60:
        print('You have unfourtunately recieved an F. Take your education seriously chap U didnt try did u?')

    elif grade <=69 :
        print('You recieved a D. Take your education seriously chap just try a little harder yah?')
    elif grade <=79 :
        print('You recieved a C. You passed! But by the skin of your teeth tho, careful fam')

    elif grade <=89 :
        print("You recieved a B. Great Job! You passed! But I know your ambitious, letss get thoose A's! ")
    elif grade >=90 :
        print("You recieved AN A. YOU SUPER LITT EVEN THO STANDARDIZED TESTING MEANS NOTHINGGGG! You passed!YOU EXCELLED! IM GLAD FOR U ! ")

gradeConvert()

if number == 1:
    print('One')
else:
    if numberr ==2:
        print('Two')
    








def main():
    num1 = float(input('Enter a number'))
    num2 = float(input('Enter a number'))
    num3 = float(input('Enter a number'))
    checkNum(num1,num2,num3)
def checkNum(num1,num2,num3):
    print('Numbers printed are', num1,num2,num3)
    if num1<num2




:
main()




years_on_the_job = float(input('Enter amount of years worked: '))
salary = float(input('Enter salary: '))
def loanShark():
    if salary  <= 30000 and years_on_the_job >= 2:
        print('Congratulations you qualify ')
    else:
         print('Unfourtunately, you are inelligable, you must have worked for at least teo consecutive years ')
    
      
loanShark()



#checking numeric ranges

#range ()start,stop[,step]


def ellligable():
  num = float(input('Enter a number: '))
  if num >= 20 or num >= 40:
     print('The number entered is within the acceptable range')
  elif num > 20 or num < 40 :
    print('The number entered is not in the acceptable range')
ellligable()

'''

def software():
  quan = float(input('Enter the number of packages purchased'))
  price = float(quan * 99 )
  discount = price - off
  off = float(.20 * price)
  if quan >= 20 or quan >= 40:
    print('your dicount is',discount)
    print('your price is',price - discount)





software()
