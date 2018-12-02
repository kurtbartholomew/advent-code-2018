from functools import *

def func_main():
    result = 0
    with open('./test_data.txt') as frequencies:
        result = reduce(lambda result, line: result + int(line[1:len(line)-1]) if line[0] is '+'  else result - int(line[1:len(line)-1]), frequencies,0)
    return result

def main():
    result = 0
    with open('./test_data.txt') as frequencies:
        for line in frequencies.readlines():
            polarity = line[0]
            line_len = len(line)
            num = int(line[1:line_len-1])
            if(polarity is '-'):
                result -= num
            else:
                result += num
    return result

if __name__ == "__main__":
    freq = main()
    func_freq = func_main()
    assert freq == 587 
    assert func_freq == 587