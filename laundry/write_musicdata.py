import json

userId = input("你的UserId：")

musicId = input("乐曲ID：")

level = input("谱面难度(绿黄红紫白)：")#Basic=0,Re:Master=4
if level == "绿":
    level = 0
elif level == "黄":
    level = 1
elif level == "红":
    level = 2
elif level == "紫":
    level = 3
elif level == "白":
    level = 4
    
playCount = input("游玩次数：")

achievement = input("完成度（%）：")
achievement = int(float(achievement) * 10000)
if achievement >= 1005000:
    scoreRank = 13
elif achievement >= 1000000:
    scoreRank = 12
elif achievement >= 995000:
    scoreRank = 11
elif achievement >= 990000:
    scoreRank = 10
elif achievement >= 980000:
    scoreRank = 9
elif achievement >= 970000:
    scoreRank = 8
elif achievement >= 940000:
    scoreRank = 7
elif achievement >= 900000:
    scoreRank = 6
elif achievement >= 800000:
    scoreRank = 5
elif achievement >= 750000:
    scoreRank = 4
elif achievement >= 700000:
    scoreRank = 3
elif achievement >= 600000:
    scoreRank = 2
elif achievement >= 500000:
    scoreRank = 1
elif achievement >= 0:
    scoreRank = 0



comboStatus = input("连击状态（无 FC FC+ AP AP+）：")
if comboStatus == '无' or '':
    comboStatus = 0
elif comboStatus == 'FC':
    comboStatus = 1
elif comboStatus == 'FC+':
    comboStatus = 2
elif comboStatus == 'AP':
    comboStatus = 3
elif comboStatus == 'AP+':
    comboStatus = 4
    
syncStatus = input("同步状态（无 FS FS+ FDX FDX+）：")
if syncStatus == '无' or '':
    syncStatus = 0
elif syncStatus == 'FS':
    syncStatus = 1
elif syncStatus == 'FS+':
    syncStatus = 2
elif syncStatus == 'FDX':
    syncStatus = 3
elif syncStatus == 'FDX+':
    syncStatus = 4
    
deluxscoreMax = input("DX分数：")


music_data = ({
    "musicId": musicId,
    "level": level,
    "playCount": playCount,
    "achievement": achievement,
    "comboStatus": comboStatus,
    "syncStatus": syncStatus,
    "deluxscoreMax": deluxscoreMax,
    "scoreRank": scoreRank,
    "extNum1": 0
})

with open('musicdata.py','w') as f:
    f.write('userId = ')
    f.write(str(userId))
    f.write('\n\nmusic_data = (')
    json.dump(music_data,f,indent = 2)
    f.write(')')