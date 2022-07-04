def permute(nums):
  result_perms = [[]]
  for n in nums:
    new_perms = []
    for perm in result_perms:
      for i in range(len(perm)+1):
        new_perms.append(perm[:i] + [n] + perm[i:])
        result_perms = new_perms
  return result_perms
a = [2,5]
b = [5,2]
c = [6,6]
d = [8,3]
x = [0,2]
my_nums = [a,b,c,d]
dd = permute(my_nums)
ln = len(permute(my_nums))
q = []
for i in range(ln):
    q.append(x)
    for j in range(4):
        q.append(dd[i][j])
    q.append(x)
lq = len(q)
dc ={}
for i in range(lq):
    if i == 0 or i%6 == 0:
        dc.update({i: q[i]+q[i+1]+q[i+2]+q[i+3]+q[i+4]+q[i+5]})

dq={}
for i in range(0,138,6):
    l1=((dc.get(i)[2]-dc.get(i)[0])**2+(dc.get(i)[3]-dc.get(i)[1])**2)**0.5
    l2=((dc.get(i)[4]-dc.get(i)[2])**2+(dc.get(i)[5]-dc.get(i)[3])**2)**0.5
    l3=((dc.get(i)[6]-dc.get(i)[4])**2+(dc.get(i)[7]-dc.get(i)[5])**2)**0.5
    l4=((dc.get(i)[8]-dc.get(i)[6])**2+(dc.get(i)[9]-dc.get(i)[7])**2)**0.5
    l5=((dc.get(i)[10]-dc.get(i)[8])**2+(dc.get(i)[11]-dc.get(i)[9])**2)**0.5
    ll = l1+l2+l3+l4+l5
    dq.update({i: ll})
import math
min=min(dq, key=dq.get)
final = dc.get(min)
r2 = []
r2.append(final[2])
r2.append(final[3])
r3 = []
r3.append(final[4])
r3.append(final[5])
r4 = []
r4.append(final[6])
r4.append(final[7])
r5 = []
r5.append(final[8])
r5.append(final[9])
print("samyi kratchaishii put'", x, '=>', r2,'=>', r3,'=>', r4, '=>', r5,'=>',x )

