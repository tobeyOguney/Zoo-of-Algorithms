# Solves the underscorify substring problem


def collapse_locations(locations):
    new_locations = []

    i = 0
    while i < len(locations):
        current = locations[i]

        j = i+1
        while j < len(locations) and (locations[j][0] == current[1] or locations[j][0] == current[1]-1):
            current[1] = locations[j][1]
            j += 1
        
        new_locations.extend(current)
        i = j

    return new_locations        



def get_locations(main_string, substring):
    locations = []
    i = 0
    
    while True:
        next = main_string.find(substring, i)

        if next != -1:
            locations.append([next, next + len(substring)])
            i = next+1

        else:
            break
    
    return collapse_locations(locations)

def underscorify_substring(main_string, substring):
    idxs = get_locations(main_string, substring)
    new_string = ""
    for i in range(len(main_string)):
        if i in idxs:
            new_string += "_"
        new_string += main_string[i]
    return new_string


if __name__ == "__main__":
    res = underscorify_substring(
        "testthis is a testtest to see if testestest it works","test"
    )

    assert res == "_test_this is a _testtest_ to see if _testestest_ it works", res

    print("You're all set!")