class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        set<int> numSet;
		
		for(int i=0; i< nums.size(); i++){
			int num = nums[i];
			if(numSet.count(num)){
				return true;
			}else{
				numSet.insert(num);
			}
		}
		return false;
    }
};