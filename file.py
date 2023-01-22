import re

class File: 

    def file_print(self):
        with open("test.txt", "r+") as file1:
            # Reading from a file
            print(file1.read())

    def file_read(self):
        with open("test.txt", "r+") as file1:
            # Reading from a file
            return file1.read()

    def no_lines_to_file(self, file):
        with open('output.txt', 'x') as f:
            f.write(file.replace('\n\n','\n'))
        print(file.replace('\n\n','\n'))