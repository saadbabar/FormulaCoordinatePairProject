def main():
    x = (input("Enter x-value for coordinate pair:"))
    y = (input("Enter y-value for coordinate pair:"))
    xs = (input("Enter x-value for coordinate pair:"))
    ys = (input("Enter y-value for coordinate pair:"))
    print("(" + str(x) + "," + str(y) + ")" + "and" + "(" + str(xs) + "," + str(ys) + ")")
    mpx = (int(x) + int(xs)) / 2
    mpy = (int(y) + int(ys)) / 2
    print("The mid point formula is" + "(" + str(mpx) + "," + str(mpy) + ")")

    slope = ((int(ys) - int(y)) / (int(xs) - int(x)))
    b = (int(y) - (int(x) * slope))
    print("the slope intercept form is " + "y=" + str(slope) + "x" + "+" + str(b))


main()


# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.



