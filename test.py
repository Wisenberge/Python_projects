import circle     #imports a file and allows its functions to be used.   print(circle.pi)
from circle import * # imports the parameters directly so you could print(pi)

nameHandle = open('kids', 'w')    #opens a file called "kids" with "w" read/write "r" read
nameHandle.write(name + '/') # writes to file
nameHande.close() #closes file


# Touples are data structures. Like strings but can include numbers as well. defined by ()  or (1, 'test')
# lists are defined with brackets [] while touples are defined with ()
# touples are immutable while lists are mutable. We can change values within a list but not a touple 

#def oddTuples(aTup):
  #  '''     - creates a description of the function within '''
   # aTup: a tuple
    
    #returns: tuple, every other element of aTup. 
    #'''


#map is a handy way to apply a function to a collection of values.   Iterates over a list and returns the output of the function into index 
#dictionaries - list that doesn't go by index, but by key
#dictionary      testdictionaryGrades = {}          testdictionaryGrades = {'Anna':'B', 'John':'C'}    testdictionaryGrades ['John']  will pull back 'C'