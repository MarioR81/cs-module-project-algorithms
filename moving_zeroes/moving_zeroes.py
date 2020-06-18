'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    # Your code here
    #iterate through list
    for num in arr:
        if num == 0:
            # print(num)
            arr.append(num)
            del arr[arr.index(0)]
    return arr[0:]
        
    #compare element to zero
    #zeros have indez changed to list length(-1)


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")