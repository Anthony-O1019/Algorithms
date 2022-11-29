# Exercise 1: Calculate the multiplication and sum of two numbers
# Given two integer numbers return their product only if the product is equal to or lower than 1000, else return their sum.

def numbers(x,y):
    result = x * y
    if result < 1000:
        return result
    else:
        return x + y


print(numbers(59,62))

# Exercise 2: Print the sum of the current number and the previous number
# Write a program to iterate the first 10 numbers and in each iteration, print the sum of the current and previous number.

def current():
    x = 0
    y = 0
    while x in range(10):
        print(" Current number for X is " + str(x) + " The current number for Y is " + str(y))
        y = x
        x = x+1

current()

# Write a program to accept a string from the user and display characters that are present at an even index number. For example, str = "pynative" so you should display ‘p’, ‘n’, ‘t’, ‘v’.

def even(word):
    size = len(word)
    print("The string is " + str(word) + " and the length of this is " + str(size) )

    for x in range(0, size -1, 2):
        print("This following letter " + word[x] + " is in an even location within the word")

even("Absolutely")

def remove_char(word, x):
    y = word [x:]
    if x > len(word):
        print("Need to choose a smaller number buddy!")
    else:
        print("The Word is " + word + " but this is the Word " + y + " without the first few letters")

remove_char("Sarcasm", 4)