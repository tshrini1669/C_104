from collections import Counter
import csv
with open('SOCR-HeightWeight.csv', newline='')as f:
    reader = csv.reader(f)
    filedata = list(reader)
filedata.pop(0)
newdata=[]
for i in range(len(filedata)):
    n_num = filedata[i][2]
    newdata.append(float(n_num))
data = Counter(newdata)
mode_data_range = {
    "75-85":0,
    "85-95":0,
    "95-105":0
}
for height,occurence in data.items():
    if 75 < float(height) < 85:
        mode_data_range["75-85"] += occurence
    elif 85 < float(height) < 95:
        mode_data_range["85-95"] += occurence
    elif 95 < float(height) < 105:
        mode_data_range["95-105"] += occurence
moderange,modeoccurence = 0,0
for range,occurence in mode_data_range.items():
    if occurence > modeoccurence:
        moderange,modeoccurence = [int(range.split("-")[0]),int(range.split("-")[1])],occurence
mode = float((moderange[0] + moderange[1])/2)
print(f"Mode is {mode:2f}")
    
    
