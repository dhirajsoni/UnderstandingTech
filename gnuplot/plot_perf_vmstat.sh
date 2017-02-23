#!/bin/bash
#plot_perf_vmstat.sh
#Don't have to cleanup the vmstat file

#20-Feb-2016 02:16:31 | procs -------------------memory------------------ ---swap-- -----io---- --system-- -----cpu-------
#20-Feb-2016 02:16:31 |  r  b       swpd       free       buff      cache   si   so    bi    bo   in   cs  us sy  id wa st
#20-Feb-2016 02:16:31 |  4  0    1012956    1072060     565256    8818916    0    0     0    19    0    1   8  3  89  0  0

#After parsing
#20-Feb-2016 02:16:41 |  1  0    1012956    1067556     565260    8819612    0    0     0   148 3133 2721   5  2  92  0  0 10452428
#20-Feb-2016 02:16:51 |  1  0    1012956    1070852     565260    8819620    0    0     0    20 2970 2595   5  2  93  0  0 10455732
#20-Feb-2016 02:17:01 |  1  0    1012956    1070496     565260    8819952    0    0     0    20 4201 3437   7  2  91  0  0 10455708


#TBD

#
graph_vmstat (){
gnuplot << EOF
set term  svg size 1000,500 mouse jsdir "./js"
#set datafile separator ","
set output "$dirp/$output_file"
set title "$title"
set xlabel "Time"
set ylabel "%CPU idle"
set y2label "KB(1024 bytes)"
set ytics nomirror
set y2tics 
set autoscale
set xdata time
#19-Feb-2016 13:05:19
set timefmt "%d-%b-%Y %H:%M:%S"
#set format x "%d %H:%M"
set format x "%T\n%D"
set style data lines
set grid
set key outside;
#set key right top;
#set key left bottom;
#set key outside below;
set key outside above;
#set key at 400,200

plot ["19-Feb-2016 13:04:54":"21-Feb-2016 11:16:43"] "$dirp/$input_file" using 1:18 title "%CPU Idle" axes x1y1,'' using 1:19  axes x1y1 title "%wa", '' using 1:21  axes x1y2 title "Free Mem KB",'' using 1:6  axes x1y2 title "swpd"

EOF
}





# Plot network usage
output_file=$1
input_file=$2
title=$3
dirp=$4

echo -e "Output_file: $dirp$output_file \n Input_file: $dirp/$input_file \n Title: $title "
graph_vmstat
