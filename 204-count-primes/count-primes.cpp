class Solution {
public:
    int countPrimes(int n) {
        if (n<=2) return 0;
        int count=0;
        vector<bool>numbers(n,true);
        for (int i=2;i<sqrt(n);i++){
            if (numbers[i]){
                for (int j=i*i;j<n;j+=i){
                    if (numbers[j]){
                        numbers[j]=false;
                        count++;
                    }
                    
                }
            }
        }
        return n-count-2;
    }
};