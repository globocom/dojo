class LinkedListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.root = None

    def append(self, val):
        node = LinkedListNode(val) # 3
        if self.root is None:
            self.root = node
            return

        nn = self.root
        while nn.next is not None:
            nn = nn.next

        nn.next = node

    def __str__(self):
        output = ""

        nn = self.root
        while nn is not None:
            output += f" -> {nn.val}"
            nn = nn.next

        return output[4:]

    def __repr__(self):
        return self.__str__()




def main():
    return True

# X -> X -> X


# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.

# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]

# [9,9,9,9,9,9,9]
# [9,9,9,9]
# ans = array1[i] + array2[i] + resto
# restor = array1[i] + array2[i] + resto%10

# carreira -> Lara -> Willian
# implementar lista ligada
#     class, append, print
# func solver problem