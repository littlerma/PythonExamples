# this code prints the multiplication tables of numbers in the range of wo numbers

def multiplication_tables(number1,number2):

  if number1 > number2:
    temp = number1
    number1 = number2 
    number2 = temp
  for i in range(number1,number2+1):
   print '-'*20
   print 'printing %d table'%(i)
   print '-'*20
   number = 1
   table_number = i
   while number <= 10:
     print '%s * %s = %d'%(number,table_number,number*table_number)
     number = number+1
   print '-'*20
   print 'done...'
   print '-'*20

multiplication_tables(1,11)

