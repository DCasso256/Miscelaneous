'''
This code encrypts and decrypts messages using a substitution method,
which consists on shifting each letter a certain number of places (defined by
a key), up or down the english alphabet depending on the selected action,
it will only work with positive keys.
'''

alpha = "abcdefghijklmnopqrstuvwxyz"
key = 30
class caesar:
    global alpha
    global key
    def __init__(self, phrase):
        self.phrase = phrase.casefold()
    def encrypt(self):
        y2 = ""
        for ltr in self.phrase:
            cntr = 0
            while ltr != " " and ltr != alpha[cntr]:
                cntr +=1
            if ltr == alpha[cntr]:
                if (cntr + key) > 25:
                    module = (cntr + key) % (len(alpha))
                    if (cntr + module) > 25:
                        foo = cntr - module
                        y2 += alpha[cntr - foo]
                    else:
                        y2 += alpha[module]
                else:
                    y2 += alpha[cntr + key]
            else:
                y2 += " "
        print("Here's your coded message: \n" + y2 )
    def decrypt(self):
        y2 = ""
        for ltr in self.phrase:
            cntr = 0
            while ltr != alpha[cntr] and ltr != " ":
                cntr += 1
            if ltr == alpha [cntr]:
                if (cntr - key) < -26:
                    module = (cntr - key) % (len(alpha))
                    y2 += alpha[0 + module]
                else:
                    y2 += alpha[cntr - key]
            elif ltr == " ":
               y2 += " "


        print("Here's your decoded message: \n" + y2)

x = input("Send 'e' to encrypt or 'd' to decrypt your message: \n").casefold()

if x == "e":
    y = input ("Send your message: \n")
    cyph = caesar(y)
    cyph.encrypt()
elif x == "d":
    y = input("Send your message:\n")
    cyph = caesar(y)
    cyph.decrypt()