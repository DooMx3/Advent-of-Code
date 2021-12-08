def take_input():
    line = input()
    values = list()
    while line:
        values.append(line)
        line = input()

    return values


def common_bit(values, index):
    bit_sum = 0
    for value in values:
        bit_sum += int(value[index])

    if 2 * bit_sum >= len(values):
        return True
    elif 2 * bit_sum < len(values):
        return False


def check_bits(values):
    gamma_rate = ""
    epsilon_rate = ""
    for index in range(len(values[0])):
        bit = common_bit(values, index)
        gamma_rate += str(int(bit))
        epsilon_rate += str(int(not bit))
    return gamma_rate, epsilon_rate


def life_support(values):
    index = 0
    oxygen = values.copy()
    while len(oxygen) > 1:
        c_bit = int(common_bit(oxygen, index))
        func = lambda x: int(x[index])==c_bit
        oxygen = list(filter(func, oxygen))
        index += 1

    index = 0
    co2 = values.copy()
    while len(co2) > 1:
        c_bit = int(not common_bit(co2, index))
        func = lambda x: int(x[index])==c_bit
        co2 = list(filter(func, co2))
        index += 1
        
    return oxygen[0], co2[0]


def main():
    values = take_input()
    gamma_rate, epsilon_rate = check_bits(values)
    answer = int(gamma_rate, 2) *  int(epsilon_rate, 2)
    print(answer)


def main2():
    values = take_input()
    oxygen, co2 = life_support(values)
    print(int(oxygen, 2), int(co2, 2))
    answer = int(oxygen, 2) * int(co2, 2)
    print(answer)


if __name__ == '__main__':
    main2()
