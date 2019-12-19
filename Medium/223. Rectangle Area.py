class Solution:
    def computeArea(self, A: int, B: int, C: int, D: int, E: int, F: int, G: int, H: int) -> int:
        allArea = (C-A)*(D-B) + (G-E)*(H-F)
        overW = max(0, min(C,G) - max(A,E))
        overH = max(0, min(D,H) - max(B,F))
        return allArea - overW * overH