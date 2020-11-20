import random
suits = ['红桃', '黑桃', '梅花', '方块']
faces = ['2', '3', '4','5','6','7','8','9','10', 'J', 'Q', 'K', 'A']
flag = 'yes'
while flag == 'yes':
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
    flag = input('继续游戏请输入yes，停止游戏请输入no：')
    



