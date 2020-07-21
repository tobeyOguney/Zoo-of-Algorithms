# Solves the apartment hunting problem


# O(b) time | O(b) space 
def get_priority_memo(priority, blocks):
    htbl = dict()

    for i in range(len(blocks)):
        if blocks[i][priority]:
            htbl[0] = [i, 'right']
            break
    
    for i in range(1, len(blocks)):
        if blocks[i][priority]:
            htbl[i] = [0, 'self']
        
        elif i+1 < len(blocks) and blocks[i+1][priority]:
            htbl[i] = [1, 'right']
        
        elif blocks[i-1][priority]:
            htbl[i] = [1, 'left']
        
        else:
            temp = htbl[i-1]

            if temp[1] == "left":
                htbl[i] = [temp[0]+1, "left"]

            elif temp[1] == "right":
                htbl[i] = [temp[0]-1, "right"]
    
    return [htbl[i][0] for i in range(len(blocks))]

# O(br) time | O(br) space
def apartment_hunting(blocks, priorities):
    priority_memos = [get_priority_memo(priority, blocks) for priority in priorities]
    memo = []

    for i in range(len(blocks)):
        memo.append(max([priority_memo[i] for priority_memo in priority_memos]))
    
    return min(enumerate(memo), key=lambda item: item[1])[0]


if __name__ == "__main__":
    res = apartment_hunting(
        [
            {
            "gym": False,
            "school": True,
            "store": False,
            },
            {
            "gym": True,
            "school": False,
            "store": False,
            },
            {
            "gym": True,
            "school": True,
            "store": False,
            },
            {
            "gym": False,
            "school": True,
            "store": False,
            },
            {
            "gym": False,
            "school": True,
            "store": True,
            },
        ],
        ["gym","school","store"]
    )

    assert res == 3, res

    print("You're all set!")