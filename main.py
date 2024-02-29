def main():
    user_input = input("Input: ")
    print("Output: ", end='')
    for char in user_input:
        if char.lower() == 'a' or char.lower() == 'e' or char.lower() == 'i' or \
                char.lower() == 'o' or char.lower() == 'u':
            pass
        else:
            print(char, end='')


main()
