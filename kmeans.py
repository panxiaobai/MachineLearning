import numpy as np
import random

def kmean(data,class_num,iter_num):
    class_center=[]

    for i in range(class_num):
        class_center.append(5*np.random.rand(data.shape[1]))
    print(class_center)

    for i in range(iter_num):
        class_center=get_class_center(data,class_num,class_center)
        print(class_center)



def get_class_center(data,class_num,class_center):
    class_list = []
    for i in range(class_num):
        dis = np.sum((data - class_center[i]) ** 2, axis=1)
        #print(dis)
        class_list.append(dis)
    class_list = (class_list == np.min(class_list, axis=0))
    for i in range(class_num):
        data_index = np.where(class_list[i])
        if len(data_index[0])>0:
            class_center[i] = np.mean(data[data_index], axis=0)
        else:
            class_center[i]=np.zeros(data.shape[1])
        #print(class_center[i])
    return class_center






def main():
    data = np.array([[2., 3.], [4., 7.], [9., 6.], [8., 1.], [7., 2.], [5., 4.]])
    kmean(data,3,10)

if __name__ == '__main__':
    main()
