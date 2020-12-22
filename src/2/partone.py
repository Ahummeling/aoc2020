import os
_ROOTDIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..')
infile = os.path.join(_ROOTDIR, 'input', '2.input')
outfile = os.path.join(_ROOTDIR, 'output', '2.out')
print(infile)
data = []
with open(infile, 'r') as file:
    [data.append(x.strip()) for x in file.readlines()]


print('got {} lines'.format(len(data)))


def is_valid(line):
    r, l, pw = line.split(' ')
    a, b = r.split('-')
    a = int(a) + 1
    b = int(b) + 1
    try:
        A = pw[a] is l[0]
        B = pw[b] is l[0]
        return (A and not B) or (not A and B)
    except IndexError:
        return False


cnt = 0
for li in data:
    if is_valid(li):
      cnt = cnt + 1

print(cnt)
