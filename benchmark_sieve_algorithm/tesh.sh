i=1

while [ $i -le 100000000000 ]
do
    echo $i
    i=$(( $i * 2 ))
done
