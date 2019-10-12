list_barev=["cervena","cierna","modra"]
list_barev.append("zlta")

list_dalsich_barev = ["bila","zelena"]

list_vsech_barev = list_barev+list_dalsich_barev

def insert(item_list,item,index):
    #pridani barvy na zadany index
    item_list.append(item)
    for i in range(len(item_list)-1-1,index-1,-1):
        print(i)
        item_list[i+1]=item_list[i]
    item_list[index]=item
    return(item_list)


list_vsech_barev=insert(list_vsech_barev,"ruzova",2)
list_vsech_barev=insert(list_vsech_barev,"ruzova",2)
list_vsech_barev=insert(list_vsech_barev,"ruzova",2)
list_vsech_barev=insert(list_vsech_barev,"ruzova",2)

def prehod_dva(list1, index1, index2):
    a=list1[index1]
    list1[index1]=list1[index2]
    list1[index2]=a
    return(list1)

list1=[9,5,3,4,1,0]


def bubble_sort(list1):
    # zoradenie prvkov v liste
    for j in range(len(list1)-1):    
        for i in range(len(list1)-1-j):
            if list1[i]>list1[i+1]:
                list1=prehod_dva(list1,i,i+1)
    return(list1)
    
list2=bubble_sort(list1)


list2.pop(2)



