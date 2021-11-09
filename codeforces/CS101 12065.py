#CS101 12065
def f(x):
    return(x**3-5*(x**2)+10*x-80)
i=0
j=10
while j-i>0.1**10:
    if f((i+j)/2)>0:
        j=(i+j)/2
    else:
        i=(i+j)/2
print('%.9f' % i)