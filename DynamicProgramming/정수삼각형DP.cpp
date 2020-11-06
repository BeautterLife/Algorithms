#include <string>
#include <vector>
#include <algorithm>
#include <iostream>
using namespace std;
/*
프로그래머스 정수삼각형
20/11/06 20:30
하삼각행렬의 형태로 생각.
d배열은 하나만 있되, d배열 갱신시에는 오른쪽->왼쪽으로 갱신해야 방금 갱신된 d에의해 영향받지않고
올바른 값이 계산됨.
*/
int solution(vector<vector<int>> triangle) {
    int answer = 0;
    int d[500]={0};
    int maxVal = 0;

    for(int i=0;i<triangle.size();i++){
        //첫줄처리(초기값)
        if(i==0){
            d[0] = triangle[i][i];
            continue;
        }
        //오른쪽 끝값은 윗 줄의 맨끝값 + 입력값
        d[i] = d[i-1]+triangle[i][i];
        //오른쪽부터 갱신해야 이전에 갱신한 d에 영향을 안받음.
        for(int j=i-1;j>0;j--){
            d[j] = max(d[j-1],d[j])+triangle[i][j];
            //maxVal = max(maxVal,d[j]);
        } 

        //첫값은 이전d+현재값
        d[0] +=triangle[i][0];
        
       
    }
    sort(d,d+triangle.size());
     /*for(int j=0;j<triangle.size();j++){
        cout<<d[j]<< " ";
     }
     */ 
    
    return d[triangle.size()-1];
}
