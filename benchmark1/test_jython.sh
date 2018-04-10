sizes="16 24 32 48 64 96 128 192 256 384 512 768 1024 1536 2048"

for size in $sizes
do
    echo $size
    /usr/bin/time --output jython.times --append --format "%e %M" java -jar jython-standalone-2.7.0.jar mandelbrot.py $size $size 255 > "j_${size}_${size}.ppm"
done
