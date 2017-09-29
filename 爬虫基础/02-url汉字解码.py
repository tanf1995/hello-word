import urllib.request

wd = {'wd': '谭峰'}

res = urllib.parse.urlencode(wd)
print(res)