# Caesar Cipher Problem form HackerRank.com #

# Julius Caesar protected his confidential information by encrypting it using a cipher. 
# Caesar's cipher shifts each letter by a number of letters. If the shift takes you past 
# the end of the alphabet, just rotate back to the front of the alphabet. In the case 
# of a rotation by 3, w, x, y and z would map to z, a, b and c.

# Original alphabet:      abcdefghijklmnopqrstuvwxyz
# Alphabet rotated +3:    defghijklmnopqrstuvwxyzabc

def caesarCipher(s, k):
    encryption = ""
    for i in range(len(s)):
        char = s[i]
        if char.isupper():
            translation = chr(((ord(char) - 65) + k) % 26 + 65)
        elif char.islower():
            translation = chr(((ord(char) - 97) + k) % 26 + 97)
        else:
            translation = char
        encryption += translation
    return encryption

if __name__ == '__main__':
    print('Testing function...')
    assert caesarCipher('middle-Outz', 2) == 'okffng-Qwvb'
    assert caesarCipher('Always-Look-on-the-Bright-Side-of-Life', 5) == 'Fqbfdx-Qttp-ts-ymj-Gwnlmy-Xnij-tk-Qnkj'
    print('Tests completed with no errors')