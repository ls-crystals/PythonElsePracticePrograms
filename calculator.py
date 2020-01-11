def main():
   print('''Select operation.
   1.Add
   2.Subtract
   3.Multiply
   4.Divide
            ''')
   num1 = int(input('Enter number1: '))
   num2 = int(input('Enter number2: '))
   op = int(input('Enter choice 1, 2, 3,or 4: '))
   if op < 1 or op > 4 :
      print('Invalid input')
   elif op == 1:
    print(num1,'+',num2, '=',add(num1,num2,op))
   elif op == 2:
      print(num1,'-',num2, '=',subtract(num1,num2,op))
   elif op == 3:
      print(num1,'*',num2, '=',multiple(num1,num2,op))
   elif op == 4:
      print(num1,'/',num2, '=',divide(num1,num2,op))
   else:
      print('invalid input')

def add(num1,num2,op):
        res = num1 + num2
        return (res)
def subtract(num1,num2,op):
        sult = num1-num2
        return (sult)
def  multiple(num1,num2,op):
          mul = num1 * num2
          return (mul)
def divide(num1,num2,op):
   div = num1/num2
   return (div)


main()
