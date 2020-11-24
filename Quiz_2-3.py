# Kyle Bautista (AMDG) 11/24/2020

word_1 = input("What 3 directions would you like the robot to go?: ")
word_1 = word_1.lower()
word_lst = list(word_1)

word_2 = input("Whats another 3 directions you would like the robot to go? ")
word_2 = word_2.lower()
word_lst2 = list(word_2)

print("The directions for the robot are {0}, {1}." .format(word_1, word_2))
