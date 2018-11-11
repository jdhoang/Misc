import copy

def GenList (temp_list, inp_list, tsum):
    global cnt
    for i in range (len (inp_list)):
        new_temp = copy.copy (temp_list)
        new_list = copy.copy (inp_list)
 
        new_temp.append (inp_list[i])
        new_list = inp_list[i+1:]
        if sum(new_temp) == tsum:
            cnt += 1
            print("---", new_temp)
        GenList (new_temp, new_list, tsum)
 

def calculate_combinations (ilist, target_sum):
    global cnt
    cnt = 0
    tmp = list()
    print (ilist)

    GenList (tmp, ilist, target_sum)
    return cnt



print (calculate_combinations ([5,5,15,10],15),"\n")
print (calculate_combinations ([1,3,5,15,2,10],15),"\n")
print (calculate_combinations ([1,3,5,7,8,10],15),"\n")
print (calculate_combinations ([2,3,5,7,8,10,12,13],10),"\n")

