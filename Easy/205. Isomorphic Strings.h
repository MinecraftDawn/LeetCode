class Solution {
public:
    bool isIsomorphic(string s, string t) {
        if(s.length() != t.length()){return false;}

		std::unordered_map<char,char> map1;
		std::unordered_map<char,char> map2;
		
		for(int i=0;i<s.length(); i++){
			if(map1.count(s[i])){
				if(map1[s[i]] != t[i]){
					return false;
				}
				
			}else{
				map1[s[i]] = t[i];
			}
			if(map2.count(t[i])){
				if(map2[t[i]] != s[i]){
					return false;
				}
				
			}else{
				map2[t[i]] = s[i];
			}
		}
		return true;
    }
};