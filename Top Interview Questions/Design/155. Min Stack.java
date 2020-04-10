class MinStack {

    /** initialize your data structure here. */
    private long min;
    private Stack<Long> stack;
    
    public MinStack() {
        stack = new Stack<>();
    }
    
    public void push(int x) {
        if (stack.isEmpty()){
            min = x;
            stack.push(0L);
        }else{
            stack.push(x - min);
            if (x < min){
                min = x;
            }
        }
    }
    
    public void pop() {
        if (!stack.isEmpty()){
            long top = stack.pop();
            if (top < 0){
                min = min - top;
            }
        }else{
            System.out.println("Error");
        }
        
    }
    
    public int top() {
        if (stack.peek() > 0){
            return (int)(stack.peek() + min);
        }else{
            return (int)min;
        }
    }
    
    public int getMin() {
        return (int)min;
    }
}

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack obj = new MinStack();
 * obj.push(x);
 * obj.pop();
 * int param_3 = obj.top();
 * int param_4 = obj.getMin();
 */