#include <algorithm>
using namespace std;
class Solution {
public:
    bool isPalindrome(int x) {
        if (x<0 || (x%10==0 && x!=0)) return false;
        string s=to_string(x);
        int l=0,r=s.size()-1;
        while (l<=r){
            if (s[l]!=s[r]) return false;
            l+=1;
            r-=1;
        }
        return true;
    }
};