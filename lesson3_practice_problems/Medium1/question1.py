#-The Flintstones Rock! print ten times with an added '-' each time.

def hypthenate(string):
    hyphen = ''
    runner = 0
    while runner < 10:
        hyphen += '-'
        print(f'{hyphen}{string}')
        runner += 1

hypthenate('The Flintstones Rock')

#alt:

for padding in range(1, 11):
    print(f'{"-" * padding}The Flintstones Rock!')