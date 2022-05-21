from data.config import ADMINS
ad = '1788486201'
i = 0
for admin in ADMINS:
    if ad == admin:
        Admin = ADMINS.pop(i)


    i+=1
print()