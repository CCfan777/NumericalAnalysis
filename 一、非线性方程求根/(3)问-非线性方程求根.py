'''
thought:  第（3）题 将已知参数代入后，求解r的公式较为复杂，需要用迭代法求出。因此先对该公式进行收敛性判断，如果收敛，再用迭代法迭代出解。
               同时，采用不同的加速方法加速迭代，再观察实验结果。
input   :   在命令行手动输入年数n。
output： 得到未加速、加权法加速、松弛法加速、斯蒂芬森法加速的迭代结果。 
'''

from sympy import symbols,diff

#(3)题 未加速
r=0.06
loop=20
n=int(input('请输入n的值：'))
r0=[] #用于保存所有迭代值
for i in range(loop):    
    y=r
    r=0.1*(1-1/pow(1+r,n))
    i=i+1
    r0.append(r)
    print('未加速——第{}次迭代结果为：{}'.format(i,r))
print('-------------------------------------')

#(3)题 加权法加速
#n=int(input('请输入n的值：'))
x=symbols('x')
y=0.1*(1-1/pow(1+x,n))  
r=0.06
r1=[]
loop=10  
for i in range(loop):
    L=diff(y,x).evalf(subs={x:r})  #当x=r时，w的值
    r=1/(1-L)*(0.1*(1-1/pow(1+r,n))-L*r)
    i=i+1
    r1.append(r)
    print('加权法加速：第{}次迭代结果为：{}'.format(i,r))
print('-------------------------------------')


#(3)题 松弛法加速
#n=int(input('请输入n的值：'))
x=symbols('x')
y=0.1*(1-1/pow(1+x,n))  
r=0.06
r2=[]
loop=10  
for i in range(loop):
    w=1/(1-diff(y,x).evalf(subs={x:r}))  
    r=(1-w)*r+w*0.1*(1-1/pow(1+r,n))  
    i=i+1
    r2.append(r)
    print('松弛法加速：第{}次迭代结果为：{}'.format(i,r))
print('-------------------------------------')


#(3)题 斯蒂芬森加速
r=0.06
r3=[]
loop=10
#n=int(input('请输入n的值：'))
for i in range(loop):
    y=0.1*(1-1/pow(1+r,n))
    z=0.1*(1-1/pow(1+y,n))
    if (z-2*y+r)==0:
        break;
    r=r-pow(y-r,2)/(z-2*y+r)
    i=i+1
    r3.append(r)
    print('斯蒂芬森迭代：第{}次迭代结果为：{}'.format(i,r))
