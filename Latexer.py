path = input('give path to the file: ')
text = open(path,'r')
latex = open('latexified.txt','w')
line = text.readline()
while line:
    values = line.split() #split at empty spaces
    StringToWrite = ' & '.join(values) + str('\\\\ \n')
    latex.write(StringToWrite)
    line = text.readline()
text.close()
latex.close()