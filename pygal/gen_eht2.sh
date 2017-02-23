echo "Date Time rxMbyt/s txMbyt/s TotalMBytes/s" >> eth2.iface.perf
cat slcam350_monitor.iface.perf|grep eth2 |awk '{printf ("%s %s %0.2f %0.2f %0.2f\n",  $1,$2,$9/(1024*1024),$10/(1024*1024),($9+$10)/(1024*1024))}' >> eth2.iface.perf
