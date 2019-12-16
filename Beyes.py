import pandas as pd

data=pd.read_csv("data.csv")

def probability(event,event_val):
    event_num=sum(data[event]==event_val)
    num=len(data)
    return event_num/num

def condition_probability(condition,condition_val,event,event_val):
    condition_num=sum(data[condition]==condition_val)

    union_num=sum(data[data[condition]==condition_val][event]==event_val)

    return union_num/condition_num


pre_data={"X1":2,"X2":"S"}
class_set=set(data["Y"])
for c in class_set:
    c_pro=probability("Y",c)
    for event,event_val in pre_data.items():
        c_pro*=condition_probability("Y",c,event,event_val)
    print(c,c_pro)

