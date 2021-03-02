'''
    tools
'''

def dec2bin_sign(dec_num):
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

def dec2bin_nosign(dec_num):
    bin_num = []
    if dec_num > 0:
        dec_num = int(dec_num)
        while True:
            if dec_num == 0:
                break
            curr_bin = dec_num % 2
            bin_num.append(curr_bin)
            dec_num = int(dec_num / 2)
    elif dec_num < 0:
        print('Input Error!!!')
    bin_num.reverse()
    return bin_num

def bin2dec_sign(bin_num):
    dec_num = 0
    length = len(bin_num)
    if bin_num[0] == 1:
        is_negative = True
        bin_num[0] = 0
    else:
        is_negative = False
    for i in range(length):
        dec_num += bin_num[i] * 2 ** (length - 1 - i)
        if is_negative:
            dec_num = -dec_num
    return dec_num

def bin2dec_nosign(bin_num):
    dec_num = 0
    length = len(bin_num)
    for i in range(length):
        dec_num += bin_num[i] * 2 ** (length - 1 - i)
    return dec_num