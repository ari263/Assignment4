x = input('Enter text to write to the file: ')

file1 = open('output.txt', 'w')
file1.write(x+'\n')

print('Data successfully written to output.txt.\n')
file1.close()

y = input('Enter additional text to append: ')
file2 = open('output.txt', 'a')
file2.write(y)

print('Data successfully appended.\n')
file2.close()

file3 = open('output.txt', 'r')
output_txt = file3.read()

print('Final content of output.txt:')
print(output_txt)
file3.close()
