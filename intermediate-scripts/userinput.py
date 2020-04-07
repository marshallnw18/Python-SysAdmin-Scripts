#!/usr/bin/env python3.6

def get_file_name(reprompt=False):
    if reprompt:
        print("Please enter a file name: ")
    
    #take user input for the filename and then strip whitespaces
    file_name = input("Destination file name: ").strip()

    #if no filename is given, reprompt the user for a filename
    return file_name or get_file_name(True)

file_name = get_file_name()

print(f"Please enter your content. Entering an empty line will write the content to {file_name}:\n")

#open the given filename and begin writing to it
with open(file_name, 'a') as f:
    eof = False
    lines = []

    while not eof:
        line = input()

        #if a line is given as input, strip it and append to the list 'lines'
        if line.strip():
            lines.append(f"{line}\n")
        #if no input is given, consider it to be the end of input 
        else:
            eof = True
    
    #write lines to the given file once input has completed
    f.writelines(lines)
    print(f"Lines written to {file_name}")

