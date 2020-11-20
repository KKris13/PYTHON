#这是一个转换16进制转10进制的程序
def decimalToHex(decimalValue):
    Hex=''
    while decimalValue!=0:
        hexValue=decimalValue%16
        Hex=toHexChar(hexValue)+Hex#字符串的连接
        decimalValue//=16
    return Hex

def toHexChar(hexValue):#把余数转换为相应的16进制字符
    if 0<=hexValue<=9:
        return chr(hexValue+ord('0'))
    else:
        return chr(hexValue-10+ord('a'))
    
def main():
    while True:
        decimalValue=eval(input("enter a decimal number(enter -1 to quit):"))
        if decimalValue>=0:
            print("the hex number for decimal {} is {}\
                ".format(decimalValue,decimalToHex(decimalValue)))
        else:
            break
main()
