def main():
    books = int(input('Enter the number of books purchased: '))
    showPoints(books)
def showPoints(books):
    if (books == 0):
      points = 0
      print("You have purchased", books ,"books. This earns you",points,'points.')
    elif(books == 1):
        points = 5
        print("You have purchased", books ,"books. This earns you",points,'points.')
    elif(books == 2):
        points = 15
        print("You have purchased", books ,"books. This earns you",points,'points.')
    elif(books == 3):
        points = 30
        print("You have purchased", books ,"books. This earns you",points,'points.')
    elif(books == 4):
        points = 60
        print("You have purchased", books ,"books. This earns you",points,'points.')
        print('thanks for the support!')
main()

'''
def main():
    books = int(input('Enter the number of books purchased: '))
    showPoints(receipts(points))
def receipts(points):
    receipts = print("You have purchased", books ,"books. This earns you",points,'points.')

def showPoints(books):
    if (books == 0):
      points = 0
      receipts(points)
    elif(books == 1):
      points = 5
      receipts(points)
    elif(books == 2):
        points = 15
        receipts(points)
    elif(books == 3):
        points = 30
        receipts(points)
    elif(books == 4):
        points = 60
        receipts(points)
main()
'''
