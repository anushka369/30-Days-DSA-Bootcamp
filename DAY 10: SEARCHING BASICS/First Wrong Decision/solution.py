def FirstWrongDecision(s):
    # Iterate through the string to find first 'W'
    for i in range(len(s)):
        if s[i] == 'W':
            return i
          
    # If no 'W' found, return -1
    return -1

if __name__ == '__main__':
    str = input()
    # Call the function FirstWrongDecision()
    print(FirstWrongDecision(str))
