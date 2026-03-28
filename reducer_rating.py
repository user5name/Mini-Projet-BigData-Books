import sys

current_rating = None
current_count = 0

for line in sys.stdin:
    line = line.strip()
    rating, count = line.split('\t')
    count = int(count)

    if current_rating == rating:
        current_count += count
    else:
        if current_rating:
            print("{0}\t{1}".format(current_rating, current_count))
        current_rating = rating
        current_count = count

if current_rating:
    print("{0}\t{1}".format(current_rating, current_count))