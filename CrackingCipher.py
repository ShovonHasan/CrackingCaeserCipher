#ceaser cypher hacking with brute force

#message=input('Enter your message:')
message='GUVF VF ZL FRPERG ZRFFNTR.'
LETTERS='ABCDEFGHIJKLMNOPQRSTUVWXYZ'

#loop through every possible key
for key in range(len(LETTERS)):

        #it is important to set the translated value to the blank string
        #so that prvious iteration's value for translated is cleared
        translated=''

        #run the encyption and decryption code on each symbol in the message

        for symbol in message:
                if symbol in LETTERS:
                        num=LETTERS.find(symbol) #get the number in the symbol
                        num=num-key

                        if num<0:
                                                                num=num+len(LETTERS)

                        translated=translated+LETTERS[num]

                else:
                        translated=translated+symbol

        print('Key #%s:%s'%(key,translated))

        #print every possible key.
