import numpy as np
import math

class TreeNode:
    def __init__(self,val,val_index):
        self.val=val
        self.val_index=val_index
        self.left=None
        self.right=None

class kd_Tree:
    def __init__(self):
        self.stack=[]
        self.from_left_stack=[]
        self.nearst_node=None
        self.nearst_dis=0


    def create_kd_tree(self,data,val_index,dim_num):
        if len(data)==0:
            return None
        if val_index>=dim_num:
            val_index=0
        data.sort(key=lambda x: x[val_index])
        print(data)
        node_index=len(data)//2
        node=TreeNode(data[node_index],val_index)
        node.left=self.create_kd_tree(data[0:node_index],val_index+1,dim_num)
        node.right=self.create_kd_tree(data[node_index+1:],val_index+1,dim_num)
        return node

    def level_travel(self,root):
        queue=[root,None]
        index=0
        while(len(queue)>index):
            q=queue[index]
            if q==None:
                print()
                if index!=len(queue)-1:
                    queue.append(None)
            else:
                print(q.val,end="")
                if q.left!=None:
                    queue.append(q.left)
                if q.right!=None:
                    queue.append(q.right)
            index+=1


    def get_distance(self,point1,point2):
        total_sum=0
        for i in range(len(point1)):
            total_sum+=pow(point1[i]-point2[i],2)
        return total_sum



    def nearst_search(self,root,point):
        if root==None:
            return
        from_flag=0
        while(root!=None):
            self.stack.append(root)
            self.from_left_stack.append(from_flag)
            if point[root.val_index]<root.val[root.val_index]:
                root=root.left
                from_flag=1
            else:
                root=root.right
                from_flag=2
        if self.nearst_node==None:
            self.nearst_node=self.stack.pop()
            self.nearst_dis=self.get_distance(self.nearst_node.val,point)
        while(len(self.stack)!=0):
            q=self.stack.pop()
            from_flag=self.from_left_stack.pop()
            if self.get_distance(q.val,point)<self.nearst_dis:
                self.nearst_node=q
                self.nearst_dis=self.get_distance(q.val,point)
            if abs(q.val[q.val_index]-point[q.val_index])<self.nearst_dis:
                if from_flag==1:
                    self.nearst_search(q.right,point)
                elif from_flag==2:
                    self.nearst_search(q.left,point)



data=[(2,3),(5,4),(9,6),(4,7),(8,1),(7,2)]
tn=kd_Tree()
root=tn.create_kd_tree(data,0,2)
tn.level_travel(root)
tn.nearst_search(root,(6,2))
print(tn.nearst_node.val)
