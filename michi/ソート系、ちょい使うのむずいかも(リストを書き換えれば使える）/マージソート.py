#マージソート
#計算量: O(nlogn) / 分割→マージを再帰的に行う

# マージソートの実装 (Moocsより)
def msort(lst):
    if len(lst) <= 1:
        return lst
    lst1 = lst[0: len(lst) // 2]
    lst2 = lst[len(lst) // 2:]

    sorted_lst1 = msort(lst1)
    sorted_lst2 = msort(lst2)

    return merge(sorted_lst1, sorted_lst2)

def merge(lst1, lst2):
    result = []
    i, j = 0, 0
    while (i < len(lst1)) and (j < len(lst2)):
        if lst1[i] <= lst2[j]:
            result.append(lst1[i])
            i += 1
        else:
            result.append(lst2[j])
            j += 1
    while i < len(lst1):
        result.append(lst1[i])
        i += 1
    while j < len(lst2):
        result.append(lst2[j])
        j += 1
        
    return result

# 過程を表示する用
from collections import deque

target = [8, 7, 6, 5, 4, 3, 2, 1]
marged = [False] * (len(target) + 1)
sque = deque([[0, (len(target) + 1) // 2, len(target)]])
mque = deque()
while len(sque):
    snow = sque.popleft()
    tque = deque()

    if marged[snow[1]-1] and marged[snow[2]-1]:
        mque.append(snow)
        continue
    else:
        tque.append(snow)

    # 後半
    if (snow[2] - snow[1]) < 2:
        marged[snow[1]] = True
    else:
        tque.appendleft([snow[1], snow[1] + (snow[2] - snow[1] + 1) // 2, snow[2]])        

    # 前半
    if (snow[1] - snow[0]) < 2:
        marged[snow[0]] = True
    
    else:
        tque.appendleft([snow[0], snow[0] + (snow[1] - snow[0] + 1) // 2, snow[1]])   
    
    for _ in range(len(tque)):
        s = tque.pop()
        sque.appendleft(s)

count = 0
while len(mque):
    count += 1
    now = mque.popleft()
    t_left = target[now[0]:now[1]]
    t_right = target[now[1]:now[2]]
    tl = []
    j = 0
    for i in range(len(t_left)):
        for j in range(j, len(t_right)):
            if t_left[i] <= t_right[j]:
                break
            
            else:
                tl.append(t_right[j])
                j += 1

        tl.append(t_left[i])
    
    for j in range(j, len(t_right)):
        tl.append(t_right[j])
        
    target = target[:now[0]] + tl + target[now[2]:]
    print("Loop {}. [{}]".format(count, ", ".join(map(str, target))))