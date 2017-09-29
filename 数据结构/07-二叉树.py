class Node(object):
    # 构造节点
    def __init__(self, elem=-1, lchild=None, rchild=None):
        self.elem = elem
        self.lchild = lchild
        self.rchild = rchild

class Tree(object):
    # 构造二叉树
    def __init__(self, root=None):
        self.root = root

    # 向树增加节点
    def addNode(self, elem):
        node = Node(elem)

        if self.root==None:
            self.root = node
            print('---add---%s' % node.elem)

        else:
            queue = []
            queue.append(self.root)

            while queue:
                cur = queue.pop(0)
                if cur.lchild==None:
                    cur.lchild = node
                    print('---add---%s'%node.elem)
                    return
                elif cur.rchild==None:
                    cur.rchild = node
                    print('---add---%s'%node.elem)
                    return

                else:
                    queue.append(cur.lchild)
                    queue.append(cur.rchild)

    # 先序遍历
    def first_traversal(self, node):
        if not node:
            return

        print(node.elem, end='--')
        self.first_traversal(node.lchild)
        self.first_traversal(node.rchild)

    # 中序遍历
    def second_traversal(self, node):
        if not node:
            return

        self.second_traversal(node.lchild)
        print(node.elem, end='--')
        self.second_traversal(node.rchild)

    # 后序遍历
    def final_traversal(self, node):
        if not node:
            return

        self.final_traversal(node.lchild)
        self.final_traversal(node.rchild)
        print(node.elem, end='--')

    # 广度遍历
    def breadth_traversal(self):
        if not self.root:
            return

        queue = []
        queue.append(self.root)
        while queue:
            cur = queue.pop(0)
            print(cur.elem, end='--')

            if cur.lchild:
                queue.append(cur.lchild)
            if cur.rchild:
                queue.append(cur.rchild)

    # 遍历
    def view_all(self):
        print('1.先序遍历')
        print('2.中序遍历')
        print('3.后序遍历')
        print('4.广度遍历')
        num = int(input('遍历方式->'))
        if num==1:
            self.first_traversal(self.root)
            print('')
        elif num==2:
            self.second_traversal(self.root)
            print('')
        elif num==3:
            self.final_traversal(self.root)
            print('')
        elif num==4:
            self.breadth_traversal()
        else:
            print('重新输入')

tree = Tree()
tree.addNode(1)
tree.addNode(2)
tree.addNode(3)
tree.addNode(5)
tree.addNode(4)
tree.addNode(6)

tree.view_all()



