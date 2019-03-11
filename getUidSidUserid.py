import glob

PATH = 'E:/国创——MOOC分析/MOOC_db/2016-11-02/7001'
uids, sids,userids = {}, {}, set()

with open('%s/wda_mooc/wda_mooc_7001.txt'%PATH, 'r', encoding='utf-8') as file:
    for line in file:
        line = line.split('\t')
        uid = line[16]
        sid = line[17]
        if not uid in uids:
            uids[uid] = 1
        else:
            uids[uid] += 1
        if not sid in sids:
            sids[sid] = 1
        else:
            sids[sid] += 1

for fileName in glob.glob('%s/user_tag_value/*'%PATH):
    with open(fileName, 'r', encoding='utf-8') as file:
        for line in file:
            line = line.split('\1')
            userid = line[0]
            userids.add(userid)

count = 0
for userid in userids:
    print(userid, end=': ')
    if userid in uids:
        print('uids:', end=str(uids[userid]))
        count += 1
    if userid in sids:
        print('sids:', end=str(sids[userid]))
    print()

print('users:', str(len(userids)))    
print('count:', str(count))
input('Done')
        