def decode(message):
    '''
    Decodes a specific encoded message that is provided with the accompanying text file
    The key has been solved before programming to taylor the program to this encoded message.
    '''
    # Key for this specific encoded message
    # This is a substitution cypher
    substitution = ['X', 'T', 'W', 'D', 'V', 'Q', 'Z', 'L', 'S', 'O', 'N', 'B', 'A', 'U', 'G', 'H', 'K', 'E', 'P', 'Y', 'R', 'C', 'I', 'F', 'M', 'J']
    decrypted_message = ""

    # Go through each character in message string
    for char in message:

        # If character is a letter and also not a space
        # substitute the letter with the key
        if char.isalpha() and char != ' ':
            decrypted_message += substitution[ord(char) - ord('a')]
        else:
            # continue with array if it is not a letter or it is a space
            decrypted_message += char

    print(decrypted_message)

# Create empty string called message to store characters
# letters array with 26 spaces, all filled with a value of 0
# it will keep track of the frequency of the letters of the cypher text
message = ""
letters = [0] * 26

# Open the text file
# Go through each line, and each character in each line
# check if the character is a letter, then add the lowercase letter to an empty string called text
with open("cypher.txt", "r") as fs:
    lines = fs.readlines()
    text = ""
    for line in lines:
        message += line
        for char in line:
            if char.isalpha():
                text += char.lower()

# For each character in text, compute the frequency of the letters in the encoded message
# take each character in text string and subtract 'a'
# this corresponds to each letters position in the letters array
# Ex: letters[0] = a, letters[1] = b
for char in text:
    letters[ord(char) - ord('a')] += 1

# Print out the frequency of the letters in the encoded message
for i in range(26):
    out = chr(i + ord('a'))
    print(out + ": " + str(letters[i]))

decode(message)