import matplotlib.pyplot as plt
import numpy as np


def draw_graphs():
    # Create a figure with 2 subplots (for the two different charts)
    fig, axes = plt.subplots(2, 1, figsize=(12, 14), constrained_layout=True)
    
    # --------- Simple Bar Chart (First Example) ---------
    # Data for first bar chart
    fruits = ['apple', 'blueberry', 'cherry', 'orange']
    counts = [40, 100, 30, 55]
    colors = ['red', 'blue', 'red', 'orange']  # Colors matching the fruit types
    
    # Create the first bar chart
    bars = axes[0].bar(fruits, counts, color=colors)
    
    # Add title and labels
    axes[0].set_title('Fruit supply by kind and color', fontsize=14)
    axes[0].set_ylabel('fruit supply')
    axes[0].set_ylim(0, 110)  # Set y-axis limits
    
    # Add a legend
    from matplotlib.patches import Patch
    legend_elements = [
        Patch(facecolor='red', label='red'),
        Patch(facecolor='blue', label='blue'),
        Patch(facecolor='orange', label='orange')
    ]
    axes[0].legend(handles=legend_elements, title='Fruit color')
    
    # --------- Grouped Bar Chart (Second Example) ---------
    # Data for the grouped bar chart
    species = ("Adelie", "Chinstrap", "Gentoo")
    penguin_means = {
        'Bill Depth': (18.35, 18.43, 14.98),
        'Bill Length': (38.79, 48.83, 47.50),
        'Flipper Length': (189.95, 195.82, 217.19)
    }
    
    # Set width of bars
    bar_width = 0.25
    
    # Set positions of the bars on X axis
    r1 = np.arange(len(species))
    r2 = [x + bar_width for x in r1]
    r3 = [x + bar_width for x in r2]
    
    # Create the grouped bar chart
    axes[1].bar(r1, penguin_means['Bill Depth'], width=bar_width, label='Bill Depth', color='#1f77b4')
    axes[1].bar(r2, penguin_means['Bill Length'], width=bar_width, label='Bill Length', color='#ff7f0e')
    axes[1].bar(r3, penguin_means['Flipper Length'], width=bar_width, label='Flipper Length', color='#2ca02c')
    
    # Add titles and labels
    axes[1].set_title('Penguin attributes by species', fontsize=14)
    axes[1].set_ylabel('Length (mm)')
    axes[1].set_xticks([r + bar_width for r in range(len(species))])
    axes[1].set_xticklabels(species)
    
    # Add a legend
    axes[1].legend()
    
    # Add value labels on top of each bar
    for i, attribute in enumerate([penguin_means['Bill Depth'], 
                                  penguin_means['Bill Length'], 
                                  penguin_means['Flipper Length']]):
        positions = [r1, r2, r3][i]
        for j, value in enumerate(attribute):
            axes[1].text(positions[j], value + 3, f"{value}", 
                         ha='center', va='bottom')
    
    # Set y-axis limit for the second chart
    axes[1].set_ylim(0, 250)
    
    # Display the charts
    plt.show()


draw_graphs()
