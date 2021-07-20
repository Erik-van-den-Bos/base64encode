"""encode data file to base64 string"""

radix64 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/='

def encode24bits(octets):
    """
    input : one, two or three octets
    output: four character base64 string
    """
    string = ''
    sextets = [64, 64, 64, 64]
    sextets[0] = octets[0] >> 2
    sextets[1] = (octets[0] & 3) << 4
    if len(octets) > 1:
        sextets[1] += octets[1] >> 4
        sextets[2] = (octets[1] & 15) << 2
        if len(octets) > 2:
            sextets[2] += octets[2] >> 6
            sextets[3] = octets[2] & 63
    for sextet in sextets:
        string += radix64[sextet]
            
    return string

def encodefile(filename):
    """
    input : filename
    output: b64_filename.txt
    """
    
    with open(filename, 'rb') as file:
        string = ''
        i = 0
        data = file.read(3)
        while data:
            string += encode24bits(data)
            if len(string[i:]) % 76 == 0:
                string += '\n'
                i = len(string)
            data = file.read(3)
        if string[-1] != '\n':
            string += '\n'

    if string:
        with open('b64_' + filename +'.txt', 'w') as file:
            file.write(string) # lines of 76 characters

def main():
    filename = input('Data file name: ')
    encodefile(filename)

if __name__ == '__main__': main()
