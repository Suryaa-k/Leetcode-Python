from collections import defaultdict, deque

class Solution:
    def remainingMethods(self, n: int, k: int, invocations: list[list[int]]) -> list[int]:
        graph = defaultdict(list)
        for a, b in invocations:
            graph[a].append(b)

        suspicious = set()
        queue = deque([k])
        while queue:
            node = queue.popleft()
            if node in suspicious:
                continue
            suspicious.add(node)
            for nb in graph[node]:
                if nb not in suspicious:
                    queue.append(nb)

        for a, b in invocations:
            if a not in suspicious and b in suspicious:
                return list(range(n))

        return [m for m in range(n) if m not in suspicious]