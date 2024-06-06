import requests
import string
import random
import argparse
import sys
import time

# Color snippets
black="\033[0;30m"
red="\033[0;31m"
bred="\033[1;31m"
green="\033[0;32m"
bgreen="\033[1;32m"
yellow="\033[0;33m"
byellow="\033[1;33m"
blue="\033[0;34m"
bblue="\033[1;34m"
purple="\033[0;35m"
bpurple="\033[1;35m"
cyan="\033[0;36m"
bcyan="\033[1;36m"
white="\033[0;37m"
nc="\033[00m"

def get_random_string(length):  # Letters and numbers
    pool = string.ascii_lowercase + string.digits
    return ''.join(random.choice(pool) for _ in range(length))

def get_random_text(length):  # Chars only
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(length))

def generate():
    nick = get_random_text(8)
    passw = get_random_string(12)
    email = f"{nick}@{get_random_text(5)}.com"

    headers = {
        "Accept-Encoding": "gzip",
        "Accept-Language": "en-US",
        "App-Platform": "Android",
        "Connection": "Keep-Alive",
        "Content-Type": "application/x-www-form-urlencoded",
        "Host": "spclient.wg.spotify.com",
        "User-Agent": "Spotify/8.6.72 Android/29 (SM-N976N)",
        "Spotify-App-Version": "8.6.72",
        "X-Client-Id": get_random_string(32)
    }
    
    payload = {
        "creation_point": "client_mobile",
        "gender": "male" if random.randint(0, 1) else "female",
        "birth_year": random.randint(1990, 2000),
        "displayname": nick,
        "iagree": "true",
        "birth_month": random.randint(1, 11),
        "password_repeat": passw,
        "password": passw,
        "key": "142b583129b2df829de3656f9eb484e6",
        "platform": "Android-ARM",
        "email": email,
        "birth_day": random.randint(1, 20)
    }
    
    r = requests.post('https://spclient.wg.spotify.com/signup/public/v1/account/', headers=headers, data=payload)

    if r.status_code == 200:
        if r.json()['status'] == 1:
            return True, f"{nick}:{r.json()['username']}:{email}:{passw}"
        else:
            return False, "Could not create the account, some errors occurred"
    else:
        return False, f"Could not load the page. Response code: {r.status_code}"

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Spotify Account Generator")
    parser.add_argument("-n", "--number", help="How many accounts to generate, default is 1", type=int, default=1)
    parser.add_argument("-o", "--output", help="Output file, default prints to the console", type=str)
    args = parser.parse_args()

    N = args.number
    output_file = args.output

    if output_file:
        file = open(output_file, "a")
    else:
        file = sys.stdout
    
    time.sleep(1)
    input(f"{bred}Benvenuto/a su SP GENERATOR, Premi invio per continuare...{nc}")
    time.sleep(1)
    print(f'''{byellow}

╔═╗╔═╗  ╔═╗╔═╗╔╗╔╔═╗╦═╗╔═╗╔╦╗╔═╗╦═╗
╚═╗╠═╝  ║ ╦║╣ ║║║║╣ ╠╦╝╠═╣ ║ ║ ║╠╦╝
╚═╝╩    ╚═╝╚═╝╝╚╝╚═╝╩╚═╩ ╩ ╩ ╚═╝╩╚═
                       	     [v1.0]
                       [By Volpino]

https://github.com/volpinottv
{nc}''')
    time.sleep(1)
    print(f"{bred}Generating Accounts...{nc}\n", file=sys.stdout)
    time.sleep(5)
    input(f"{bcyan}Accounts Generated, Premi invio per continuare...{nc}\n")
    
    for i in range(N):
        result = generate()
        if result[0]:
            nick, username, email, password = result[1].split(":")
            print(f"{bcyan}NICKNAME: {bpurple}{nick}{nc}\n{bcyan}USERNAME: {bpurple}{username}{nc}\n{bcyan}E - MAIL: {bpurple}{email}{nc}\n{bcyan}PASSWORD: {bpurple}{password}{nc}\n", file=sys.stdout)
            if file is not sys.stdout:
                print(result[1], file=file)
        else:
            print(f"{i+1}/{N}: {result[1]}", file=sys.stdout)
    
    if output_file:
        file.close()
