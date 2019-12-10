class Solution {
public:
	vector<vector<int>> ans;
	
    vector<vector<int>> combinationSum3(int k, int n) {
        dfs(k, n, vector<int>(), 1);
		return ans;
    }
	
	void dfs(int k, int curNum, vector<int> usedNum, int start){
		if(k == 0){
			if(curNum == 0){
				ans.push_back(usedNum);
			}
		}else{
			for(int i = start; i<10; i++){
				if(curNum - i >= 0){
					usedNum.push_back(i);
					dfs(k-1, curNum-i, usedNum, i+1);
					usedNum.pop_back();
				}
			}
		}
	}
};