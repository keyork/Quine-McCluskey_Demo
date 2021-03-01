'''
    This is the main entrance of the  Quine-McCluskey program.
'''

from tools.dec2bin import dec2bin

if __name__ == '__main__':
    bin_num = dec2bin(20)
    print(bin_num)
