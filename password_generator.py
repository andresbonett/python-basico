import random


def password_generator():
    upper = ('A','B', 'C', 'D', 'E', 'F','G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z')
    lowel = ('a','b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
    symbol = ('!','#', '$', '%', '@', '?', '_', '-')
    number = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')
    characters = upper + lowel + symbol + number
    random_password = []

    for i in range(15):
        random_char = random.choice(characters)
        random_password.append(random_char)
        del i
        
    random_password = ''.join(random_password)
    return random_password
    

def main():
    password = password_generator()
    print("New password generated: " + password)


if __name__ == "__main__":
    main()