from bot import input_birthday
error_count = 0

# open files to read correct birthday and secret
f = open('data/birthday.txt','r')
secret_bday = f.readline()
f.close()

f = open('data/secret.txt','r')
secret = f.readline()
f.close()

print("You only get 3 attempts to enter your birthday")
while(error_count < 3):
    user_input = input("Please input your birthday to reveal your secret letter.")
    bot_result = input_birthday(user_input=user_input)
    
    # if correct format:
    if bot_result[0] == 'Y':
        bot_result = bot_result[3:]
        if bot_result == secret_bday:
            print(secret)
            break
        else: 
            print("incorrect birthday, no secret for you")
    
    #ambiguous date
    elif bot_result[0] == 'A':
        bot_result = bot_result[3:]
        print(bot_result)
            
    # incorrect format
    elif bot_result[0] == 'N':
        print(bot_result[3:]) 

    # unknown output from bot
    else:
        print("unknown bot output" + bot_result)
    
    error_count += 1

if error_count > 2:
    print("3 incorrect attempts -> secret will no longer be revealed.")