#return the reversal of an integer,e.g.reverse(465) returns 654
def reverse(number):
    Str=''
    while number!=0:
        i=number%10
        Str=Str+str(i)
        number=number//10
    print("the reverse number is:",Str)
    return Str

#return true if number is a palindrome
def IsPalindrome(number):
    Str=reverse(number)
    if str(number)==Str:
        return True
    else :
        return False

def main():
    n=eval(input("please input a integer:"))
    if IsPalindrome(n):
        print("{} is a palindrome".format(n))
    else:
        print("{} is not a palindrome".format(n))

main()
