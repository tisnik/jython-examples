sizes="16 24 32 48 64 96 128 192 256 384 512 768 1024 1536 2048"

for size in $sizes
do
    echo $size
    /usr/bin/time --output python3.times --append --format "%e %M" python3 mandelbrot.py $size $size 255 > "p3_${size}_${size}.ppm"
done
