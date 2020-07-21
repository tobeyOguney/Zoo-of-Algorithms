# Solves the smallest substring containing problem


def get_count_map(string_):
    count_map = dict()

    for char in string_:
        count_map[char] = count_map.get(char, 0) + 1

    return count_map

# O(m+s) time | O(m+s) space
def smallest_substring_containing(main_string, substring):
    substring_table = get_count_map(substring)
    solution_pairs = []
    
    left = 0
    right = 0
    substring_char_count = 0
    memo_table = {char: 0 for char in substring}

    while right < len(main_string):
        if substring_char_count < len(memo_table):
            if main_string[right] in memo_table:
                memo_table[main_string[right]] += 1
                
                if memo_table[main_string[right]] == substring_table[main_string[right]]:
                    substring_char_count += 1
            
            right += 1
            
        else:
            solution_pairs.append([left, right])

            if main_string[left] in memo_table:
                memo_table[main_string[left]] -= 1
                substring_char_count -= 1

            left += 1
    
    solution_idxs = min(solution_pairs, key=lambda item: item[1]-item[0])

    return main_string[solution_idxs[0]: solution_idxs[1]]


if __name__ == "__main__":
    res = smallest_substring_containing(
        "abcd$ef$axb$c$", "$$abf"
    )

    assert res == "f$axb$", res

    print("You're all set!")