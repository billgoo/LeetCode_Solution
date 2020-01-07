/*
Binary Search
- 根据: 每个人花的多少时间(time)来做binary search: 每个人花多久时间, 可以在K个人之内, 用最少的时间完成?
- time variable的范围不是index, 也不是page大小. 而是[minPage, pageSum]
- validation 的时候注意3种情况: 人够用 k>=0, 人不够所以结尾减成k<0, 还有一种是time(每个人最多花的时间)小于当下的页面, return -1
- O(nLogM). n = pages.length; m = sum of pages.
因为是二分搜索，所以显然最终会收敛到一个恰好的值，具体的int数。因为大或小都会导致二分搜索继续下去
 */
public class CopyBooks {  
    /** 
     * @param pages: an array of books with pages number. 
     * @param k: number of copiers. 
     * @return: minimum max number. 
     */  
    public int copyBooks(int[] pages, int k) {  
        if (pages.length == 0) {  
            return 0;    
        }  
          
        //1. calculate the sum of pages, and its max element.  
        int sum = 0;  
        int biggest = pages[0];  
        for (int i = 0; i < pages.length; i++) {  
            sum += pages[i];  
            biggest = Math.max(biggest, pages[i]);  
        }  
          
        //2.use binary enumeration to calculate whether the mid   
        //  value is the proper one.  
        int midStart = biggest;  
        int end = sum;          
        while (midStart + 1 < end) {  
            int mid = midStart + ((end - midStart) >> 1); // binary enumeration.  
            // validate if the mid value can meet with k copiers.  
            if (calculateCopiers(pages, mid) > k) { // when meet. midStart value is smaller.   
                midStart = mid;            // increase it.   
            } else {  
                end = mid;                 // when can't meet. midStart value is larger.  
            }  
        }  
          
        if (calculateCopiers(pages, midStart) <= k) {  
            return midStart;  
        }  
          
        return end;  
    }  
      
      
      
    // with given limit number, calculate the copiers that needed.  
    private int calculateCopiers(int[] pages, int limit) {  
        if (pages.length == 0) {  
            return 0;  
        }  
          
        int copiers = 1;  
        int subTaskSum = pages[0]; // limit is always >= pages[0]  
        for (int i = 1; i < pages.length; i++) {  
            if (subTaskSum + pages[i] > limit) {  
                copiers++;  
                subTaskSum = 0;  
            }  
            subTaskSum += pages[i];  
        }  
          
        return copiers;  
    }  
      
    /** 
    public static void main(String[] args) { 
        int[] pages = new int[]{}; 
    } 
    */  
}  

