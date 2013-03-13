def count_characters(word,character):
  index = 0
  count = 0
  while index < len(word):
    print word[index]
    if word[index] == character:
      count += 1
    index += 1
  print 'count of %s\'s in %s is %d'%(character,word,count)

count_characters('macha','a')


