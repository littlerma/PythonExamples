# search using while loop

def search_char_in_string(char,word):
  index = 0
  while index < len(word):
    if char == word[index]:
      return index
    index += 1
  return 'not found'

print(search_char_in_string('f','macha'))

# search using for 

def search_char_in_string(word,char):
  for i in range(len(word)):
    
    

print(search_char_in_string('macha','c'))
    



    