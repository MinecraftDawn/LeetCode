class Solution {
public:
    bool isHappy(int n) {
        std::unordered_map<int, bool> map;
        while (n) {
            if (map.find(n) == map.end()) {
                map.insert(std::pair<int,bool>(n,true));
            }else{
                return false;
            }

            int num = 0;
            while (n) {
                int forPow = n % 10;
                num += forPow * forPow;
                n /= 10;
            }
            n = num;

            if(num == 1){
                return true;
            }
        }
        return false;
    }
};
