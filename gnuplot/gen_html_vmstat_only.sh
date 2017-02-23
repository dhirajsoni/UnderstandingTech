#Usage
#Go to the analysis directory where all .svg files are then do this
#/media/sf_FusionPSR/SAAS/Debug/MyScripts/io_scripts/perf/gen_html_vmstat_only.sh ECZT-TEST > ECZT-TEST-vmstat.html

echo "<html>"
echo "<head>"
echo "<title>Host $1 IO Pressure Analysis: </title>"
echo "<link rel="stylesheet" href="http://gnuplot.sourceforge.net/demo_svg_4.6/gnuplot_demo.css" type="text/css">"
echo "</head>"
echo "<body>"
echo ""

echo "<h1>Host $1 IO Pressure Analysis: </h1>"

ft=vmstat

echo "<h4 id=\"Back\">$i</h4>"
for i in *$ft*.svg
do
echo "<a href=\"#$i\">$i</a></BR>"
done


echo "<table>"

for i in *$ft*.svg
do
echo "<tr>"
echo "<td valign=top>"
echo "<h4 id=\"$i\">$i</h4>"
echo "<a href=\"#Back\">Back</a></BR>"
echo "</td>"
echo "</tr>"
echo "<tr>"
echo "<td valign=top>"
echo "<embed src=\"$i\" type="image/svg+xml" width=1000 height=500 class="float-right">"
echo "</td>"
echo "</tr>"
done




echo "</table>"
echo "</html"
echo ""

