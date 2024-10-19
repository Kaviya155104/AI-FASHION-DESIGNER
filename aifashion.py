import matplotlib.pyplot as plt
import numpy as np

def draw_frock():
    # Create a figure and axis
    fig, ax = plt.subplots(figsize=(6, 8))

    # Draw the top part (bodice)
    bodice_x = [0.3, 0.7, 0.7, 0.3, 0.3]
    bodice_y = [1.0, 1.0, 0.7, 0.7, 1.0]
    ax.fill(bodice_x, bodice_y, color='lightblue', alpha=0.8, label='Bodice')

    # Draw the skirt part
    skirt_x = [0.3, 0.7, 0.9, 0.1, 0.3]
    skirt_y = [0.7, 0.7, 0.0, 0.0, 0.7]
    ax.fill(skirt_x, skirt_y, color='pink', alpha=0.6, label='Skirt')

    # Draw sleeves
    sleeve_left_x = [0.3, 0.1, 0.1, 0.3]
    sleeve_left_y = [0.9, 0.9, 0.7, 0.7]
    ax.fill(sleeve_left_x, sleeve_left_y, color='lightblue', alpha=0.8)

    sleeve_right_x = [0.7, 0.9, 0.9, 0.7]
    sleeve_right_y = [0.9, 0.9, 0.7, 0.7]
    ax.fill(sleeve_right_x, sleeve_right_y, color='lightblue', alpha=0.8)

    # Draw neckline
    neckline_x = [0.35, 0.65, 0.5, 0.35]
    neckline_y = [1.0, 1.0, 1.1, 1.0]
    ax.fill(neckline_x, neckline_y, color='lightblue', alpha=0.8)

    # Set limits and aspect
    ax.set_xlim(0, 1)
    ax.set_ylim(-0.2, 1.2)
    ax.set_aspect('equal')
    plt.axis('off')  # Turn off the axis
    plt.title("Simple Frock Structure")

    # Show the plot
    plt.show()

# Call the function to draw the frock
draw_frock()
