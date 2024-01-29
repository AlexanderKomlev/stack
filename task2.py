from stack import Stack


def is_balanced(example: str) -> bool:
    stack = Stack()

    couple = {
        ')': '(',
        '}': '{',
        ']': '['
    }

    for element in example:
        if element in ['(', '{', '[']:
            stack.push(element)
        elif element in [')', '}', ']']:
            if stack.size() == 0:
                return False
            elif stack.peek() == couple[element]:
                stack.pop()
            else:
                return False
    
    return True


if __name__ == "__main__":
    
    # balanced
    example1 = "(((([{}]))))"
    example2 = "[([])((([[[]]])))]{()}"
    example3 = "{{[()]}}"

    # unbalanced
    example4 = "}{}"
    example5 = "{{[(])]}}"
    example6 = "[[{())}]"

    for str in [example1, example2, example3, example4, example5, example6]:
        if is_balanced(str):
            print(f"{str} is balanced")
            print("============================")
        else:
            print(f"{str} is not balanced")
            print("============================")
