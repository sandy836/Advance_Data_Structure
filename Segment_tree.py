class SegmentTree:
    def __init__(self, inputArray, length, operator):
        self.inputArray = inputArray
        self.length = length
        self.operator = operator
        self.segTree = 4*length*[0]
        self._build(0, length-1, 0)
    
    def _build(self, low, High, pos):
        if low == High:
            self.segTree[pos] = self.inputArray[low]
            return
        mid = (low+(High - low)//2)
        self._build(low, mid, 2*pos+1)
        self._build(mid+1, High, 2*pos+2)
        self.segTree[pos] = self.operator(self.segTree[2*pos+1], self.segTree[2*pos+2])
    
    def _update(self, index, rang_Low, range_High, updated_Val, pos):
        if rang_Low == range_High:
            self.segTree[pos] = updated_Val
            return 
        
        mid = (rang_Low+(range_High - rang_Low)//2)
        if index<=mid:
            self._update(index, rang_Low, mid, updated_Val, 2*pos+1)
        else:
            self._update(index, mid+1, range_High, updated_Val, 2*pos+2)
        self.segTree[pos] = self.operator(self.segTree[2*pos+1], self.segTree[2*pos+2])
        
    def _query(self, query_Low, query_High, pos, rang_Low, range_High):
        if range_High<query_Low or query_High<rang_Low:
            return 0
        elif rang_Low>=query_Low and range_High<=query_High:
            return self.segTree[pos]
        else:
            mid = (rang_Low+(range_High - rang_Low)//2)
            query_Left = self._query(query_Low, query_High, 2*pos+1, rang_Low, mid)
            query_Right = self._query(query_Low, query_High, 2*pos+2, mid+1, range_High)
            return self.operator(query_Left, query_Right)

class Driver:
    def __init__(self, inputArray, operator):
        self.inputArray = inputArray
        self.length = len(inputArray)
        self.operator = operator
        self.create_SegTree()
    
    def create_SegTree(self):
        self.ObjSegTree = SegmentTree(self.inputArray, self.length, self.operator)
    
    def update_SegTree(self, updateIndex, valueToUpdate):
        self.ObjSegTree._update(updateIndex, 0, self.length-1, valueToUpdate, 0)
    
    def query_SegTree(self, query_Low, queryHigh):
        try:
            if self.length-1<query_Low or queryHigh<0:
                raise Exception("Sorry out of range query")
            return self.ObjSegTree._query(query_Low, queryHigh, 0, 0, self.length-1)
        except Exception as error:
            return error


inputArray = [1, 3, 5, 7, 9, 11]

def operator(_input1, _input2):
    return _input1 + _input2

runObject = Driver(inputArray, operator)
runObject.update_SegTree(1, 4)
print(runObject.query_SegTree(0, 2))





        

