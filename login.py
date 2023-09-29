
def paswrd (password):
    if len(password) < 8 :
        print('your pasword should 8 char')
    elif password.isnumeric():
        print('your pass should one letter')
    elif password.isalpha():
        print('your pass has one number ')
    else :
        print('yes , your password is correct')
    
while True :
    passsword = input('plz enter your password : ')
    paswrd(passsword)