import random

p = 0.5
max_unanswered_calls = 4
max_nr_days = 100

successes = 0
for d in range(max_nr_days):
    if random.random() > p and random.random() > p and random.random() > p and random.random() > p and random.random() <= p:
        successes += 1

print(successes/max_nr_days)
    
        
            
