
#divisible by 3 and 5 
#the object of this code is to check a specific range of nbs which are divisible by 3 and 5 both
#hint:for a nb to be divisible by a number is having remainder = 0 once dividing it by the number 
#so we will use the modulus operator % to check the remainder of the division of the number by
#3 and 5 and if the remainder is 0 then the number is divisible by 3 
#and 5 and we will print it out


number = int(input("Please enter a number :")) 
 #inputing a number to check the divisible nb by 3 and 5

for i in range (number):
   #
   if i % 3 == 0 and i % 5 == 0: #checking if the number is divisible by 3 and 5 
      print(i , end =' ') 



        
