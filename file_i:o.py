def write_file():
  fout = open('output.txt','w')
  text = 'this has to be written into the file \n'
  fout.write(text)
  fout.close()

write_file()