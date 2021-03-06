'''
<접근방법>
 : 100x100짜리 도화지를 1x1짜리 정사각형으로 모두 분리해 색칠한다.
 1) (0,0) 부터 (100,100) 까지의 이차원 리스트를 만든다
 2) 색종이의 갯수만큼 반복문을 작성한다
 3) 해당 색종이의 왼쪽 하단 점을 기준으로 우로 10칸 아래로(그림에서는 위지만 편의를 위해 아래로 생각하자, 답은 같으니) 10칸을 색칠한다
 4) 이때 색칠이되어있으면 넘어가고 아니면 색칠 후 ans 1증가
 5) 반복문 다돌고 난 후 ans값이 정답
'''

n = int(input())

paper = [[0]*101 for _ in range(101)]   # 빈 도화지인 이차원 리스트
ans = 0                                 # ans 초기설정
for _ in range(n):                      # 색종이 만큼 반복문
    x, y = map(int, input().split())    # 왼쪽 위(그림에서는 아래)좌표
    for i in range(10):                 # 해당 좌표를 기준으로 10칸씩
        for j in range(10):
            if paper[y+i][x+j] == 0:    # 색칠 되어있지 않으면 색칠 후 ans 1증가
                paper[y+i][x+j] = 1
                ans += 1
print(ans)
