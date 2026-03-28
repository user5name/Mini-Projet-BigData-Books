import sys
for line in sys.stdin:
    line = line.strip()
    parts = line.split(',')
    if len(parts) >= 2 and parts[1] != "Category":
        category = parts[1].replace('"', '').strip()
        print("{0}\t1".format(category))