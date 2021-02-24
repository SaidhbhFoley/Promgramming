# Programme that puts 10 random numbers into a queue
# Then outputs all the values in the queue
# Then take thenumbers from the queue one at a time
# Print it and the current numbers stillin the queue
# Author: Saidhbh Foley

import random
queue = []
numberofNumbers = 10
rangeTo = 100

for n in range (0, numberofNumbers):
    queue.append(random.randint(0, rangeTo))
print ("queue is {}" .format(queue))

while len(queue) !=0:
    currentNumber = queue.pop(0)
    print ("current Number is {} and the queue is {}" .format(currentNumber, queue))

print ("the queue is now empty")