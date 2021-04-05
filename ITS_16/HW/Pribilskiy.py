import json

ERR_MSG = {
    'stack_full': 'stack is full',
    'stack_no_full': 'stack is not full',
    'stack_empty': 'stack is empty',
    'stack_no_empty': 'stack is not empty',
    'stack_cls': 'stack is cleared'
}


class Stack:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"'name': '{self.name}', 'age': {self.age}"


class StackList:

    def __init__(self):
        self._stack_list = []
        self.stack_size = 5

    def __str__(self):
        result = ''
        for i in range(len(self._stack_list)):
            result += f"{self._stack_list[i]} \n"
        return result

    def push(self, *new_cat):
        if self.stack_size != len(self._stack_list):
            new_cat = Stack(new_cat[0], new_cat[1])
            self._stack_list.append(new_cat)
        else:
            print(ERR_MSG['stack_full'])

    def pop(self):
        if len(self._stack_list) != 0:
            pop_cat = self._stack_list[-1]
            del self._stack_list[-1]
            return pop_cat
        else:
            print(ERR_MSG['stack_empty'])

    def count(self):
        return f'{len(self._stack_list) + 1} cat\'s in stack'

    def is_empty(self):
        if len(self._stack_list) == 0:
            return ERR_MSG['stack_empty']
        else:
            return ERR_MSG['stack_no_empty']

    def is_full(self):
        if len(self._stack_list) + 1 == self.stack_size:
            return ERR_MSG['stack_full']
        else:
            return ERR_MSG['stack_no_full']

    def clear(self):
        self._stack_list = []
        return ERR_MSG['stack_cls']

    # def serialize_json(self):
    #     stack_list_str = dict()
    #     for i in range(len(self._stack_list)):
    #         stack_list_str[i] = dict(str(self._stack_list[i]))
    #
    #     return json.dumps(stack_list_str)


if __name__ == '__main__':
    stack_list = StackList()
    stack_list.push("Tom", 3)
    stack_list.push("Jim", 5)
    stack_list.push("Ojjy", 8)
    stack_list.push("Jilly", 8)
    stack_list.push("Andy", 8)

    print(stack_list)
    print(stack_list.pop())
    print(stack_list.count())
    print(stack_list.is_empty())
    print(stack_list.is_full())
    # print(stack_list.clear())
    # print(type(stack_list.serialize_json()), stack_list.serialize_json())

