import os
_ROOTDIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..')
infile = os.path.join(_ROOTDIR, 'input', '1.input')
outfile = os.path.join(_ROOTDIR, 'output', '1.out')
print(infile)
data = []
with open(infile, 'r') as file:
    [data.append(int(x.strip())) for x in file.readlines()]

with open(outfile, 'w') as file:
    [file.write(str(x*(2020-x))) and exit(0) for x in data if 2020 - x in data]
