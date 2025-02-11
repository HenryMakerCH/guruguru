import csv
import json
import io
import sys

from lib.sdgb import sdgb_api
from lib.preview import preview

sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')

begin = int(input("Begin:"))
end = int(input("End:"))
errors = 0
nulls = 0
players = 0

for userId in range(begin,end):
    try:
        playerPreview = json.loads(preview(userId))
    except ValueError as e:
        print(f"{userId} Error occurred: {e}",flush=True)
        errors += 1
        userId -= 1
        continue
    if playerPreview["userId"] == None:
        print (f"{userId},No Player",flush=True)
        nulls += 1
        continue
    else:
        userName = playerPreview["userName"]
        players += 1
        print(f"{userId},{userName}",flush=True)
    playerRating = playerPreview["playerRating"]
    filename = 'PlayerData_' + str(begin) + '_' + str(end) + '.csv'
    with open(filename,'a',newline='',encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow([userId,userName,playerRating])
print("========Completed========")
print(f"Scan completed from {begin} to {end} with {errors} errors.")
print(f"Scanned {players} players, {nulls} nulls in total.")