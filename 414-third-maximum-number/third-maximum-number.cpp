class Solution {
public:
    int thirdMax(vector<int>& nums) {
        set<int> sortedNums;
        for (int &num : nums) {
            if (sortedNums.count(num)) continue;
            if (sortedNums.size()==3){
                if (*sortedNums.begin()<num){
                    sortedNums.erase(sortedNums.begin());
                    sortedNums.insert(num);
                }    
            } 
            else {
                sortedNums.insert(num);
            }
        }
        if (sortedNums.size()==3) {
            return *sortedNums.begin();
        }
        return *sortedNums.rbegin();
    }
};