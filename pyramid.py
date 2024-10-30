# pyramid of numbers 
#objective is to create nb of rows each is counting from 1 to a specific input
#we should use loop because its repeating the action of creting rows each with different nbs


x = int(input("Enter please a number: ")) 
  #enter an integer,representing the nb of rowsyou want to generate

for i in range (1,x+1):
   # making a for loop to generate x rows, range from 1 to x+1 exclusive 0 and including the x value
  
  for j in range (1,i+1):
     #another for loop to generate the numbers in each row 
     #the range is from 1 to i+1 to include the i value 
     #it starts counting in each row from 1 to i+1

    print(j ,end=' ' )
     #print the values in each row each in a line 

  print() 
  # new line after each row
  