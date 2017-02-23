#parse_perf_vmstat.sh
#Cleans up the vmstat lines; called from run_perf_vmstat_plot.sh 
#Creates $dirp/$input_file.out i.e. a .out file with same name

input_file=$1
hostn=$2
dirp=$3
dirs=$4


echo "Inside parse_perf_vmstat.sh...."
#echo $input_file $hostn  

cat $dirp/$input_file |grep -v '\-\-'|grep -v swpd | awk  '{ printf "%s %s\n", $0, $7+$8+$9}' > $dirp/$input_file.out

#Remove the first line from the file
tail -n  +2 $dirp/$input_file.out  > $dirp/$input_file.tmp
mv $dirp/$input_file.tmp $dirp/$input_file.out

find $dirp -size 0 -type f -exec rm '{}' \;

$dirs/plot_perf_vmstat.sh $hostn-vmstat.svg $input_file.out $hostn-vmstat $dirp
