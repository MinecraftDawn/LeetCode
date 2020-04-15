class Solution {
public:
    int maxEnvelopes(vector<vector<int>>& envelopes) {
        if(envelopes.size() < 2) return envelopes.size();

		sort(envelopes.begin(), envelopes.end());
		int ans = 1;
		int dp[envelopes.size()];
		for(int i = 0; i < envelopes.size(); i++) dp[i] = 1;

		for(int i = 0; i < envelopes.size(); i++){
			for(int j = 0; j < i; j++){
				if(envelopes[i][0] > envelopes[j][0] && envelopes[i][1] > envelopes[j][1]){
					dp[i] = max(dp[i], dp[j]+1);
				}

			}
			ans = max(ans, dp[i]);
		}

		return ans;
    }
};