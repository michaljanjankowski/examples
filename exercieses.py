
#A script you are writting uses logaritmic functions from the math module.
#Implement the add_patch function that should add a log100 function to the math module.
#The log100 function should wrap the exiting math.log function so that it calculates a logarithm with a base od 100.
#For example, math.log100(10) is equivalent to math.log(10,100) and should return 0.5.



import math

class LogPatch:

    def add_patch():
        # Write the code that goes here
        def function(value):
            return (math.log(value,100))
        math.log100 = function

    pass


#Example case.
LogPatch.add_patch()
print(math.log100(10))


#Candies exercise
class Candies:

    @staticmethod
    def count_candies(start_amount,eat_each):
        candies_left = start_amount
        eat_amout = 0
        while (candies_left):

            if candies_left - eat_each >= 0:
                candies_left = candies_left - eat_each
                candies_left = candies_left + 1
                eat_amout = eat_amout + eat_each
                continue

            if candies_left == 1:
                eat_amout = eat_amout + 1
                break


        return eat_amout

print(Candies.count_candies(3,2))
print(Candies.count_candies(5,3))
