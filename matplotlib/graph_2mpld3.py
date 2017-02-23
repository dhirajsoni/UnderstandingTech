#https://docs.python.org/2/library/csv.html
#http://matplotlib.org/2.0.0/users/pyplot_tutorial.html
#http://matplotlib.org/2.0.0/api/pyplot_api.html#matplotlib.pyplot.colors

#http://mpld3.github.io/
#https://github.com/arnoutaertgeerts/python-highcharts
#http://bokeh.pydata.org/en/latest/
#Bokeh is a project which targets browser-based graphics, and recent releases are beginning to do big data in the browser the right way.
#VisPy is another effort to provide easy visualization of large datasets. It is based on OpenGL, with plans to add a WebGL backend.


import csv 
import matplotlib.pyplot as plt,mpld3
from datetime import datetime
from mpld3 import fig_to_html, plugins
import mp
#import pygal
fn='eth2.iface.perf.copy'
filen=open(fn)
cR=csv.reader(filen,delimiter=' ')
header=next(cR)
print (header)
print header[0] , header[1]
for index,col in enumerate(header):
	print(index,col)

#hd=[]
#for he in header:
#	hd.append(he)

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

#http://matplotlib.org/2.0.0/faq/usage_faq.html
#http://matplotlib.org/2.0.0/users/pyplot_tutorial.html
#https://www.continuum.io/
#https://www.continuum.io/why-python
#http://www.tiobe.com/tiobe-index//
#https://github.com/mpld3/mpld3/issues/203

def ret_labels(dt,val):
	labels=[]
	for d,x in zip(dt,val):
       		labels.append(d.strftime("%d-%b-%Y %H:%M:%S")+" "+str(x))
        	#print d,x
	#print "============================="
	return labels



#input_values = [1, 2, 3, 4, 5]
#squares = [1, 4, 9, 16, 25]
line=plt.plot(dates,rx,'ro-',label=header[2])
#tt1 = mpld3.plugins.LineLabelTooltip(line[0], label='RX MB/s') #Doesnt render
#labels=[]
#for d,x in zip(dates,rx):
#	labels.append(d.strftime("%d-%b-%Y %H:%M:%S")+" "+str(x))
#	#print d,x
#print labels

tt1 = mpld3.plugins.PointLabelTooltip(line[0],ret_labels(dates,rx))

line=plt.plot(dates,tx,'bo-',label=header[3])
tt2 = mpld3.plugins.PointLabelTooltip(line[0],ret_labels(dates,tx))

line=plt.plot(dates,tot,'ko-',label=header[4])
tt3 = mpld3.plugins.PointLabelTooltip(line[0],ret_labels(dates,tot))
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
#plt.show()
#plt.figure(figsize=(10,5))
fig=plt.gcf()
ax=plt.gca()
fig.set_size_inches(15, 9)

mpld3.plugins.connect(fig,mp.MousePositionDatePlugin())
mpld3.plugins.connect(fig,tt1,tt2,tt3)
#mpld3.show()
mpld3.save_html(fig,"eth2.html")
