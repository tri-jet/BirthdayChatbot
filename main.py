from bot import input_birthday
error_count = 0

while(error_count < 3):
    user_input = input("Please input your birthday to reveal your secret letter.")
    input_birthday(user_input=user_input)
    # send data to bot
    # if correct format:
        # check if matches birthday.txt
    
    # else: error_count += 1, 
    print("done")
    error_count = 3

## Pass user input to bot + determine how bot output received.

# - set format: 
# if correct date format -> YES: <date>
# if incorrect date/format wrong -> NO: <feedback>