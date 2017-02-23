#http://www.pygal.org/en/stable/documentation/output.html
#http://pygal.org/en/stable/documentation/index.html
#http://pygal.org/en/stable/installing.html
#http://www.pygal.org/en/stable/documentation/configuration/rendering.html

import csv 
from datetime import datetime
import pygal
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

lc=pygal.Line()
lc.legend_at_bottom=True
lc.title='slcam350 Hypervisor Network traffic on eth20'
lc.x_title='Time'
lc.y_title='MB/s'
lc.width=1000
#lc.show_x_labels=False
lc.show_y_guides=True
lc.show_x_guides=True
lc.x_labels_major_every=10
lc.show_minor_x_labels=False
lc.x_labels=map(lambda d: d.strftime('%d-%b-%Y %H:%M:%S'),dates)
lc.x_label_rotation=90
lc.add(header[2],rx)
lc.add(header[3],tx)
lc.add(header[4],tot)
#lc.render()
lc.render_to_file('eth2_line_chart.svg')
#lc.render_to_png('eth2_line_chart.png')
