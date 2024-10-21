from bot import input_birthday
error_count = 0

secret_bday = "13/6/2000"

while(error_count < 3):
    user_input = input("Please input your birthday to reveal your secret letter.")
    bot_result = input_birthday(user_input=user_input)
    
    # if correct format:
    if bot_result[0] == 'Y':
        bot_result = bot_result[2:]
        if bot_result == secret_bday:
            print("reveal secret")
        else: 
            print("incorrect birthday, no secret for you")
            
    # incorrect format
    elif bot_result[0] == 'N':
        print(bot_result[2:]) 
    else:
        print("unknown bot output" + bot_result)
    
    error_count += 1
    
print("3 incorrect attempts -> secret will no longer be revealed.")

## Pass user input to bot + determine how bot output received.

# - set format: 
# if correct date format -> YES: <date>
# if incorrect date/format wrong -> NO: <feedback>