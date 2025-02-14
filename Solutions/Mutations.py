#Solution 1: Using Indexing and Slicing
def mutate_string(string, position, character):
    string = string[:position] + character + string[position+1:]
    return string

if __name__ == '__main__':




#Solution 2: Convert the string to a list, then change the character at that position, then use .join method to join the string and return it

def mutate_string(string, position, character):
    l = list(string)
    l[position] = character
    string = ''.join(l)
    return string

if __name__ == '__main__':
