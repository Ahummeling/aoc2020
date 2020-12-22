import os
_ROOTDIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..')
infile = os.path.join(_ROOTDIR, 'input', '1.input')
outfile = os.path.join(_ROOTDIR, 'output', '1.out')
print(infile)
data = []
with open(infile, 'r') as file:
    [data.append(int(x.strip())) for x in file.readlines()]

for x in data:
    for y in data:
        if x == y:
            continue
        s = x + y
        z = 2020 - s
        if z in data:
            print(x, y, z)
            print('answer: {}'.format(x*y*z))
            exit(0)