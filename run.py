'''
    This is the main entrance of the Quine-McCluskey program.
'''

from tools.utils import dec2bin_nosign, dec2bin_sign, bin2dec_nosign, bin2dec_sign

if __name__ == '__main__':
    bin_num = dec2bin_nosign(15)
    print(bin_num)
    print(bin2dec_nosign([1, 0, 1, 0, 0]))
