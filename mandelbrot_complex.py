import palette_mandmap
from sys import argv, exit


def calc_mandelbrot(width, height, maxiter, palette):
    print("P3")
    print("{w} {h}".format(w=width, h=height))
    print("255")

    c = 0.0 - 1.5J
    for y in range(0, height):
        c = complex(-2.0, c.imag)
        for x in range(0, width):
            z = 0.0 + 0.0J
            i = 0
            while i < maxiter:
                if abs(z) > 4.0:
                    break
                z = z**2 + c
                i += 1

            r = palette[i][0]
            g = palette[i][1]
            b = palette[i][2]
            print("{r} {g} {b}".format(r=r, g=g, b=b))
            c += 3.0/width
        c += 3.0J/height


if __name__ == "__main__":
    if len(argv) < 4:
        print("usage: python mandelbrot width height maxiter")
        exit(1)

    width = int(argv[1])
    height = int(argv[2])
    maxiter = int(argv[3])
    calc_mandelbrot(width, height, maxiter, palette_mandmap.palette)
