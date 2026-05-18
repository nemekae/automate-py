# A simple login app using username and password.

while True:
    print('Welcome! lets log you in😊')
    name = input('username: > ')
    if name != 'nemekae':
        continue
    print(f"Welcome {name}! what is your password?")
    passwd = input('password: > ' )
    if passwd == 'swordfish':
        print(f"Access granted {name}. Let's begin.")
        break
