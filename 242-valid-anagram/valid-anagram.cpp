#include <algorithm>
#include <string>
#include <unordered_map>
using namespace std;

class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.size()!=t.size()) return false;
        unordered_map<char,int> mp;
        for (int i=0;i<s.size();i++){
            mp[s[i]]+=1;
        }
        for (int j=0;j<t.size();j++){
            if (mp.find(t[j])==mp.end()) return false;
            mp[t[j]]-=1;
            if (mp[t[j]]==0){
                mp.erase(t[j]);
            }
        }
        return mp.size()==0;
    }
};