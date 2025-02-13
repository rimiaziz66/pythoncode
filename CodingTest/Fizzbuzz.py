'''Question: Print numbers from 1 to 100. For multiples of 3,
print "Fiz  z"; for multiples of 5, print "Buzz"; and for multiples of both, print "FizzBuzz"'''

def fizzbuzz(n):

    for i in range(1,n+1):
        if i % 3 == 0 and i% 5 == 0:
            print("fizzbuzz")
        elif i% 3 == 0:
            print("fizz")
        elif i% 5 == 0:
            print("Buzz")
        else:
            print(i)


fizzbuzz(10)