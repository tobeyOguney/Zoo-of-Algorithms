# Solves the pattern matcher problem


# O(nm) time | O(1) space
def find_all_idxs(sub_string, main_string):
    yielded = False
    for i in range(len(main_string) - len(sub_string)):
        match = True

        for j in range(len(sub_string)):
            if sub_string[j] != main_string[j+i]:
                match = False
                break

        if match:
            yielded = True
            yield i
    
    if not yielded:
        yield -1

# O(n^2 * m) time | O(n) space
def pattern_matcher(pattern, main_string):
    first = pattern[0]
    second = "y" if first == "x" else "x"
    pattern_map = dict()

    for i in range(1, len(main_string)):
        pattern_map.clear()
        pattern_map = {first: main_string[:i]} 
        pattern_pointer = 1
        j = i

        is_first_validated = True
        while pattern[pattern_pointer] == first and j+len(pattern_map[first]) < len(main_string):
            if pattern_map[first] != main_string[j : j+len(pattern_map[first])]:
                is_first_validated = False
                break
            
            else:
                pattern_pointer += 1
                j += len(pattern_map[first])
        
        if not is_first_validated or pattern[pattern_pointer] == first:
            continue

        next_first_idxs = find_all_idxs(pattern_map[first], main_string)
        next_first_idx = None
        for _ in range(pattern_pointer+1):
            next_first_idx = next(next_first_idxs)

        if next_first_idx == -1:
            pattern_map[second] = main_string[j:next_first_idx]

        else:
            second_count = pattern.find(first, pattern_pointer) - pattern_pointer
            second_strip_length = next_first_idx - j
            pattern_map[second] = main_string[j : j+second_strip_length//second_count]
        
        potential_match = ''
        for char in pattern:
            potential_match += pattern_map.get(char, '')

        if potential_match == main_string:
            return [pattern_map[first], pattern_map[second]]
    
    return []


if __name__ == "__main__":
    res = pattern_matcher(
        "xxyxxy","gogopowerrangergogopowerranger"
    )

    assert res == ["go","powerranger"], res

    print("You're all set!")