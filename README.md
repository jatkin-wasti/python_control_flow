# This lesson will cover control flow
## If statements, Elif, and Else statements
## For loops and While loops
- ```break``` will stop the loop
- ```continue``` will immediately start the next iteration of the loop
### For loops
- Will loop through data for a set range
- The maximum number of loops is defined before it is run
- 
### While loops
- Will continue looping through data until a certain condition is met
- Useful for continuously prompting a user
- Can be problematic if 
- ```break``` and ```continue``` can be used to control the flow of the loop
- Not regularly used however it can be useful for monitoring
- Syntax for a while loop is while condition:   e.g. while number < 10:
- Task: Take user input with while loop
- isdigit() checks if the input is all digits
```
user_prompt = True
while user_prompt:  # Continues to loop until user_prompt is set to False
    age = input("Please enter your age:  ")  # Receives user's age
    if age.isdigit() and int(age) < 117:  # Checks if the user's age is a number or a reasonable value
        user_prompt = False  # If they have input a satisfactory age we can end the loop
    else:  # Otherwise we should continue looping
        print("Please provide age in digits")  # Prompt the user to input a more satisfactory value
print(f"Your age is {age}")  # Outputs their age 
```
- Task: Create a while loop
```
number = 0  # Defining the number variable
while number < 10:  # Checking a condition and running until the number is 10 or above
    print(f"It's working --> {number}")  # Prints out a string containing the current value of number
    if number == 4:  # Checks if the number is currently 4
        break  # If so it breaks out of the loop
    number += 1  # Iterate the number variable
```