repeat_count=1
limit=10000000

OUTFILE="jython.times"
PREFIX="jython"

rm -f $OUTFILE
rm -f ${PREFIX}.txt

while [ $repeat_count -lt $limit ]
do
    echo $repeat_count
    echo -n "$repeat_count " >> $OUTFILE
    /usr/bin/time --output $OUTFILE --append --format "%e %M" java -jar jython-standalone-2.7.0.jar string_concat.py $repeat_count >> "${PREFIX}.txt"
    repeat_count=$(( $repeat_count * 2 ))
done
