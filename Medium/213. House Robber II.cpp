class Solution {
public:
    int rob(vector<int>& nums) {
        if(nums.size() == 0) return 0;
		
		if(nums.size() <  2){
			return *std::max_element(nums.begin(), nums.end());
		}
		
		vector<int> left(&nums[0],&nums[nums.size()-1]);
		vector<int> right(&nums[1],&nums[nums.size()-0]);
		
		return std::max(notCircle(left), notCircle(right));
		
    }
	
	int notCircle(vector<int>& nums){
		int pre = 0, cur = 0;
		
		for(int i = 0; i < nums.size(); i++){
			int tmp = cur;
			cur = std::max(cur, nums[i] + pre);
			pre = tmp;
		}
		return cur;
	}
};