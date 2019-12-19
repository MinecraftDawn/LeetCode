class Solution {
public:
    int computeArea(int A, int B, int C, int D, int E, int F, int G, int H) {
        long allArea = (long)(C-A)*(D-B) + (G-E)*(H-F);
		long overW = max(0L, min(C,G) - (long)max(A,E));
        long overH = max(0L, min(D,H) - (long)max(B,F));
		return allArea - overW*overH;
    }
};