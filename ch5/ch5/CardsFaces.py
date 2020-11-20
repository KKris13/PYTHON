import random
faces = ['2', '3', '4','5','6','7','8','9','10', 'J', 'Q', 'K', 'A']
myFace = random.choice(faces)
yourFace = random.choice(faces)
print('我的牌是',myFace,'，你的牌是',yourFace)
if faces.index(myFace) > faces.index(yourFace):
    print('我赢了！')
elif faces.index(myFace) < faces.index(yourFace):
    print('你赢了！')
else:
    print('平局！')    



