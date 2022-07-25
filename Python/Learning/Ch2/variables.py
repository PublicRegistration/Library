# Declare & Initialize
f = 0
print(f)

# Re-Declaring the Variable

f = "abc"
print(f)

# Global vs. Local Variables in Functions

def someFunction():
    #global f
    f = "def"
    print(f)

someFunction()
print(f)

# Delete Variables
del f
print(f)