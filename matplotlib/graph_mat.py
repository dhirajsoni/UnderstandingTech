#https://docs.python.org/2/library/csv.html
#http://matplotlib.org/2.0.0/users/pyplot_tutorial.html
#http://matplotlib.org/2.0.0/api/pyplot_api.html#matplotlib.pyplot.colors

#http://mpld3.github.io/
#https://github.com/arnoutaertgeerts/python-highcharts
#http://bokeh.pydata.org/en/latest/

import csv 
import matplotlib.pyplot as plt
from datetime import datetime
fn='eth2.iface.perf.copy'
filen=open(fn)
cR=csv.reader(filen,delimiter=' ')
header=next(cR)
print (header)
print header[0] , header[1]
for index,col in enumerate(header):
	print(index,col)


dates=[]
rx=[]
tx=[]
tot=[]
for row in cR:
        dt_str=row[0]+" "+row[1] 
	dt2 = datetime.strptime(dt_str, "%d-%b-%Y %H:%M:%S")
	dates.append(dt2)
	#print dt2
	rx.append(float(row[2]))
	tx.append(float(row[3]))
	tot.append(float(row[4]))
#print (rx)



#input_values = [1, 2, 3, 4, 5]
#squares = [1, 4, 9, 16, 25]
plt.plot(dates,rx,'ro-',label=header[2])
plt.plot(dates,tx,'bo-',label=header[3])
plt.plot(dates,tot,'ko-',label=header[4])
#plt.plot(dates,tx,linewidth=5,c='blue')
#plt.plot(dates,tot,linewidth=5,c='black')
#plt.scatter(input_values,squares,linewidth=5)
# Set chart title and label axes.
plt.title("eth2 hypervisor slcam350 n/w traffic", fontsize=24)
plt.xlabel("Time", fontsize=14)
#plt.xticks(rotation=90)
plt.ylabel("MB/s", fontsize=14)
plt.grid(True)
plt.legend()
#plt.tick_params(axis='both', labelsize=14)
plt.show()
