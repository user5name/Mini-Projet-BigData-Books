import matplotlib.pyplot as plt

# Data from your results
ratings = ['Four', 'One', 'Three', 'Five', 'Two']
counts = [5, 4, 4, 3, 3]

plt.bar(ratings, counts, color='skyblue')
plt.xlabel('Book Rating')
plt.ylabel('Number of Books')
plt.title('Distribution of Book Ratings')
plt.savefig('rating_distribution.png')
plt.show()