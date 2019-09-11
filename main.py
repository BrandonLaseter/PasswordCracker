import crypt
import sys
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
    file = open(filepath)
    lines = file.read().split("\n")
    file.close

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

shadowfilepath = sys.argv[1]
passwordfilepath = sys.argv[2]

print ("Shadow file path " + shadowfilepath)
print ("Password file path " + passwordfilepath)

#list = ReadPasswordFile("/home/blaseter/Documents/Dev/Python/PasswordCracker/listopass.txt")
list = ReadPasswordFile(passwordfilepath)
#IterateShadowFile("/home/blaseter/Documents/Dev/Python/PasswordCracker/Passwords.txt", list)
IterateShadowFile(shadowfilepath, list)
print ("Done")

