import validations

def first_name(name):
  first_name = name
  if (validations.valid_string(first_name) == False):
    print 'error :'
first_name('macha%')
first_name('x')