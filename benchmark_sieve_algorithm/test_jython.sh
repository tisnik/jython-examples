max_value=1
limit=100000000

OUTFILE="jython.times"
PREFIX="jython"

rm -f $OUTFILE
rm -f ${PREFIX}.txt

while [ $max_value -lt $limit ]
do
    echo $max_value
    echo -n "$max_value " >> $OUTFILE
    /usr/bin/time --output $OUTFILE --append --format "%e %M" java -jar jython-standalone-2.7.0.jar sieve_algorithm.py $max_value >> "${PREFIX}.txt"
    max_value=$(( $max_value * 2 ))
done
