#------------------------------------------------
# Homework 3 of course "Python for Research"
# HarvardX -  PH526xEdX, EdX
# Cipher
#------------------------------------------------

#Exercise 1--------------------------------------
# Let's look at the lowercase letters.
import string
alphabet=' '+string.ascii_lowercase

#Exercise 2--------------------------------------
# Create a dictionary  with keys alphabet and values positions
positions={alphabet[i]: i for i in range(0,len(alphabet))} #key=alphabet[i], value=i
positions.items()
positions.values()

#Exercise 3--------------------------------------
# shift message by one in alphabet
message = "hi my name is caesar"
shift=1
encoded_message=''
#1. for loop that calls the position of each character in message and increments it by one
for i in range(len(message)):
    #find the value of each letter
    pos_message=positions[message[i]]
    new_pos_message=pos_message+shift
    new_pos_message=new_pos_message%(len(alphabet))

    #2.Using these incremented positions as indices of alphabet,
    #  you will recover the correct encoded character of the message!

    #get the new keys for the shifted values = new_pos_message
    onekey = [key  for (key, value) in positions.items() if value == new_pos_message]
    onekey=''.join(onekey) #transforms list in string
    #print(message[i], onekey,pos_message,new_pos_message)
    encoded_message=encoded_message+onekey

#print(encoded_message)
#Tutorial on dictionaries
#https://developers.google.com/edu/python/dict-files

#Exercise 4--------------------------------------
def encoding(message,shift):
    encoded_message=''
    #1. for loop that calls the position of each character in message and increments it by one
    for i in range(len(message)): #here we loop over values! much better to loop over the characters
    #see alternative solution below)
        pos_message=positions[message[i]]
        new_pos_message=pos_message+shift
        new_pos_message=new_pos_message%(len(alphabet))
        onekey = [key  for (key, value) in positions.items() if value == new_pos_message]
        onekey=''.join(onekey) #transforms list in string
        #print(message[i], onekey,pos_message,new_pos_message)
        encoded_message=encoded_message+onekey
    return(encoded_message)

encoded_message=encoding(message,3)
print(encoded_message)

#Alternative (more elegant) solution as provided by lecture:
#values are directly given in dictionary!
#loop over characters (which are also the keys in the dictionary position)
def encoding(message,key):
    encoding_list = []
    for char in message: #loop over characters= loop over keys of dictionary
        position = positions[char] #gives value of key "char"
        encoded_position = (position + key) % len(alphabet)
        encoding_list.append(alphabet[encoded_position])
        encoded_string = "".join(encoding_list) #transform list in strings seperated by nothing
    return(encoded_string)

encoded_message=encoding(message,3)
print(encoded_message)

#Exercise 5
decoded_message = encoding(encoded_message,-3)
# print your decoded message here!
help(list)
