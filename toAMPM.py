def toAMPM(t):
    k=t.index(":")#取出冒号排在第几位
    h=int(t[0:k])#取出时
    m=int(t[k+1:len(t)])#取出分
    #print(k,h,m)
    ampm='AM'if h<12 else 'PM'
    if(h==0):
        h=12
    elif(h>12):
        h=h-12
    return char2(h)+':'+char2(m)+' '+ampm

def char2(n):
    if 0<=n<10:
        return '0'+str(n)
    else:
        return ''+str(n)

def main():
    print(toAMPM('00:20'))

main()
    
    
