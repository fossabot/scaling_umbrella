import argparse
parser = argparse.ArgumentParser()


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    return name


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    parser.add_argument('file1', help='first file to check')
    parser.parse_args()
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
