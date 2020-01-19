class Solution {
public:
	unordered_map<int,int> dict;

    int numSquares(int n) {
		if(n <= 3) return n;

        int square = int(sqrt(n));
		int minNum = n;
		for(int i=square; i>1; i--){
			int num = n - i*i;

			int value;
			if(dict.count(num) > 0){
				value = dict[num];
			}else{
				value = numSquares(n - i*i);
				dict[num] = value;
			}
			minNum = min(minNum, value);
		}

		return minNum + 1;
    }
};