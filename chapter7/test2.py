import time
starttime = time.time()
a = 15423645
s = 0
s = (a*(1+a))/2
print(s)
endtime = time.time()
dtime = endtime - starttime
print("程序运行时间：%.8s s" % dtime)