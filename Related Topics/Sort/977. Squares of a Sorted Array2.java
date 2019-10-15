class Solution {
    public int[] sortedSquares(int[] A) {
        int n = A.length;
        int[] result = new int[n];
        int i = 0;
        while(i < n && A[i] < 0){
            i++;
        }
        int j = i--;
        
        int counter = 0;
        while(i >= 0 && j < n){
            if(A[i] * A[i] < A[j] * A[j]){
                result[counter++] = A[i] * A[i];
                i--;
            }
            else{
                result[counter++] = A[j] * A[j];
                j++;
            }
        }
        
        while(i >= 0){
            result[counter++] = A[i] * A[i];
            i--;
        }
        while(j < n){
            result[counter++] = A[j] * A[j];
            j++;
        }
        return result;
    }
}