# sum of ODD numbers
#objective of this code is to add the odd numbers to a specific number
#for a number to be odd the remainder foe the division operation by 2 must be not zero
# so we will use a for loop to iterate over the range of numbers from 1 to the input
# number and check if the number is odd by using the modulus operator % and if it is odd
# we will add it to the sum variable and print the sum at the end of the loop


number = int(input("Please enter a number :"))

sum_odd = 0 #a variable to add to 

for i in range (number):
   
   if i % 2 != 0 : #checking if the number is odd
      
      sum_odd += i #adding the odd number to the sum
     
print("The sum of all odd numbers from 0 to ",number," is ",sum_odd) 