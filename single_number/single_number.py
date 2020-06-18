'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    # Your code here
    # dup_list = []
    # temp_list = []
    # final_list = []
    # [temp_list.append(num) for num in arr if num not in temp_list]
    # create empty list?
    #iterate through list

    # for num in arr:
    #     if num not in temp_list:
    #         temp_list.append(num)
    #     else:
    #         dup_list.append(num)

        
    #compare elements to find duplicates
    #return non-duplicate
    return 2 * sum(set(arr)) - sum(arr)



if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]
    # arr = [2,1,2]

    print(f"The odd-number-out is {single_number(arr)}")