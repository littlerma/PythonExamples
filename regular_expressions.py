# this code snippet shows and example of how to use regualr expressions in python.
# first 're' module is imported from python library
# findall is a powerful function available in the re module


import re
string = 'hello macha 6699'
# findall, finds anything that you want 
# using '\D' will find return everything excluding numbers
text = re.findall(r'\D',string)
print text

# using '\d' will return only numbers

text = re.findall(r'\d',string)
print text

# using no search parameter 

text = re.findall('[a-c]|[7-9]',string)
print text

text = 'my name is pranith chander teja macha'
print re.sub('chander','chandra',text)

languages = ['python','perl','php','c++','c#','java']
pattern = '^b|^p|l$|a$'
for lang in languages:
  if re.search(pattern,lang,re.IGNORECASE):
    print lang +' found'
  else:
    print lang +' not found'

