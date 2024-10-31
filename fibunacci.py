# fibonacci
# the Fibonacci sequence is a series of numbers in which each number (after the first two) 0,1
# is the sum of the two preceding ones . Using the list we can esily use the previous numbers and add them
# to get the next number in the sequence


number = int(input("Please enter a number :"))
# Number of terms to generate

fibonacci_list = [0, 1]
# Initialize the list with the first two Fibonacci numbers


for i in range(2, number):
    # Generate the rest of the sequence usinf a for loop starting with 2

    next_number = fibonacci_list[i - 1] + fibonacci_list[i - 2]
    # Fn=Fn-1 + Fn-2 ,means the next number is the sumof the 2 previous ones

    fibonacci_list.append(next_number)
    #adding the next sequence to the list 

print(fibonacci_list)
# Print the sequence




   