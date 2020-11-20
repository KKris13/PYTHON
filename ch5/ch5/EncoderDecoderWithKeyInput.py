# 输入需要加密的消息
message = input("请输入需要加密或解密的消息：")
key = eval(input("请输入密钥（ 1-26）: "))
# 将消息转换为大写字母
message = message.upper()

# 存储加密后的消息
output = ""

# 遍历消息中的每个字母
for letter in message:              
    if letter.isupper():
        value = ord(letter) + key    
        letter = chr(value)         
        if not letter.isupper():    # 检查是否移出大写字母的范围
            value -= 26             # 返回大写字母范围
            letter = chr(value) 
    output += letter                # 把字母加入输出消息
print("结果为: ", output)   

