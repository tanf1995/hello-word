def needNum():
    nowNums = int(input())
    li = map(int, raw_input().split(" "))
        
    li.sort()
    needNums = 0
    i = 0
    j = 1
    while i<len(li)-1:
        if li[i+1] - li[i] > 20:
            if j==1:
                needNums += 2
            else:
                needNums +=1
            i += 1
            j = 1
            continue
          		
        elif li[i+1] - li[i] > 10:
            if j==1:
                needNums += 1
                i += 2
                continue
            else:
                needNums += 1
                i += 1
                continue
                
        else:
            if j==1:
                i += 1
                j = 2
            else:
                i +=1
                j = 1
            continue
           
    if (len(li)+needNums) % 3 == 1:
        needNums += 2
    elif (len(li)+needNums) % 3 == 2:
        needNums += 1
    else:
        pass
    print(needNums)

needNum()