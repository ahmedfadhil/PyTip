def main():
    # List of string
    list1 = ['Hi', 'hello', 'at', 'this', 'there', 'from']

    # List of string
    list2 = ['there', 'hello', 'Hi']

    '''    
            check if list1 contains all elements in list2
        '''
    result = all(elements in list1 for elements in list2)
    result2 = any(elements in list1 for elements in list2)

    if result:
        print("it contains all")
    else:
        print("it does not contain all")

    if result2:
        print("it contains some")
    else:
        print("it does not contain some")


if __name__ == '__main__':
    main()
