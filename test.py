import re
from datetime import datetime


print(datetime.now().strftime("%Y-%d-%m %H:%M:%S"))
z=re.match("(201\w+)\-.*\-.*\W(08\:16\:.*)",datetime.now().strftime("%Y-%d-%m %H:%M:%S"))
#s="102-s:karthik"
#z=re.match("(1\w+)\-.\:.*",s)
print(z)
if(z):
    print(z.group())