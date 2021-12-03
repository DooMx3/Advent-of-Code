def take_input():
    line = input()
    input_list = list()
    while line:
        command, value = line.split(' ')
        input_list.append((command, int(value)))
        line = input()
    return input_list


def compute(input_list):
    x_pos = 0
    depth = 0
    aim = 0
    for command, value in input_list:
        match command:
            case 'forward':
                x_pos += value
                depth += aim * value
            case 'up':
                aim -= value
            case 'down':
                aim += value
    return x_pos, depth


def main():
    list_input = take_input()
    x_pos, depth = compute(list_input)
    print(x_pos * depth)

if __name__ == '__main__':
    main()
