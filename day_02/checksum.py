
def main():
    two_count, three_count = 0, 0
    a_code = ord('a')
    with open('./test_data.txt') as box_ids:
        for line in box_ids.readlines():
            freq_list = [0] * 26
            for char in line[:-1]:
                freq_list[ord(char)-a_code] += 1
            for freq in freq_list:
                if freq is 2:
                    two_count += 1
                    break
            for freq in freq_list:
                if freq is 3:
                    three_count += 1
                    break
    return two_count * three_count

if __name__ == '__main__':
    print(main())