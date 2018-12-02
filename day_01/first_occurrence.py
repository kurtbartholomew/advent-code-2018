
def main():
    result = 0
    freqs = set()
    freqs.add(result)
    lines = None
    with open('./test_data.txt') as freq_changes:
        lines = freq_changes.readlines()

    found = False
    while not found:
        for line in lines:
            polarity = line[0]
            line_len = len(line)            
            num = int(line[1:line_len-1])
            result += (num if polarity == '+' else -num)
            if result in freqs:
                found = True
                break
            else:
                freqs.add(result)
            print(result)
    return result

if __name__ == "__main__":
   print(main())