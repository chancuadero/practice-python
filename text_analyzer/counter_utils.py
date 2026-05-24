# text_analyzer/counter_utils.py
import matplotlib.pyplot as plt

def plot_counter(counter, n_most_common=5):
    """Plots a bar chart showing the most common items from a Counter object."""
    # 1. Get the top N elements and their frequency values
    top_items = counter.most_common(n_most_common)
    
    # 2. Separate keys (words) and values (counts) into lists
    labels, values = zip(*top_items) if top_items else ([], [])
    
    # 3. Render a clean matplotlib bar plot
    plt.figure(figsize=(8, 4))
    plt.bar(labels, values, color='skyblue')
    plt.xlabel('Tokens')
    plt.ylabel('Frequency')
    plt.title('Top Token Counts')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()  # Displays the window on your local machine
