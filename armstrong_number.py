

def check_armstrong(number):
  number_string = str(number)
  sum = 0
  for i in number_string:
    num=int(i)
    cube_of_number = cube(num)
    sum=sum+cube_of_number
  if number==sum:
    return True
  else:
    return False
def cube(number):
  return pow(number,3)

def main():
  print(check_armstrong(153))

if __name__ == '__main__':main()