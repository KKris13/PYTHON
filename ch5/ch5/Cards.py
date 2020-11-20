import random
suits = ['红桃', '黑桃', '梅花', '方块']
faces = ['2', '3', '4','5','6','7','8','9','10', 'J', 'Q', 'K', 'A']
mySuit = random.choice(suits)
myFace = random.choice(faces)
print('我的牌是', mySuit + myFace)


