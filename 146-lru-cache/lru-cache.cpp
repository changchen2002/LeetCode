struct Node{
    int key;
    int val;
    Node *next;
    Node *prev;
    Node(int key, int val) : key(key), val(val), next(nullptr), prev(nullptr){}
}; //定义struct 或class 之后必须加分号，这是 C++ 的语法规定。

class LRUCache {
public:
    int cap;
    unordered_map<int, Node *> dic;  //unordered_map=hashmap, map=根据键的大小自动排序O(log)
    Node *head = new Node(-1, -1);
    Node *tail = new Node(-1, -1);

    LRUCache(int capacity) : cap(capacity){ //Initialization 更快
        head->next=tail;
        tail->prev=head;  //Assignment
    }
    
    int get(int key) {
        if (dic.find(key)==dic.end()){ //没找到会返回一个特殊的迭代器，指向哈希表中最后一个元素的下一个位置
            return -1;
        }
        Node *node=dic[key];
        remove(node);
        add(node);
        return node->val;
    }
    
    void put(int key, int value) {
        if (dic.find(key)!=dic.end()){
            Node *oldNode=dic[key];
            remove(oldNode);
        }
        Node *node=new Node(key,value);
        dic[key]=node;
        add(node);

        if (dic.size()>cap){  //.size()=len()
            Node *deleteNode=head->next;
            remove(deleteNode);
            dic.erase(deleteNode->key); //先找到deleteNode才能找到它的key
        }
    }

    void add(Node *node){  //永久修改一个大型对象就需要用*
    //C++ 标准容器 (list, dic, set, vector) 应该使用 引用 (&) 来避免复制
        Node *pre=tail->prev;
        pre->next=node;
        node->prev=pre;
        node->next=tail;
        tail->prev=node;
    }

    void remove(Node *node){
        node->prev->next=node->next;
        node->next->prev=node->prev;
    }
};

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache* obj = new LRUCache(capacity);
 * int param_1 = obj->get(key);
 * obj->put(key,value);
 */