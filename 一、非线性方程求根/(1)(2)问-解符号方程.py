#(1)(2)题将已知参数代入后可以直接求出未知参数的值，较为简单。
#写代码时可以用argparse函数实现手动输入任意几个参数，并通过代码自动求出剩余参数。

from sympy import symbols,solve
import argparse

#添加手动输入参数
parser = argparse.ArgumentParser()                         
parser.add_argument('-a', type=float, default=symbols("a"),help='Optional parameters')   
parser.add_argument('-p', type=float, default=symbols("p"),help='Optional parameters')    
parser.add_argument('-r', type=float, default=symbols("r"),help='Optional parameters')    
parser.add_argument('-n', type=float, default=symbols("n"),help='Optional parameters')    
#解析参数
args = parser.parse_args()                         
a,p,r,n =args.a , args.p , args.r , args.n

#目标方程
f=a*pow(1+r,n)*r-p*pow(1+r,n)+p

#求解f=0，解出未知数。
ans=solve(f)

print('answer is：',ans)

##注意：代码运行要手动在运行命令行最后输入参数，如：
#runfile('...',args='-a 100000 -p 10000 -r 0.06')
