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