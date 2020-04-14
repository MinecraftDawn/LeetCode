class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int,int> map;
		vector<int> ans;
		
		for(int i = 0;i < nums.size(); i++){
			int num = nums[i];
			map[num] = i;
		}
		
		for(int i = 0;i < nums.size(); i++){
			int num = nums[i];
			if(map.count(target-num) > 0 && map[target-num] != i){
				ans.push_back(i);
                ans.push_back(map[target-num]);
				return ans;
			}
		}
        return ans;
    }
};