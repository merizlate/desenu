def parse(text):
    lines = text.split('\n')
    result = {}
    for line in lines:
        if '=' in line:
            key, value = line.split('=', 1)
            result[key.strip()] = value.strip()
    return result

text = """
name = Alice
age = 30
city = Wonderland
"""

parsed_data = parse(text)
print(parsed_data)  # Output: {'name': 'Alice', 'age': '30', 'city': 'Wonderland'}
