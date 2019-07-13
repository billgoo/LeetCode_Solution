public class Solution {
    // you need treat n as an unsigned value
    public int reverseBits(int n) {
        int mask = 1, ret = 0;
	    for(int i = 0; i < 32; ++i){
		    ret <<= 1;
		    if ((mask & n) != 0) ret |= 1;
		    mask <<= 1;
	    }
	    return ret;
    }
}