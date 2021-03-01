'''
    This is a tools translate DEC Num to BIN num.
'''

def dec2bin(dec_num):
    bin_num = []
    if dec_num > 0:
        dec_num = int(dec_num)
        while True:
            if dec_num == 0:
                break
            curr_bin = dec_num % 2
            bin_num.append(curr_bin)
            dec_num = int(dec_num / 2)
        bin_num.append(0)
    elif dec_num < 0:
        dec_num = -dec_num
        dec_num = int(dec_num)
        while True:
            if dec_num == 0:
                break
            curr_bin = dec_num % 2
            bin_num.append(curr_bin)
            dec_num = int(dec_num / 2)
        bin_num.append(1)

    bin_num.reverse()
    return bin_num
