# Solves the balanced bracket problem


# O(n) time | O(n) space
def balanced_brackets(string_):
    stack = []
    brackets = {"{":"}", "[":"]", "(":")"}

    for char in string_:
        if char in brackets:
            stack.append(char)
        
        else:
            if brackets[stack.pop()] != char:
                return False
    
    return True


if __name__ == "__main__":
    assert balanced_brackets("([])(){}(())()()") == True

    print("You're all set!")