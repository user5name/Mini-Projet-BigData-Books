import sys
current_category = None
current_count = 0

for line in sys.stdin:
    category, count = line.strip().split('\t')
    if current_category == category:
        current_count += int(count)
    else:
        if current_category:
            print("{0}\t{1}".format(current_category, current_count))
        current_category = category
        current_count = int(count)
if current_category:
    print("{0}\t{1}".format(current_category, current_count))