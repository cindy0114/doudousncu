x,y = map(int,input().split())                        #输入(x,y)
s_ju = (100-x)*y                                      #矩形面积
two_san = ((x*y)/2) + ((100-x)*(100-y)/2)             #两个三角形面积
ans = int(10000/2-s_ju-two_san)                       #阴影部分面积
print(ans)