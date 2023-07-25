# Write a  python program using function to convert celsius to fahrenheit

# Formula	
# (0°C × 9/5) + 32 = 32°F


def farh(cel):
    return (cel * 9/5) + 32


c = int(input("Enter the celsius temp: "))
f = farh(c)
print("Fahrenheit Temperature is " + str(f))