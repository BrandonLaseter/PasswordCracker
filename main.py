import crypt
from hmac import compare_digest as compare_hash

def CheckValues(text, original_hash):
    new_hash = crypt.crypt(text, original_hash)
    results = compare_hash(original_hash, new_hash)
    return results

def ReadPasswordFile(filepath):
    print("opening " + filepath)
    file = open(filepath)
    list = file.read().split("\n")
    print (str(len(list)) + " passwords loaded")
    file.close()
    return list

def IterateShadowFile(filepath, passwords):
    file = open(filepath) #need to close)
    lines = file.read().split("\n")

    for line in lines:
        if line == "":
            continue 

        items = line.split(":")
        username = items[0]
        old_hash = items[1]

        for pw in passwords:
            if(CheckValues(pw, old_hash)):
                print("Password for " + username + " is " + pw)
                break
    file.close

list = ReadPasswordFile("/home/blaseter/Documents/Dev/Python/PasswordCracker/listopass.txt")
IterateShadowFile("/home/blaseter/Documents/Dev/Python/PasswordCracker/Passwords.txt", list)
print ("Done")

