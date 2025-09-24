class MinStack {
    stack<int> stack, dec;

public:
    MinStack() {}
    
    void push(int val) {
        stack.push(val);
        if (dec.empty() || val<=dec.top()){
            dec.push(val);
        }
    }
    
    void pop() {
        if (stack.top()==dec.top()){
            dec.pop();
        }
        stack.pop();
    }
    
    int top() {
        return stack.top();
    }
    
    int getMin() {
        return dec.top();
    }
};

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack* obj = new MinStack();
 * obj->push(val);
 * obj->pop();
 * int param_3 = obj->top();
 * int param_4 = obj->getMin();
 */