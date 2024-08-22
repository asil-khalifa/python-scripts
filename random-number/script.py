from time import time

a = 1664525
c = 1013904223
m = 2**32
counter = 8
def ran():
    global counter
    #Python's unix time has a 7 digit precision after decimal point, so multiply by 10^7 to use those numbers as well
    
    n = (time()*10**7)%(10**9)
    counter+=1
    if counter>15:
        counter = 8
    
    #divide by m to ensure number is in the range [0, 1)
    return ((a*counter*(n-1)+c)%m)/m

#Example:
print(ran())

#Loop Example:
for i in range(100):
    print(ran())