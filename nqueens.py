from z3 import *
n = 4
ls = []
vs = [[[Bool("p_{}{}{}".format(i,j,k)) for k in range(n)] for j in range(n)] for i in range(n)]
ls = ls + [PbEq([(vs[i][j][k],1) for j in range(n) for k in range(n)],1) for i in range(n)]
ls = ls + [PbEq([(vs[i][j][k],1) for i in range(n) for k in range(n)],1) for j in range(n)]
ls = ls + [PbLe([(vs[i][j][k],1) for i in range(n) for j in range(n) for k in range(n) if i+j == t],1) for t in range(2*n-1)]
ls = ls + [PbLe([(vs[i][j][k],1) for i in range(n) for j in range(n) for k in range(n) if i-j == t],1) for t in range(-n+1,n)]
s = Solver()
s.add(And(ls))
r = s.check()
print(r)
print(s.model())