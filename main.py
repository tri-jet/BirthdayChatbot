from bot import input_birthday
error_count = 0

f = open('birthday.txt','r')
secret_bday = f.readline()

while(error_count < 3):
    user_input = input("Please input your birthday to reveal your secret letter.")
    bot_result = input_birthday(user_input=user_input)
    
    # if correct format:
    if bot_result[0] == 'Y':
        bot_result = bot_result[3:]
        if bot_result == secret_bday:
            print("reveal secret")
            break
        else: 
            print("incorrect birthday, no secret for you")
            
    # incorrect format
    elif bot_result[0] == 'N':
        print(bot_result[3:]) 
    else:
        print("unknown bot output" + bot_result)
    
    error_count += 1

if error_count > 2:
    print("3 incorrect attempts -> secret will no longer be revealed.")

## Pass user input to bot + determine how bot output received.

# - set format: 
# if correct date format -> YES: <date>
# if incorrect date/format wrong -> NO: <feedback>