# diamond 
#objective to this code is to create specific nb of rows that creates the shape of diamond
# the number of rows is specified by the user


x = int(input("Enter please a number: ")) 
  #specifing the nb of rows 

spaces = x 
 #nb of spaces are according to the input

for j in range (1,x*2,2):

  #for loopfor generating the stars in each row,starting from
  #1 star to x*2 stars moving 2 by 2 
  #nb of stars is odd nb 1 ,3 ,5....

  print(" " * spaces + "*"*j)

  #print the spaces and stars in each row

  spaces-=1

  #decreasing the nb of spaces in each row by 1

spaces= 1 

for j in range (x*2-1,0,-2):

  #generating the opposite side for the diamond that have decreasing nb of stars
  #starting from range x*2-1 ,decreasing by -2 to have odd number

  print(" " * spaces + "*"*j) 

    #print the spaces and stars in each row

  spaces+=1

  #increasing the nb of spaces in each row by 1
  
print()





