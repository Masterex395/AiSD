from typing import Any


class Node:
    value: Any
    next: 'Node'

    def __init__(self, element, next=None):
        self.value = element
        self.next = next

class LinkedList:
    head: Node
    tail: Node

    def __init__(self):
        self.head = None
        self.tail = None

    def __len__(self):
        count = 0
        node = self.head
        while node != None:
            count += 1
            node = node.next
        return count

    def __str__(self):
        temp = ""
        pointer = self.head
        for x in range(len(self)):
            if pointer.next != None:
                temp += str(pointer.value) + " -> "
            if pointer.next == None:
                temp += str(pointer.value)
            pointer = pointer.next
        return temp

     # metoda push(self, value: Any) -> None umieści nowy węzeł na początku listy
    def push(self, element):
        self.head = Node(element, self.head)

     # metoda append(self, value: Any) -> None umieści nowy węzeł na końcu listy
    def append(self, element):
            if self.head == None:
                self.head = Node(element)
            else:
                pointer = self.head
                while pointer.next != None:
                    pointer = pointer.next
                pointer.next = Node(element)

     # metoda node(self, at: int) -> Node zwróci węzeł znajdujący się na wskazanej pozycji
    def node(self, at: int) -> Node:
        if at == len(self) - 1:
            node = self.tail
        if len(self) > at:
            node = self.head
            for x in range(at):
                node = node.next
        return node

    # metoda insert(self, value: Any, after: Node) -> None wstawi nowy węzeł tuż za węzłem wskazanym w parametrze
    def insert(self, value: Any, after: Node) -> None:
        if after == self.tail:
            self.append(value)
            return
        if after == None:
            return
        new_node = Node(value)
        new_node.next = after.next
        after.next = new_node

    # metoda pop(self) -> Any usunie pierwszy element z listy i go zwróci
    def pop(self) -> Any:
        if self.head == None:
            return None
        else:
            del_node = self.head
            self.head = del_node.next
            return del_node.value

    # metoda remove_last(self) -> Any usunie ostatni element z listy i go zwróci
    def remove_last(self) -> Any:
        node = self.node(len(self)-3)
        self.tail = node
        node = node.next
        del_last = node.next
        node.next = None
        return del_last.value

    # metoda remove(self, after: Node) -> Any usunie z listy następnik węzła przekazanego w parametrze
    def remove(self, after: Node) -> Any:
        node = self.head
        if after.next == self.tail:
            del_next = self.tail
            self.remove_last()
        else:
            while node.next != after:
                node = node.next
            del_next = node.next
            node.next = after.next
        return del_next


list_ = LinkedList()
assert list_.head == None
print(list_)

list_.push(1)
list_.push(0)
assert str(list_) == '0 -> 1'
print(list_)

list_.append(9)
list_.append(10)
assert str(list_) == '0 -> 1 -> 9 -> 10'
print(list_)

middle_node = list_.node(at=1)
list_.insert(5, after=middle_node)
assert str(list_) == '0 -> 1 -> 5 -> 9 -> 10'
print(list_)

first_element = list_.node(at=0)
returned_first_element = list_.pop()
assert first_element.value == returned_first_element

last_element = list_.node(at=3)
returned_last_element = list_.remove_last()
assert last_element.value == returned_last_element

assert str(list_) == '1 -> 5 -> 9'
print(str(list_))

second_node = list_.node(at=2)
list_.remove(second_node)
assert str(list_) == '1 -> 5'
print(str(list_))