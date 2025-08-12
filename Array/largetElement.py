class Solution:
    def largest(self, arr):
        n=len(arr)
        maxi=arr[0]
        for i in range(1,n):
            if arr[i]>= maxi:
                maxi=arr[i]
                
            return maxi;
                
                

