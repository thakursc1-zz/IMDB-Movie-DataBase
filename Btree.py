### Class movie make a set of storage options as below
class movie:
    def __init__(self,title,ID,year,rating):
        self.title=title
        self.id=ID
        self.year=year
        self.rating=rating
    def printmovie(self):
        print self.title ,"(",self.year,")"
        print "imdb id :",self.id
        print "rating :",self.rating

        
### Class Tree Node Makes an node for the tree using movie class at payload       
class TreeNode:
    def __init__(self,id,val,year,rating=None,left=None,right=None,parent=None):
        self.key=val
        self.payload= movie(val,id,year,rating)  #### uses movie class
        self.leftchild=left
        self.rightchild=right
        self.parent=parent


    def hasLeftChild(self):
        return self.leftchild
    def hasRightChild(self):
        return self.rightchild
    def isLeftChild(self):
        return self.parent.leftchild==self and self.parent
    def isRightChild(self):
        return self.parent.rightchild==self and self.parent
    def isRoot(self):
        return not self.parent
    def isleaf(self):
        return not (self.rightchild or self.leftchild)
    def hasAnyChildren(self):
        return self.rightchild or self.leftchild
    def hasBothChilren(self):
        return self.rightchild and self.leftchild
    def replaceNodeData(self,ID,value,year,rating,lc,rc):
        self.key = value
        self.payload = movie(value,ID,year,rating)
        self.leftChild = lc
        self.rightChild = rc
        if self.hasLeftChild():
            self.leftChild.parent = self
        if self.hasRightChild():
            self.rightChild.parent = self

class BinarySearchTree:

    def __init__(self):
        self.root = None
        self.size = 0

    def length(self):
        return self.size

    def __len__(self):
        return self.size


    def put(self,key,val,year,rating):
        if self.root:
            val = val.lower()
            self._put(id,val,year,rating,self.root)
        else:
            val = val.lower()
            self.root=TreeNode(id,val,year,rating)
        self.size = self.size + 1

    def _put(self,id,val,year,rating,currentnode):           
        if val<currentnode.key:
            if currentnode.hasLeftChild():
                self._put(id,val,year,rating,currentnode.leftchild)
            else:
                currentnode.leftchild = TreeNode(id,val,year,rating,None,None,currentnode)
        elif val==currentnode.key:
            if id<currentnode.payload.id:
                if currentnode.hasLeftChild():
                    self._put(id,val,year,rating,currentnode.leftchild)
                else:
                    currentnode.leftchild = TreeNode(id,val,year,rating,None,None,currentnode)
            else:
                 if currentnode.hasRightChild():
                     self._put(id,val,year,rating,currentnode.rightchild)
                 else:
                     currentnode.rightchild = TreeNode(id,val,year,rating,None,None,currentnode)
                
        else:
            if currentnode.hasRightChild():
                self._put(id,val,year,rating,currentnode.rightchild)
            else:
                currentnode.rightchild = TreeNode(id,val,year,rating,None,None,currentnode)

                

    def get(self,val):
        if self.root:
            res = self._get(val,self.root)
            if res:
                return res.payload
            else:
                return None
        else:
            return None
        

        
    def _get(self,val,currentnode):
        if not currentnode:
            return None
        elif currentnode.key==val:
            return currentnode
        elif val<currentnode.key:
            return self._get(val,currentnode.leftchild)
        else:
            return self._get(val,currentnode.rightchild)



    def __getitem__(self,val):
        return self.get(val.lower())

    

    def pre_tree(self):
        self.root.payload.printmovie()
        print " LEFT SUBTREE Begins........"
        if self.root.hasLeftChild:
            self._pre_node(self.root.leftchild)
        print 500*"*"
        print " Right SUBTREE Begins.......\n"
        if self.root.hasRightChild:
            self._pre_node(self.root.rightchild)
        return
    def _pre_node(self,node):
        if  not node:
            return
        else:
            node.payload.printmovie()
            print "------------(",node.parent.payload.title,")"
            if node.hasLeftChild:
                self._pre_node(node.leftchild)
            if node.hasRightChild:
                self._pre_node(node.rightchild)
            else:return 

    def in_tree(self):
        print " LEFT SUBTREE Begins........"
        if self.root.hasLeftChild:
            self._in_node(self.root.leftchild)
        print 50*'/'
        self.root.payload.printmovie()
        print 50*'/'
        print " Right SUBTREE Begins.......\n"
        if self.root.hasRightChild:
            self._in_node(self.root.rightchild)
    def _in_node(self,node):
        if not node:
            return
        else:
            if node.hasLeftChild:
                self._in_node(node.leftchild)
            node.payload.printmovie()
            print "------------(",node.parent.payload.title,")"
            if node.hasRightChild:
                self._in_node(node.rightchild)
            else:return

    def post_tree(self):
        print " LEFT SUBTREE Begins........"
        if self.root.hasLeftChild:
            self._post_node(self.root.leftchild)
        print 50*'/'
        print 50*'/'
        print " Right SUBTREE Begins.......\n"
        if self.root.hasRightChild:
            self._post_node(self.root.rightchild)
        print 50*'-'
        self.root.payload.printmovie()
    def _post_node(self,node):
        if not node:
            return
        else:
            if node.hasLeftChild:
                self._post_node(node.leftchild)
            if node.hasRightChild:
                self._post_node(node.rightchild)
            node.payload.printmovie()
            print "------------(",node.parent.payload.title,")"
            return 
        
            
        
############# Creates a tree using Nodes.txt
My_Movie_BTree = BinarySearchTree()

file = open("Nodes.txt",'r')
temp = file.read().splitlines()
file.close()
length = len(temp)
i=0
while i<length:
    val = temp[i].lower()
    i=i+1
    id = temp[i]
    i=i+1
    year = temp[i]
    i=i+1
    rating = temp[i]
    i=i+1
    My_Movie_BTree.put(id,val,year,rating)
    
#generates binarysearch tree in less than 0.5 secs#


    
#My_Movie_BTree.pre_tree()#Time needed is only for printin
#k = My_Movie_BTree["mehmood"]'''
