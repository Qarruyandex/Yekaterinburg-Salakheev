string = input()
while len(string) >= 1:
    if string[0] == '-':
        c = 0
        while string[c] == '-':
            c = c + 1
        print('-' * c, end='')
        cc = 0
        while string[c + cc] == '>':
            cc = cc + 1
            if c + cc >= len(string):
                break
        print('>' * cc, end='')
        print()
        string = string[c + cc:]
    else:
        c = 0
        while string[c] == '<':
            c = c + 1
        print('<' * c, end='')
        if string.find("<", c) < 0:
            if string.find(">", c) < 0:
                print('-' * (len(string) - c))
                break
            else:
                cc = 0
                while string[c + cc] == '-':
                    cc = cc + 1
                print('-' * (cc - 1), end='')
                print()
                string = string[c - 1 + cc:]
        else:
            if string.find(">", c) < 0:
                cc = 0
                while string[c + cc] == '-':
                    cc = cc + 1
                print('-' * cc, end='')
                print()
                string = string[cc + c:]
            else:
                if string.find(">", c) < string.find("<", c):
                    cc = 0
                    while string[cc + c] == '-':
                        cc = cc + 1
                    print('-' * (cc - 1), end='')
                    print()
                    string = string[c - 1 + cc:]
                else:
                    cc = 0
                    while string[cc + c] == '-':
                        cc = cc + 1
                    print('-' * cc, end='')
                    print()
                    string = string[cc + c:]