import random
suits = ['红桃', '黑桃', '梅花', '方块']
faces = ['2', '3', '4','5','6','7','8','9','10', 'J', 'Q', 'K', 'A']
flag = True
while flag:
    mySuit = random.choice(suits)
    myFace = random.choice(faces)
    yourSuit = random.choice(suits)
    yourFace = random.choice(faces)
    print('我的牌是',mySuit+myFace,'，你的牌是',yourSuit+yourFace)
    if faces.index(myFace) > faces.index(yourFace):
        print('我赢了！')
    elif faces.index(myFace) < faces.index(yourFace):
        print('你赢了！')
    else:
        print('平局！')    
    answer = input('按回车键继续游戏，其它键停止游戏：')
    flag = (answer == '')
    



