import requests

def call(depts):
    reqs = []
    for i in depts:
        reqs.append(requests.get("http://stardock.cs.virginia.edu/louslist/courses/view/" + i + "?JSON"))
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
    return int(sum(ret_ary)/len(ret_ary)) + 10
