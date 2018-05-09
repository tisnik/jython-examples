max_value=1
limit=100000000

OUTFILE="python3.times"
PREFIX="python3"

rm -f $OUTFILE
rm -f ${PREFIX}.txt

while [ $max_value -lt $limit ]
do
    echo $max_value
    echo -n "$max_value " >> $OUTFILE
    /usr/bin/time --output $OUTFILE --append --format "%e %M" python3 -B sieve_algorithm.py $max_value >> "${PREFIX}.txt"
    max_value=$(( $max_value * 2 ))
done
