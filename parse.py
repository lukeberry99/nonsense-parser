import sys

with open(sys.argv[1], 'r') as file:
    sorted_data=sorted(file.readlines(),
            key=lambda item: int(item.split(' ', 1)[0].strip()))

    f = open('sorted.txt', 'w')
    for line in sorted_data:
        f.write(line)
    f.close()
print "Saved to sorted.txt"
