import numpy as np

def train(data,label,w,b,lr):
    '''

    :param data: data.shape=(data_num,data_length)
    :param label: label.shape=(data_num,1)
    :param w: w.shape=(data_length)
    :param b:
    :param lr: learning rate
    :return:
    '''
    flag=True
    while(flag):
        flag=False
        for i in range(data.shape[0]):
            x=data[i]
            x_=x[:,np.newaxis]
            w_ = w[:,np.newaxis]
            y_pred=np.dot(w_.T,x_)+b
            y=label[i]
            if y*y_pred<=0:
                w=w+lr*y*x
                b=b+lr*y
                flag=True
    return w,b


def param_init(data):
    w=np.zeros((data.shape[1]))
    b=0
    return w,b

def main():
    data=np.array([[3,3],[4,3],[1,1]])
    label=np.array([[1],[1],[-1]])
    w,b=param_init(data)
    w,b=train(data,label,w,b,1)
    print(w)
    print(b)


if __name__ == '__main__':
    main()
