#include<iostream>
#include<cstdio>
#include<cstring>
using namespace std;
int main(){
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    char t1[1000],t2[1000];
    while(~scanf("%s",t2)){
        if(t1[0]=='i' && t1[1]=='s' && strlen(t1)==2){
            printf("%s, ",t2);
        }
        strcpy(t1,t2);
    }
}