def BubbleSort(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp
                print(alist)
Data = [3, 6, 4, 10]
BubbleSort(Data)

def shortBubbleSort(alist):
    exchanges = True
    passnum = len(alist) - 1
    while passnum > 0 and exchanges:
        exchanges = False
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                exchanges = True
                temp = alist[i]
                alist[i] =alist[i+1]
                alist[i+1] = temp
            print(alist)
            passnum = passnum - 1
alist =[3,6,4,10]
shortBubbleSort(alist)
