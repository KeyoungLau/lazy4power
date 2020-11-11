ls = ['beijing', 'shanghai', 'tianjing', 'chongqing']
f = open('city.csv', 'w')
f.write(",".join(ls) + '\n')
f.close()
