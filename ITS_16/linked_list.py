# [1, ->] [2, ->]
# [<-, 1, ->], [<-, 2, ->]

from pprint import pprint


class Box:
    def __init__(self, cat=None):
        self.cat = cat
        self.next_cat = None

    def __str__(self):
        return f'{self.cat} -> {self.next_cat}'


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        result = ''
        lastbox = self.head
        while lastbox:
            result += f'{lastbox.__str__()} \n'
            lastbox = lastbox.next_cat
        return result

    def contains(self, cat):
        lastbox = self.head
        while lastbox:
            if cat == lastbox.cat:
                return True
            lastbox = lastbox.nextcat
        return False

    def add_to_end(self, newcat):
        newbox = Box(newcat)
        if self.head is None:
            self.head = newbox
            return
        lastbox = self.head
        while lastbox.next_cat:
            lastbox = lastbox.next_cat
        lastbox.next_cat = newbox

    def get(self, catIndex):
        lastbox = self.head
        box_index = 0
        while box_index <= catIndex:
            if box_index == catIndex:
                return lastbox.cat
            box_index += 1
            lastbox = lastbox.next_cat

    def remove_box(self, rmcat):
        headcat= self.head
        if headcat is not None:
            if headcat.cat == rmcat:
                self.head = headcat.next_cat
                headcat = None
                return
        while headcat is not None:
            if headcat.cat == rmcat:
                break
            lastcat = headcat
            headcat = headcat.next_cat
        if headcat == None:
            return
        lastcat.nextcat = headcat.nextcat
        headcat = None


new_linked_list = LinkedList()


new_linked_list.add_to_end('Jerry')
# print(new_linked_list)
new_linked_list.add_to_end('Mikky')

new_linked_list.add_to_end('Wikki')
print(new_linked_list)