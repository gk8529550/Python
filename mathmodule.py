import math

def main():
    # Constants
    print("Pi:", math.pi)
    print("Euler's number:", math.e)

    # Basic mathematical operations
    print("\nBasic Operations:")
    print("Square root of 25:", math.sqrt(25))
    print("Power of 2^3:", math.pow(2, 3))
    print("Absolute value of -10:", math.fabs(-10))
    
    # Trigonometric functions
    print("\nTrigonometric Functions:")
    angle_in_radians = math.radians(45)
    print("Sine of 45 degrees:", math.sin(angle_in_radians))
    print("Cosine of 45 degrees:", math.cos(angle_in_radians))
    print("Tangent of 45 degrees:", math.tan(angle_in_radians))

    # Logarithmic and exponential functions
    print("\nLogarithmic and Exponential Functions:")
    print("Natural logarithm of 2:", math.log(2))
    print("Base-10 logarithm of 100:", math.log10(100))
    print("Exponential function e^2:", math.exp(2))

    # Ceiling and floor functions
    print("\nCeiling and Floor Functions:")
    print("Ceiling of 4.3:", math.ceil(4.3))
    print("Floor of 4.7:", math.floor(4.7))

    # Other functions
    print("\nOther Functions:")
    print("Factorial of 5:", math.factorial(5))
    print("GCD of 12 and 18:", math.gcd(12, 18))
    print("Degrees from radians:", math.degrees(math.pi/2))

if __name__ == "__main__":
    main()
