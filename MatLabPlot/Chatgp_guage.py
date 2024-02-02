import matplotlib.pyplot as plt
import numpy as np

def draw_vertical_half_gauge_with_ranges(value, max_value, red_range, yellow_range, title="Vertical Half Gauge with Ranges"):
    # Ensure value is within bounds
    value = max(0, min(value, max_value))

    # Create a figure and axis
    fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))

    # Set theta (angle) and r (radius) values for the vertical half-gauge display
    theta = np.linspace(-np.pi, 0, 100)
    r = np.linspace(0, 1, 100)

    # Plot the background vertical half-gauge arc
    ax.plot(theta, np.ones_like(theta), color='gray', linewidth=2)

    # Plot the colored ranges
    ax.fill_between(theta[:int(red_range/100 * len(theta))], 0, 1, color='red', alpha=0.5, label='Red Range')
    ax.fill_between(theta[int(red_range/100 * len(theta)):int(yellow_range/100 * len(theta))], 0, 1, color='yellow', alpha=0.5, label='Yellow Range')
    ax.fill_between(theta[int(yellow_range/100 * len(theta)):int(value/100 * len(theta))], 0, 1, color='green', alpha=0.5, label='Green Range')

    # Plot the filled area representing the vertical half-gauge value
    ax.fill_between(theta[:int(value/100 * len(theta))], 0, 1, color='green', alpha=0.7)

    # Plot the needle
    needle_length = 0.9
    needle_angle = np.deg2rad(-90 + (value / max_value) * 180)
    ax.plot([needle_angle, needle_angle], [0, needle_length], color='red', linewidth=2)

    # Add numbers to the gauge
    for i in range(0, max_value+1, 10):
        angle = np.deg2rad(-90 + (i / max_value) * 180)
        ax.text(angle, 1.2, str(i), ha='center', va='center', fontweight='bold', color='blue')

    # Set the title
    ax.set_title(title, va='bottom')

    # Remove axis labels and ticks
    ax.set_yticklabels([])
    ax.set_xticklabels([])
    ax.set_yticks([])
    ax.set_xticks([])

    # Display the vertical half-gauge with colored ranges
    plt.legend()
    plt.show()

# Example usage:
draw_vertical_half_gauge_with_ranges(value=75, max_value=100, red_range=30, yellow_range=70, title="Vertical Half Gauge with Ranges")
