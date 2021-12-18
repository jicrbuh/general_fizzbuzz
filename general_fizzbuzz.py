import argparse
END_INT = 100


def main():
    parser = argparse.ArgumentParser(description="A general fizzbuzz. Takes 2 integers as input")
    parser.add_argument('integers', metavar='N', type=int, nargs='*', default=[3, 5],
                        help='two integers for fizzbuzz')

    args = parser.parse_args()

    if len(args.integers) != 2:
        print("You must provide either two integers or none")
        return

    fizz_int, buzz_int = args.integers
    print("general fizz buzz with: ", args.integers)
    for i in range(1, END_INT+1):
        print_msg = ''
        if i % fizz_int == 0:
            print_msg = 'fizz'
        if i % buzz_int == 0:
            print_msg = print_msg + 'buzz'
        if not print_msg:
            print_msg = str(i)
        print("{}: {}".format(i, print_msg))


if __name__ == "__main__":
    main()
