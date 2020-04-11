import requests

def call(depts):
    reqs = []
    for i in depts:
        reqs.append(requests.get("http://stardock.cs.virginia.edu/louslist/courses/view/" + i + "?JSON"))
    ret_ary = []
    for r in reqs:
        for line in r.text.split("\n"):
            s = line.split(';')
            try:
                ret_ary.append(s[0] + " " + s[1])
            except:
                pass
    ret_ary = list(set(ret_ary))
    ret_ary.sort()
    return ret_ary