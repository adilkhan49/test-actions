from datetime import datetime
ts = datetime.now()

with open('file.log','a') as f:
    f.write(str(ts) + '\n')