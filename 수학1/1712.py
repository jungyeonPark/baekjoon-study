A, B, C = map(int, input().split())
ans = 0
if C <= B:      # 손익분기점이 존재하지 않을 때
    ans = -1
else:
    ans = A // (C - B) + 1      
print(ans)

'''
ans * (C - B) - A = 0   이익과 손해가 같아지는 순간
ans = A / (C - B)
이 순간을 넘으면 손익분기점이니까 +1 해서
ans = A // (C - B) + 1      
'''