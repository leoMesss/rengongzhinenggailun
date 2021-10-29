
import random
import numpy as np
def h_n(seq):
    leng=len(seq)
    board=np.zeros([leng,leng])
    for i in range(leng):
        if(seq[i]>-1):
            board[i][seq[i]]=1

    row_sum=board.sum(axis=0)
    row_cost=row_sum[np.where(row_sum>1)].sum()
    column_sum = board.sum(axis=1)
    column_cost = column_sum[np.where(column_sum>1)].sum()
    upDown_cost=0
    downUp_cost=0
    for i in range(leng):
        x=i
        y=0
        tem_upDown=0
        while(x<leng and y<leng):
            if(board[x][y]==1):
                tem_upDown+=1
            x+=1
            y+=1
        if(tem_upDown>1):
            upDown_cost+=tem_upDown
        x=0
        y=i
        tem_upDown = 0
        while(x<leng and y<leng):
            if (board[x][y] == 1):
                tem_upDown += 1
            x += 1
            y += 1
        if (tem_upDown > 1):
            upDown_cost += tem_upDown
        x=i
        y=0
        tem_Downup = 0
        while(x>0 and y<leng):
            if (board[x][y] == 1):
                tem_Downup += 1
            x -= 1
            y += 1
        if (tem_Downup > 1):
            downUp_cost += tem_Downup
        x=leng-1
        y=i
        tem_Downup = 0
        while (x > 0 and y < leng):
            if (board[x][y] == 1):
                tem_Downup += 1
            x -= 1
            y += 1
        if (tem_Downup > 1):
            downUp_cost += tem_Downup
    return row_cost+column_cost+upDown_cost+downUp_cost

def Astar4eightqueen(n):
    priority_queen=[{"remain_queen":n,"cost":28,"seq":[-1]*n}]
    while(priority_queen):
        now_best_queen=priority_queen.pop(0)
        if(now_best_queen["remain_queen"]==0 and now_best_queen["cost"]==0):
            return now_best_queen["seq"]
        seq=now_best_queen["seq"]
        if(seq.count(-1)==0):
            continue
        pos=list(range(n))
        for j in range(n):
            row_loc=seq.index(-1)
            column_loc=random.choice(pos)
            temp_seq = list(seq)
            temp_seq[row_loc]=column_loc
            pos.remove(column_loc)
            priority_queen.append({"remain_queen":temp_seq.count(-1),"cost":h_n(temp_seq),"seq":temp_seq})
        priority_queen.sort(key=lambda x:x["cost"]+x["remain_queen"])
    return "解不存在"

seq=Astar4eightqueen(8)
print(seq)
leng=len(seq)
board = np.zeros([leng, leng])
for i in range(leng):
    if (seq[i] > -1):
        board[i][seq[i]] = 1
print(board)