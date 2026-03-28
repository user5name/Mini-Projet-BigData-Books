import sys
# Define valid ratings to filter out noise/shifted columns
valid_ratings = ["One", "Two", "Three", "Four", "Five"]

for line in sys.stdin:
    line = line.strip()
    if "Price" in line or "Rating" in line:
        continue
        
    parts = line.split(',')
    if len(parts) >= 4:
        rating = parts[3].strip()
        # Only print if it's a real rating word
        if rating in valid_ratings:
            print("{0}\t1".format(rating))