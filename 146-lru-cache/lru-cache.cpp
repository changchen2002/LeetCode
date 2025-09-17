class LRUCache {
public:
    int cap;
    unordered_map<int,list<pair<int,int>>::iterator> dic;
    //:: 意思是iterator是定义在它左边的那个类或命名空间内部的
    //iterator 存储的是该缓存项在 lru 链表中的精确**内存地址。
    list<pair<int,int>> lru; //pair只能两个,用.first 和 .second 访问

    LRUCache(int capacity): cap(capacity) {}

    int get(int key) {
        auto it=dic.find(key);
        if (it==dic.end()) return -1;
        int value=it->second->second; 
        //it->first=key, it->second是list<pair<int,int>>这个迭代器,it->second->second是pair的第二个元素
        lru.erase(it->second);   //迭代器O(1)
        lru.push_front({key,value}); //

        dic.erase(it);
        dic[key]=lru.begin(); //
        return value;
    }
    
    void put(int key, int value) {
        auto it=dic.find(key);
        if (dic.find(key)!=dic.end()){
            lru.erase(it->second); //it 在dic中是什么,包含key和 iterator?然后it->second 是iterator?
            dic.erase(it);
        }
        lru.push_front({key,value}); //传入多个值就用{}
        dic[key]=lru.begin();
        if (dic.size()>cap){
            auto it=dic.find(lru.rbegin()->first); 
            //reverse begin反向迭代器指向列表末尾, lru.rbegin()是一个迭代器, lru.rbegin()->first 指向迭代器的第一项也就是key
            lru.pop_back(); //deque 和 list 都有 pop_front(),O(1)
            dic.erase(it); //先删lru再删dic,因为it是通过lru指的
        }
    }
};

/*
访问tuple: 
    tuple<int, string, double> t = {1, "hello", 3.14};
    double d = get<1>(t) << endl;  //必须知道精确index
访问vector:
    vector<int> v = {10, 20, 30, 40};
    cout << v[2] << endl; //endl 直接打印
count<<"hello"\n;
cout << "world" << endl; 保证看见
*/