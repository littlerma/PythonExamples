def adder(a, b=[]):
    b.append(a)
    return b
def test():
	input = raw_input("enter a word here: ")
	print adder(input)
 
def inputs():
	i = 0
	for i in range(1,10):
		test()
	
		
inputs()