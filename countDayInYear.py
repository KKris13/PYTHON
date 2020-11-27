#编写一个程序返回一年的天数
def numberOfDayInYear(year):
    if year % 4==0 and year % 100!=0 or year % 400==0:
        return 366
    else:
        return 365
def main():
    for i in range(2010,2021):
        print("{}年的天数是{}".format(i,numberOfDayInYear(i)))

main()
