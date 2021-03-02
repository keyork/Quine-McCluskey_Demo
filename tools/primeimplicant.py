'''

'''
import decbin

def search_prime_implicant(dec_list):
    for dec_num in dec_list:
        bin_num = decbin.dec2bin_nosign(dec_num)
        one_time = bin_num.count(1)
        print(one_time)










# debug
if __name__ == '__main__':
    search_prime_implicant([4,8,9,10,12,11,14,15])