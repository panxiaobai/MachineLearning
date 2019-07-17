import numpy as np
import math

min_dis,min_node=None,None

class Node():
    def __init__(self,data=None,lchild=None,rchild=None,l=None):
        self.data=data
        self.lchild=lchild
        self.rchild=rchild
        self.l=l

def find_median(x,l):
    sort_x=x[:,l].copy()
    sort_x.sort()
    median=sort_x[len(sort_x)//2]
    return np.where(x[:,l]==median),median


def create_kd_tree(data,depth):
    if data.size==0:
        return None
    l=depth % data.shape[1]

    index,median=find_median(data,l)

    rc_data=data[np.where(data[:,l]>median)].copy()
    lc_data=data[np.where(data[:,l]<median)].copy()


    root=Node()
    root.data=np.squeeze(data[index])
    root.rchild=create_kd_tree(rc_data,depth+1)
    root.lchild=create_kd_tree(lc_data,depth+1)
    root.l=l
    '''
    print("-----")
    print(root.data)
    print(root.l)
    print("right:"+str(rc_data))
    print("left:"+str(lc_data))
    print("-----")
    '''
    return root


def get_dis(x,y):
    return math.sqrt(np.sum((x-y)*(x-y)))

def search(point,node,p):
    global min_dis,min_node
    #递归寻找子节点
    if point[node.l]<node.data[node.l] and node.lchild is not None:
        min_dis,min_node,pc=search(point,node.lchild,'lchild')
    elif point[node.l]>node.data[node.l] and node.rchild is not None:
        min_dis, min_node,pc =search(point,node.rchild,'rchild')
    else:
        pc=None

    dis=get_dis(node.data,point)
    print(dis,node.data)
    #判定当前节点是否最短距离
    if min_dis is None or dis<min_dis:
        min_dis=dis
        min_node=node
    if pc==None:
        pc=p
    #判定是否与其他子空间超平面相交
    abs=math.fabs(node.data[node.l]-point.data[node.l])
    if abs<=min_dis and abs>0:
        if pc=='lchild' and node.rchild is not None:
            min_dis, min_node, pc=search(point,node.rchild,'rchild')
        elif pc=='rchild' and node.lchild is not None:
            min_dis, min_node, pc=search(point,node.lchild,'lchild')
        else:
            pass

    return min_dis,min_node,pc






def main():
    data=np.array([[2.,3.],[4.,7.],[9.,6.],[8.,1.],[7.,2.],[5.,4.]])

    root=create_kd_tree(data,0)
    min_dis,min_node,_=search(np.array([2.1,4.5]),root,None)
    print(min_dis,min_node.data)


if __name__ == '__main__':
    main()

