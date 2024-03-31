class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [[p,s] for p, s in zip(position, speed)]
        sorted_pair = sorted(pair)[::-1]
        stack = [(target - sorted_pair[0][0]) /  sorted_pair[0][1]]
        for p, s in sorted_pair:
            time = (target - p) / s
            if time <= stack[-1]:
                continue
            else:
                stack.append(time)

        return len(stack)
