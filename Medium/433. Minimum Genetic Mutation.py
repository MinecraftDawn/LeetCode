from collections import defaultdict, deque


class Solution:
    def minMutation(self, start: str, end: str, bank: list) -> int:
        if end not in bank: return -1

        queue = deque()
        myDict = defaultdict(set)

        for gene in bank:
            for i in range(len(start)):
                myDict[gene[:i] + "?" + gene[i + 1:]].add(gene)

        for i in range(len(start)):
            for gene in myDict[start[:i] + "?" + start[i + 1:]]:
                queue.append((gene, {gene}))

        while queue:
            for _ in range(len(queue)):
                gene, preVisited = queue.popleft()
                visited = preVisited.copy()
                visited.add(gene)

                if gene == end: return len(visited)

                for i in range(len(start)):
                    for nxtGene in myDict[gene[:i] + "?" + gene[i + 1:]]:
                        if nxtGene not in visited:
                            queue.append((nxtGene, visited))

        return -1