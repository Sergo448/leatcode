"""
TASK

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
"""


# Wrong
def isValid_wrong0(s: str) -> bool:
    for i in range(0, len(s)):
        if s[i] == '(':
            if s[i + 1] != ')':
                return False
        elif s[i] == '{':
            if s[i + 1] != '}':
                return False
        elif s[i] == '[':
            if s[i + 1] != ']':
                return False
    return True


def isValid_wrong1(s: str) -> bool:
    res: dict = {'(': 0, ')': 0, '{': 0, '}': 0, '[': 0, ']': 0}

    for i in range(0, len(s)):
        if s[i] == '(':
            res[s[i]] += 1
        elif s[i] == ')':
            res[s[i]] += 1
        elif s[i] == '{':
            res[s[i]] += 1
        elif s[i] == '}':
            res[s[i]] += 1
        elif s[i] == '[':
            res[s[i]] += 1
        elif s[i] == ']':
            res[s[i]] += 1

    elems_1 = res['('] + res[')']
    elems_2 = res['{'] + res['}']
    elems_3 = res['['] + res[']']
    if (elems_1 % 2 != 0) or (elems_2 % 2 != 0) or (elems_3 % 2 != 0):
        return False
    else:
        return True


def isValid(s: str) -> bool:
    '''
    Function to pair if sequence contains valid parenthesis
    :param s: Sequence of brackets
    :return: True is sequence is valid else False
    '''
    stack = []
    opening = set('([{')  # Список открывающихся скобок
    closing = set(')]}')  # Список закрывающихся скобок
    pair = {')': '(',
            ']': '[',
            '}': '{'}  # Пары, для выделения тех скобок из списка, которые закрываются
    for i in s:
        if i in opening:  # Если скобка в открывающимся списке добавляем ее в список
            stack.append(i)
        if i in closing:  # Если в закрывающимся и ее нет в списке, то ложь
            see1 = pair[i]
            if not stack:
                return False
            elif stack.pop() != pair[i]:  # Если удаленная последняя скобка из списка не равна ее паре, то ложь
                return False
            else:
                continue
    if not stack:  # Если список пустой - все скобки верно открыты и закрыты. Иначе ложь
        return True
    else:
        return False


def isValid_my(sequince: str) -> bool:
    opening_set = set('({[')
    closing_set = set(')}]')
    pairs: dict = {
        ')': '(',
        '}': '{',
        ']': '['
    }

    result: list = []
    for elem in sequince:
        if elem in opening_set:
            result.append(elem)
        if elem in closing_set:
            if not result:
                return False
            elif result.pop() != pairs[elem]:
                return False
            else:
                continue

    if not result:
        return True
    else:
        return False


print(isValid(s="(]))"))
print(isValid(s="()[]{}"))
print(isValid_my(sequince="()"))
print(isValid(s="({[][]})"))
print(isValid_my(sequince="()(){{}}([({})])"))
print(isValid(s="()(){{}}([({}])"))
