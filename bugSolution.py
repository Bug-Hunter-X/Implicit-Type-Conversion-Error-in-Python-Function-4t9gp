def function(a, b):
    if isinstance(a, int) and isinstance(b, int):
        return a + b
    elif isinstance(a, str) and isinstance(b, str):
        return a + b
    else:
        return "Error: incompatible types"

result = function(5, 10)
print(result)  # Output: 15

result = function(5, '10')
print(result)  # Output: Error: incompatible types