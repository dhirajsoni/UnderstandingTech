#Usage: /media/sf_FusionPSR/SAAS/Debug/MyScripts/io_scripts/perf/run_perf_vmstat_plot.sh sgfar08110e11_monitor.vmstat.perf
#Usage: /media/sf_FusionPSR/Projects/PROD_ISSUES/zdt_io_pressure/scripts/run_perf_vmstat_plot.sh aufsn4x0fuf05_monitor.vmstat.perf

echo "cd to dir where .perf file is"

input_file=$1
hostn=`echo $input_file| cut -d"_" -f1` #Gets hostname from the file itself. So saves manual entry
dirp=`pwd` 		#Current dir where .perf file resides
dirs=`dirname $0` 	#scriptdir
echo $hostn $dirp

#If you want to override dirp then place the folder here
#dirp="/media/sf_FusionPSR/Projects/PROD_ISSUES/zdt_io_pressure/logs/eboi-amer/cffar14100y05.usdc2.oraclecloud.com/cffar14100y05osw"
#dirp="/media/sf_FusionPSR/Projects/PROD_ISSUES/zdt_io_pressure/monitor/eboi-amer/analysis"

#Call the parsing vmstat routing to clean the file up for plotting
$dirs/parse_perf_vmstat.sh $1 $hostn $dirp $dirs
