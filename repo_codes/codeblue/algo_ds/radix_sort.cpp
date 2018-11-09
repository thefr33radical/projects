#include <iostream>
#include<bits/stdc++.h>
using namespace std;

void msort(vector<int> &arr, int low,int mid, int high)
{
	int start1= low;
	int start2 =mid+1;
	vector<int> temp;
	int i=0;
	
	while(start1<mid || start2 < high)
	{
		if(arr[start1]<arr[start2])
		{
			temp[i++]=arr[start1++];
		}
		else
		{
			temp[i++]=arr[start2++];
		}
	}
	
	while(start1<mid)
		temp[i++]=arr[start1++];
	while(start2 < high)
		temp[i++]=arr[start2++];
		
	int k=0;
	for(int i =low;i<high;i++)
		{
			arr[i]=temp[k++];
			cout<<arr[i];
		}	
	
	
	
	
	
}


void split(vector<int> &arr,int low, int high)
{
	if(low<high)
	{
		int mid = (low+high)/2;
		cout<<mid;
		split(arr,low,mid);
		split(arr,mid+1,high);
		//msort(arr,low,mid,high);
	}
	
	
	
}

int main() {
	// your code goes here
	vector<int> arr({2,1,45,23,65,9,57});
	for(auto i=0:i<arr.size)
		cout<<i<<" ";
		
	
	
	
	
	
	return 0;
}