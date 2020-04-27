import requests

def call(depts):
    reqs = []
    for i in depts:
        payload = requests.get("http://stardock.cs.virginia.edu/louslist/courses/view/" + i + "?JSON")
        if(len(payload.content)):
            reqs.append(payload)
    ret_ary = []
    top = avg(reqs)
    for r in reqs:
        for line in r.text.split("\n"):
            s = line.split(';')
            try:
                ret_ary.append(s[0] + " " + s[1] + ": " + s[3][0:top])
            except:
                pass
    ret_ary = list(set(ret_ary))
    ret_ary.sort()
    return ret_ary


#Intelligent Delimiter
def avg(classes):
    if(not classes):
        return 0
    ret_ary = []
    for r in classes:
        for line in r.text.split("\n"):
            s = line.split(';')
            try:
                ret_ary.append(len(s[3]))
            except:
                pass
    ret_ary = list(set(ret_ary))
    ret_ary.sort()
    avg = sum(ret_ary)/len(ret_ary)
    return int(avg + 10) 
