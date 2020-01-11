'''Main() promt for y/n

Samantha jones gem store 
2.5 = retail mark up.
retail price = wholesale price * 2.5
price for several
show_retail calc and display retail price
if wholecost > 0 error'''



MARKUP =  2.5 
def main():
    wholesale = float(input('Enter the items wholesale cost: '))
    retprice = int(wholesale * MARKUP)
    show_retail(wholesale,retprice)
    again = input('Do you have another item? (Enter y for yes)')
    while again == 'y':
       main()
    
    
         
	 

def show_retail(wholesale,retprice):
 if wholesale <=  0:
     print('ERROR: The cost cannot be negative.')
     wholesale = float(input('Enter the correct wholesale cost: '))
     print('Retail price: $',retprice)

 else:
     print('Retail price: $',retprice)
	
    

main()


