## 介绍：
树是数据结构中非常重要的一种，主要的用途是用来提高查找效率，对于要重复查找的情况效果更佳，如二叉排序树、FP-树。另外可以用来提高编码效率，如哈弗曼树。
![2chashu](https://raw.githubusercontent.com/xdnh/Algorithm_python/master/pic/%E4%BA%8C%E5%8F%89%E6%A0%91.jpg)
## 代码：
用python实现树的构造和几种遍历算法，把代码作了一下整理总结。实现功能：
- 树的构造
- 递归实现先序遍历、中序遍历、后序遍历
- 堆栈实现先序遍历、中序遍历、后序遍历
- 队列实现层次遍历
```python
# coding=utf-8


class Node(object):
    """"节点类"""
    def __init__(self, elem=-1, lchild=None, rchild=None):
        self.elem = elem
        self.lchild = lchild
        self.rchild = rchild


class Tree(object):
    """树类"""
    def __init__(self):
        self.root = Node()
        self.myQueue = []
        self.a = 0

    def add(self, elem):  # 按层生成树
        """为树添加节点"""
        node = Node(elem)
        if self.root.elem == -1:  # 如果树是空的，则对根节点赋值
            self.root = node
            self.myQueue.append(self.root)
        else:
            treeNode = self.myQueue[0]   # 此结点的子树还没有齐
            if treeNode.lchild is None:
                treeNode.lchild = node
                self.myQueue.append(treeNode.lchild)
            else:
                treeNode.rchild = node
                self.myQueue.append(treeNode.rchild)
                self.myQueue.pop(0)  # 如果该结点存在右子树，将此结点丢弃

    def front_digui(self, root):
        """利用递归实现树的先序遍历"""
        if root is None:
            return
        print(root.elem)
        self.front_digui(root.lchild)
        self.front_digui(root.rchild)

    def front_digui_sum(self, root):
        """赋值求和"""
        if root is None:
            return
        self.a += root.elem
        self.front_digui_sum(root.lchild)
        self.front_digui_sum(root.rchild)
        return self.a

    def sum_front_digui(self, root):
        """递归求和"""
        if root is None:
            return 0
        return root.elem + self.sum_front_digui(root.lchild) + self.sum_front_digui(root.rchild)

    def middle_digui(self, root):
        """利用递归实现树的中序遍历"""
        if root is None:
            return
        self.middle_digui(root.lchild)
        print(root.elem)
        self.middle_digui(root.rchild)

    def later_digui(self, root):
        """利用递归实现树的后序遍历"""
        if root is None:
            return
        self.later_digui(root.lchild)
        self.later_digui(root.rchild)
        print(root.elem)

    def front_stack(self, root):
        """利用堆栈实现树的先序遍历"""
        if root is None:
            return
        myStack = []
        node = root
        while node or myStack:
            while node:  # 从根节点开始，一直找它的左子树
                print(node.elem)
                myStack.append(node)
                node = node.lchild
            node = myStack.pop()  # while结束表示当前节点node为空，即前一个节点没有左子树了
            node = node.rchild

    def middle_stack(self, root):
        """利用堆栈实现树的中序遍历"""
        if root is None:
            return
        mystack = []
        node = root
        while node or mystack:  # 从根节点开始，一直找它的左子树
            while node:
                mystack.append(node)
                node = node.lchild
            node = mystack.pop()  # while结束表示当前节点node为空，即前一个节点没有左子树了
            print(node.elem)
            node = node.rchild   # 开始查看它的右子树

    def later_stack(self, root):
        """利用堆栈实现树的后序遍历"""
        if root is None:
            return
        mystack1 = []
        mystack2 = []
        node = root
        mystack1.append(node)
        while mystack1:  # 这个while循环的功能是找出后序遍历的逆序，存在myStack2里面
            node = mystack1.pop()
            if node.lchild:
                mystack1.append(node.lchild)
            if node.rchild:
                mystack1.append(node.rchild)
            mystack2.append(node)
        while mystack2:   # 将myStack2中的元素出栈，即为后序遍历次序
            print(mystack2.pop().elem)

    def level_queue(self, root):
        """利用队列实现树的层次遍历"""
        if root is None:
            return
        myqueue = []
        node = root
        myqueue.append(node)
        while myqueue:
            node = myqueue.pop(0)
            print(node.elem)
            if node.lchild is not None:
                myqueue.append(node.lchild)
            if node.rchild is not None:
                myqueue.append(node.rchild)


if __name__ == "__main__":
    """主函数"""
    elems = range(10)
    tree = Tree()  # 新建一个树对象
    for elem in elems:
        tree.add(elem)  # 按层逐个添加树的节点

    print("前序遍历树节点并求和")
    count = tree.sum_front_digui(tree.root)
    cnt = tree.front_digui_sum(tree.root)
    print(cnt)
    print(count)
    print("\n\n递归实现前序遍历：")
    tree.front_digui(tree.root)
    print('\n\n递归实现中序遍历:')
    tree.middle_digui(tree.root)
    print("\n\n递归实现后序遍历:'")
    tree.later_digui(tree.root)

    print('\n\n堆栈实现先序遍历:')
    tree.front_stack(tree.root)
    print('\n\n堆栈实现中序遍历:')
    tree.middle_stack(tree.root)
    print('\n\n堆栈实现后序遍历:')
    tree.later_stack(tree.root)

    print('队列实现层次遍历:')
    tree.level_queue(tree.root)


```
## 参考网址：
* [python实现二叉树和它的七种遍历](https://blog.csdn.net/Bone_ACE/article/details/46718683)
* [二叉树的遍历(python实现)](https://blog.csdn.net/xxm524/article/details/50768610)
