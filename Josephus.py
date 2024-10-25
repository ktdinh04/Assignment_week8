class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
            new_node.next = self.head

    def get_winner(self, M):
        current = self.head
        while current.next != current:  # Chỉ còn một người trong vòng tròn
            # Di chuyển M-1 bước
            for _ in range(M - 1):
                current = current.next
            # Loại bỏ người tại vị trí hiện tại
            print(f"Loại bỏ người chơi {current.next.data}")
            current.next = current.next.next
            current = current.next  # Tiếp tục với người kế tiếp
        return current.data  # Người cuối cùng còn lại là người chiến thắng

def josephus_winner(N, M):
    circle = CircularLinkedList()
    for i in range(1, N + 1):
        circle.append(i)
    return circle.get_winner(M)
N = 5
M_values = [1, 2, 3]

for M in M_values:
    winner = josephus_winner(N, M)
    print(f"Với N = {N} và M = {M}, người chiến thắng là người chơi {winner}")