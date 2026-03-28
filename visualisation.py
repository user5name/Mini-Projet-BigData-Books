import matplotlib.pyplot as plt

def create_chart():
    ratings = []
    counts = []

    # Reading the file you just pulled from HDFS
    try:
        with open('rating_results.txt', 'r') as f:
            for line in f:
                # MapReduce output is tab-separated: Rating \t Count
                parts = line.strip().split('\t')
                if len(parts) == 2:
                    ratings.append(parts[0])
                    counts.append(int(parts[1]))

        # Create the Bar Chart
        plt.figure(figsize=(10, 6))
        colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99','#c2c2f0']
        plt.bar(ratings, counts, color=colors, edgecolor='black')

        # Add labels and title
        plt.xlabel('Book Ratings', fontweight='bold')
        plt.ylabel('Number of Books', fontweight='bold')
        plt.title('Distribution of Book Ratings (Mystery Category)', fontsize=14)
        plt.grid(axis='y', linestyle='--', alpha=0.7)

        # Save the image for your report
        plt.savefig('rating_distribution_chart.png')
        print("Success! Chart saved as 'rating_distribution_chart.png'")
        plt.show()

    except FileNotFoundError:
        print("Error: rating_results.txt not found. Make sure you ran the 'docker exec' command first.")

if __name__ == "__main__":
    create_chart()
