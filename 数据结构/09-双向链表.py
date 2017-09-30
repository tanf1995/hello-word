class Node(object):
    def __init__(self, elem=-1, next=None, previous=None):
        self.elem = elem
        self.next = next
        self.previous = previous

class DleLinkList(object):
    def __init__(self, head=None):
        self.head = head

    # 尾部插入节点
    def add(self, elem):
        node = Node(elem)

        if self.head == None:
            self.head = node
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = node
        node.previous = cur

    # 遍历
    def travel(self):
        cur = self.head
        if cur == None:
            print('链表为空！')
            return

        while cur:
            print(cur.elem, end='--')
            cur = cur.next
        print('\n遍历结束')

    # 返回链表长度
    def length(self):
        count = 0
        if not self.head:
            print('链表长度为0')
            return
        else:
            count += 1
            cur = self.head
            while cur.next:
                count += 1
                cur = cur.next
            return count

    # 插入节点
    def insert(self, pos, elem):
        node = Node(elem)
        if pos <= 0:
            node.next = self.head
            self.head.previous = node
            self.head = node
        elif pos >= self.length():
            self.add(elem)
        else:
            cur = self.head
            for i in range(1, pos):
                cur = cur.next
            node.next = cur.next
            node.previous = cur
            cur.next = node

    # 删除节点
    def remove(self, ele):
        cur = self.head
        pre = None
        while cur:
            if cur.elem == ele:
                if not pre:
                    self.head = cur.next
                    cur.next.previous = self.head
                else:
                    pre.next = cur.next
                    cur.next.previous = pre
                print('删除节点成功！')
                break
            else:
                pre = cur
                cur = cur.next

    # 查询节点是否存在
    def search(self, elem):
        cur = self.head
        while cur:
            if cur.elem == elem:
                return True
            else:
                cur = cur.next




link1 = DleLinkList()
link1.add(1)
link1.add(2)
link1.add(4)
link1.add(2)
link1.add(3)
link1.travel()

link1.insert(0, 8)
link1.travel()
link1.insert(10, 12)
link1.travel()

link1.insert(5, 15)
link1.travel()

link1.insert(-1, 30)
link1.travel()

link1.remove(1)
link1.travel()

res = link1.search(1)
if res:
    print('节点存在')
else:
    print('节点不存在')

length = link1.length()
print('链表长度为%d'%length)