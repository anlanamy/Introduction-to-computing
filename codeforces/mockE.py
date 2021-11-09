#5
d={'negative':-1, 'zero':0, 'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9, 'ten':10, 'eleven':11, 'twelve':12, 'thirteen':13, 'fourteen':14, 'fifteen':15, 'sixteen':16, 'seventeen':17, 'eighteen':18, 'nineteen':19, 'twenty':20, 'thirty':30, 'forty':40, 'fifty':50, 'sixty':60, 'seventy':70, 'eighty':80, 'ninety':90, 'hundred':100, 'thousand':1000, 'million':1000000}
l=input().split()
num=0
l2=[]
l4=[]
if l[0]=='negative':
    l1=l[1:]
else:
    l1=l
if 'million' in l1:
    k=l1.index('million')
    l2=l1[0:k]
    l3=l1[k+1:]
else:
    l3=l1
if 'thousand' in l3:
    j=l3.index('thousand')
    l4=l3[0:j]
    l5=l3[j+1:]
else:
    l5=l3
def hun(l):
    count=0
    if 'hundred' in l:
        m=l.index('hundred')
        l6=l[0:m]
        l7=l[m+1:]
        for j in l6:
            count+=d[j]
        count*=100
        for j in l7:
            count+=d[j]
    else:
        for j in l:
            count+=d[j]
    return count

num=hun(l2)*1000000+hun(l4)*1000+hun(l5)
if l[0]=='negative':
    num=-num
print(num)