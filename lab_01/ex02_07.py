print("Enter text lines (Type 'done' to finish):")
lines = []
while True:
    line = input()
    if line.lower() == 'done':
        break
    lines.append(line)
print("\nThe entered lines in uppercase:")
for line in lines:
    print(line.upper())
