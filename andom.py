# factorial of given number
def factorial(n):
    print (n)
    # single line to find factorial
    return 1 if (n==1 or n==0) else n * factorial(n - 1);
    
 
# code to start factorial
num =10;
print("Factorial of",num,"is",factorial(num))
print('Hello world')
