# file management
# open with name and way to open it
# the mode to open is optional, by default it is 'r'
# (read)
# we can specity 'w': if the file does not exist
# in the specific path, it is created
# If the file exists it is overwritten

#open("file.txt") # this launches an exception of file not found
f = open("file.txt",'w+')
# r+ and w+ mean that the file is opened both for
# writing and for reading
# x return exception if the file that we want to create
# is already created (exclusive creation)
# a to append data

# we can open textual files .txt and .html 'rt' which coincides with 'r'
# and it is the default case
# binary files as .jpg and .mp3 'rb',...
#print(dir(f))

print(f.mode)
print(f.name)

if(f.writable()):
    print("The file is writable\n")
    f.write("Lorem ipsum dolor sit amet, consectetur adipiscing elit.\n")
f.close()

f = open("file.txt")
if(f.readable()):
    print("The file is readable\n")
    # we want to read the first 5 characters
    tmp = f.read(5)
    print(tmp)
f.close()

# we want to cancel the previous file, so we use 'w' and not 'a'
f = open("file.txt", 'w')
content = ['Nam pretium orci ante, eu vehicula justo sagittis nec.\n',
'Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; ',
'Donec pretium efficitur ornare. In condimentum tellus non nunc interdum varius.']
if(f.writable()):
    f.writelines(content)

f.close()

f = open("file.txt")
if(f.readable()):
    print("The file is readable\n")
    tmp = f.readlines()
    print(tmp)

    i = 0
    for line in content:
        print('line', i, line, "\n", sep=" ")
        i = i + 1

f.close()
