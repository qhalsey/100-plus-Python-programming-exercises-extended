# Question 1

### **Question:**

##Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
##between 2000 and 3200 (both included).The numbers obtained should be printed in a comma-separated sequence on a single line.

### Hints: 
### Consider use range(#begin, #end) method.***


def special_numbers():
    print_string = ""
    for i in range(2000, 3201):
        if (i % 7 == 0) and (i % 5 != 0):
            print_string += str(i) + ", "

    print(print_string)

special_numbers()

# Question 2

### **Question:**

##Write a program which can compute the factorial of a given numbers.The results should be printed in a comma-separated sequence on a single line.Suppose the following input is supplied to the program: 8
##Then, the output should be:40320

##--------------------
### Hints:
##In case of input data being supplied to the question, it should be assumed to be a console input.***

def factorial(input):
	factorial_answer = 1
	for i in range(1, input + 1):
		factorial_answer = factorial_answer * i

	print(factorial_answer)

factorial(8)

# Question 3

### **Question:**

##With a given integral number n, write a program to generate a dictionary that contains (i, i x i) such that is an integral number between 1 and n (both included). and then the program should print the dictionary.Suppose the following input is supplied to the program: 8***

##Then, the output should be:***

##{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}

##------------------

### Hints: 
##In case of input data being supplied to the question, it should be assumed to be a console input.Consider use dict()***

##-----------------

def dictionary_squared(input):
	dictionary = {}
	for i in range(1, input + 1):
		dictionary[i] = i * i

	print(dictionary)

dictionary_squared(8)
