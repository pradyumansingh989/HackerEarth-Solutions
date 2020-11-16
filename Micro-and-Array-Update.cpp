#include<iostream>
using namespace std;
 
int main(){
	int t, tmp, n, k, max, diff, i;
	cin >> t;
 
    while(t--){
 
        cin >> n >> k;
 
        max=0;
 
        for(i=0; i<n; i++){
 
            cin >> tmp;
 
            diff = k - tmp;
 
            if(max < diff)
 
                max = diff;
 
        }
 
        if(max < 0)
 
            max=0;
 
        cout << max << "\n";
 
    }
 
}