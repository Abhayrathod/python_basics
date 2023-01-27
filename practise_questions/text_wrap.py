# hackerank

import textwrap

# def wrap(string, max_width):
#     return textwrap.fill(string, max_width)

# def wrap(string, max_width):
#     for i in range(1, len(string) // max_width + 1):
#         string = string[:i*max_width+i-1] + '\n' + string[i*max_width+i-1:]
#     return string

# def wrap(string, max_width):
#     res = list(textwrap.wrap(string,max_width))
#     return "\n".join(res)

def wrap(string, max_width):
    l=[]
    count=0
    for i in string:
        l.append(i)
        count+=1
        if count%max_width==0:
            l.append('\n')
            count=0
    return "".join(l)

if __name__ == '__main__':
    # string, max_width = input(), int(input())
    string = "ABCDEFGHIJKLIMNOPQRSTUVWXYZ"
    max_width = 4
    result = wrap(string, max_width)
    print(result)