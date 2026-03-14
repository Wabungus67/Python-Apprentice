"""
Below is the FizzBuzz Program from the earlier lesson. 
The rules for the program are: 

For the numbers from 1 to 30:

* If the number is evenly divisible by 5, print '🦡 badger'
* If the number is evenly divisible by 3, print '🍄 mushroom'
* If the number is evenly divisible by 15, print '🐍 snake!'
* If it is divisible by neither, print the number.

Your job is to modify only one line -- the one with range() 
-- so that the program only prints '🦡 badger'

Your program should print 4 badgers. 
"""
nums = range(0, 30)

for i in (nums[::5]): # Change only this line
    if (i) % 15 > 0:
    # Don't change anything below this line
        if i % 15 == 0:
            print(i, '🐍 snake!')
        elif i % 5 == 0:
            print(i, '🦡 badger')
        elif i % 3 == 0:
            print(i, '🍄 mushroom')
        else:
            print(i)

# hint: run the program once and look at the numbers that are printed.
# Maybe iterate over those numbers.