from collections import deque


def reverse(queue: deque) -> deque:
    new_q = deque()
    while queue:
        new_q.append(queue.pop())
    [queue.append(d) for d in new_q]


if __name__ == "__main__":
    q = deque()
    q.append(1)
    q.append(2)
    q.append(3)
    q.append(4)
    print(reverse(q))
