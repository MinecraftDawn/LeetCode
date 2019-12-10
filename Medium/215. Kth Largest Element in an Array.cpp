class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        std::sort(nums.begin(), nums.end());
		std::reverse(nums.begin(), nums.end());
		return nums[k-1];
    }
};