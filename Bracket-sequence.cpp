#include<bits/stdc++.h>
 
using namespace std;
 
int main()
 
{
 
    string s;
 
    cin>>s;                   //input as a string
 
    long int i,z=0,l=0,r=0,x=0,y=0;
 
    for(i=0;i<s.length();i++)
 
{
 
if(s[i]=='(')
 
l++;
 
else
 
r++;
 
}                           //calculates the no. of left and right parenthesis in l & r respectively
 
if(l!=r)
 
cout<<"0";            //if l and r are unequal it can never be in a balanced form in any no. of rotations
 
else
 
{
 
l=0;                     
 
for(i=0;i<s.length();i++)
 
{
 
if(s[i]=='(')
 
l++;
 
else
 
l--;
 
if(l<y)
 
{
 
y=l;
 
x=i+1;
 
}
 
}// the idea of the above loop is increment l when we get '(' and decrement at ')' and note the point in x where l becomes the lowest. Let's take an example
 
//input : )()())((   at i=0,l=-1,y=-1,x=i+1=1  at i=1,l=0,no change in x & y as if condition is false  at i=2,l=-1  at i=3,l=0  at i=4,l=-1  at i=5,l=-2,y=-2,x=i+1=6  at i=6,l=-1  at i=7,l=0 end;
 
//at x=6, l=-2 which is the lowest and if u observe that if we left-shift array to x(=6) positions, the input becomes balanced in O(n). 
 
  reverse(s.begin(), s.begin()+x);
 
  reverse(s.begin()+x, s.end());
 
  reverse(s.begin(), s.end());
 
//above 3 lines left-shifts the array to 6 positions and the input becomes (()()()) {balanced}.
 
l=0;
 
for(i=0;i<s.length();i++)
 
{
 
if(s[i]=='(')
 
l++;
 
else
 
l--;
 
if(l==0)
 
z++;
 
}
 
//above loop increments l at '(' and decrement at ')' and counts the points where l=0 in z, notice that the points where z becomes zero, if u left-shift your input at that position
 
//the input becomes balanced. Input has changed to (()()()) : at i=0,l=1 at i=1,l=2 at i=2,l=1 at i=3,l=2 at i=4,l=1 at i=5,l=2 at i=6,l=1 at i=7,l=0,z=1 so answer will be 1.
 
//Let's summarize with input#6: )()(())()(  :  No. of left and right parenthesis r equal therefore code moves to else:
 
//at i=0,l=-1,y=-1,x=i+1=1  at i=1,l=0  at i=2,l=-1  at i=3,l=0  ...  l never goes less than -1 so x=1 at the end; Left-shifting 1 position input becomes  ()(())()() (balanced).
 
//calculating points at which l=0; Input has changed to ()(())()() : at i=0,l=1 at i=1,l=0,z=1 at i=2,l=1 at i=3,l=2 at i=4,l=1 at i=5,l=0,z=2 at i=6,l=1 at i=7,l=0,z=1 at i=8,l=1 at i=9,l=0,z=4 
 
//answer will be 4. //Hope u like it :) (Satwik Dash)
 
cout<<z;
 
}
 
    return 0;
 
}