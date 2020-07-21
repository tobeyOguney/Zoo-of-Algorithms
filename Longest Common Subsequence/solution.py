# Solves the longest common subsequence problem

def long_comm_sub(first_string, second_string):
    # Adjust both strings for memo table offset
    first_string = "*" + first_string
    second_string = "*" + second_string

    # Implement minified memo table
    memo = [
        ["" for _ in range(len(first_string))] for _ in range(2)
    ]

    for i in range(1, len(second_string)):
        temp = ""

        for j in range(1, len(first_string)):
            if first_string[j] == second_string[i]:     # Coincidence check
                temp = first_string[j]
            
            memo[1][j] = memo[0][j] + temp
        
        # print(memo[1])  # View memo table

        memo[0] = list(memo[1]) # Create space for next row in minified memo table

    return list(memo[-1][-1])


if __name__ == "__main__":
    res = long_comm_sub("ZXVVYZW", "XKYKZPW")

    assert res == ["X", "Y", "Z", "W"], res

    print("You're all set!") 