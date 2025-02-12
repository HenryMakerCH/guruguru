import csv
import json
import io
import sys
import time

from lib.sdgb import sdgb_api
from lib.preview import preview

sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')

begin = int(input("Begin:"))
end = int(input("End:"))
totalRetries = 0
nulls = 0
players = 0
retries = 0

for userId in range(begin,end):
    while retries < 5:
        try:
            playerPreview = json.loads(preview(userId))
            break
        except ValueError as e:
            print(f"{userId} Error occurred: {e}",flush=True)
            totalRetries += 1
            time.sleep(1)
        retries += 1
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
print(f"Scan completed from {begin} to {end} with {totalRetries} retries.")
print(f"Scanned {end - begin} userIds, {players} players and {nulls} nulls in total.")