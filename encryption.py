print ('WELCOME TO CAESAR CIPHER PROGRAM!!!')

alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

password = input('What is your pass phrase in plain text? : ')
shift = int(input('type a number to: '))
algorithm = input('Choose the right action - "encrypt" or "decrypt":  ')

def caesar(phrase, amount, algo):

    output = " "

    if algo == "decrypt":
        amount *= -1
    
    for letter in phrase:
        if letter not in alphabets:
            output += letter
        else:
            transition = alphabets.index(letter) + amount
            transition %= len(alphabets)
            output += alphabets[transition]

    print(f'Here is your {algo} passphrase: {output}')


should_continue = True

while should_continue:
    password = input('What is your pass phrase in plain text? : ')
    shift = int(input('type a number to: '))
    algorithm = input('Choose the right action - "encrypt" or "decrypt":  ')

    caesar(phrase=password, amount=shift, algo=algorithm)

    restart = input("Type 'yes' if you want to go again. Otherwise, type 'no'. \n").lower()
    if restart == 'no':
        should_continue = False
        print("Goodbye!")
   
 