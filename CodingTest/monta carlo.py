
import random

def monta_carlo_pi(num_samples):
    inside_circle =0
    for _ in range(num_samples):
         x,y = random.random() , random.random()
         if x**2 + y**2 <=1:
             inside_circle +=1

    pie = 4* (inside_circle/num_samples)
    return pie

print(monta_carlo_pi(1000000))


