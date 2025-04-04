try:
    file1 = open("sample.txt", 'r')

    line = file1.readline()
    line_number = 1

    print('Reading file content:')

    while line != '':
        print("line {}: {}".format(line_number, line), end="")
        line_number += 1
        line = file1.readline()

    file1.close()
except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found.")
