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
            if ltr in alpha:
                cntr = alpha.index(ltr)
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
            if ltr in alpha:
                cntr = alpha.index(ltr)
                if (cntr - key) < -26:
                    module = (cntr - key) % (len(alpha))
                    y2 += alpha[0 + module]
                else:
                    y2 += alpha[cntr - key]
            elif ltr == " ":
               y2 += " "
        print("Here's your decoded message: \n" + y2)
