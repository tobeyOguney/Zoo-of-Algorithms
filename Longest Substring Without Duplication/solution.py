# Solves the longest substring without duplication problem

# O(n) time | O(n) space
def long_sub_dup(string_):
    memo = [[1, 0, 1]]
    last_seen = {string_[0]: 0}

    for i in range(1, len(string_)):
        if string_[i] not in last_seen or last_seen[string_[i]] < memo[i-1][1]:
            last_seen[string_[i]] = i
            memo.append([
                memo[i-1][0] + 1,
                memo[i-1][1],
                i+1
            ])

        else:
            idx = last_seen[string_[i]]
            print(i, idx)
            last_seen[string_[i]] = i
            memo.append([
                i - idx,
                idx+1,
                i+1
            ])
    
    res = max(memo, key=lambda t: t[0])

    return string_[res[1] : res[2]]

if __name__ == "__main__":
    res = long_sub_dup("clementisacap")

    assert res == "mentisac", res

    print("You're all set!")
