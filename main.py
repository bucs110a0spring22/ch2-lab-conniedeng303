import random
#Part A
classes_per_week = 3

weeks = 16
classes = 5
tuition = 6000
cost_per_week = ((tuition / classes) / weeks)

cost_per_class = (cost_per_week / classes_per_week)

print("Cost per week:", cost_per_week)
print("The cost per class:", cost_per_class, type (cost_per_class))

#Part B
my_list = ["orange", "lemon", "apple", "banana", "coconut"]
print("The random fruit is",random.choice(my_list))

