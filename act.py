from datetime import datetime
ts = datetime.now()
print(ts)
with open('file.log','a') as f:
    f.write(str(ts) + '\n')