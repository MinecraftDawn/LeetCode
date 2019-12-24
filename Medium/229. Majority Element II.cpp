class Solution {
public:
    vector<int> majorityElement(vector<int>& nums) {
        int bound = nums.size()/3;
		unordered_set<int> found;
		unordered_map<int,int> numDict;
		
		for(int &num : nums){
			if(numDict.count(num)){
				numDict[num] +=1;
			}else{
				numDict[num] = 1;
			}
			if(numDict[num] > bound){
				found.insert(num);
			}
		}
		return vector<int>(found.begin(),found.end());
    }
};