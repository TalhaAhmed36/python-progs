from math import*
#Here the parameters for numerical integration are defined
N = int (input ("Enter how many times you want to sum (more times = more accurate):"))
a=float (input ("Enter the lower integration bound:"))
b=float (input ("Enter the upper integration bound:"))

#This is the integration function which performs the integration
def Integrate(N, a, b):
    def f(x):
        #type your function after return
        return x**2
    value=0
    value2=0
    for n in range(1,N+1):
        value += f(a+ ((n-(1/2))* ((b-a)/N)))
    value2= ((b-a)/N)*value
    return value2

#Outputs including the integration value:
print("")
print("Here is your answer:")
print (Integrate(N, a, b))


