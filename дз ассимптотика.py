def palindrome(str):
    if str[::-1] == str:
        print('True')
    else:
        print('False')
    print(str)

palindrome('helloworld')