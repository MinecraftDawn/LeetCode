class Solution {
public:
    bool containsNearbyDuplicate(vector<int>& nums, int k) {
        unordered_map<int,int> map;
		for(int i=0; i<nums.size(); i++){
			int num = nums[i];
			if(map.count(num) > 0){
				if(i - map[num] <= k){
					return true;
				}else{
					map[num] = i;
				}
			}else{
				map[num] = i;
			}
		}
		return false;
    }
};