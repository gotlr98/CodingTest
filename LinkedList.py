# 코딩테스트 특강 복습

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):
        # 필요한 것 : 전체 갯수, head, tail, next
        init = Node('init')
        self.head = init
        self.tail = init

        self.cur = None
        self.nodeNum = 0
        
    def append(self, data):
        new_node = Node(data)
        self.tail.next = new_node
        self.tail = new_node
        self.nodeNum += 1

    def pop(self):
        self.cur = self.head
        while self.cur.next is not self.tail:
            self.cur = self.cur.next
        pop_val = self.cur.next.data
        self.cur.next = None
        self.nodeNum -= 1

        return pop_val
    
    def find(self, data):
        self.cur = self.head
        count = 0
        while True:
            if (self.cur.next.data == data):
                break
            self.cur = self.cur.next
            count += 1
        return count+1


l = LinkedList()
l.append(10)
l.append(20)
l.append(30)
l.append(40)
l.append(50)
print(l.find(50))



