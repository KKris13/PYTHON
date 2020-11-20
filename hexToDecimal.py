#这是一个转换10进制转16进制的程序
def hexToDecimal(HexValue):
    sum=0
    l=len(HexValue)
    for c in HexValue:
        if '0'<=c<='9':
            t=ord(c)-ord('0')
        else :
            c=str.upper(c)#转换成大写
            t=ord(c)-ord('A')+10
        sum=sum+t*(16**(l-1))
        l=l-1
    return sum

def main():
    while True:
        hexValue=(input("enter a hex (enter -1 to quit):"))
        if hexValue=='-1':
            break
        else:
            print("the decimal number for hex {} is {}\
            ".format(hexValue,hexToDecimal(hexValue)))
        
main()
