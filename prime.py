# method to check if a number is prime
def check_prime(number):
  if number % 2 == 0 or number % 3 == 0:
    print 'not a prime'
  else: 
    print 'prime'

# method to check if a string is palindrome or not
def check_palindrome(string):
  status = True
  if len(string) == 1 or len(string) == 0:
    status = True
  else:
   for index in range(len(string)/2):
     if string[index] == string[len(string)-1-index]:
       status = True
     else:
       status = False
  if status == True:
    print 'palindrome'
  else:
    print 'not a palindrome'
    




