import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# Define colors for outcomes
color_map = {
    "Complete": "blue",
    "Incomplete": "red",
    "Out": "orange",
    "Pass Offside": "purple"
}

# Function to plot Passes
def plot_passes(pass_df, team_name, img_path):
    # Load pitch image
    img = mpimg.imread(img_path)

    fig, ax = plt.subplots(figsize=(10,7))
    ax.imshow(img, extent=[0,120,0,80])

    # Unique outcomes
    outcomes = pass_df['outcome_label'].unique()

    for outcome in outcomes:
        subset = pass_df[pass_df['outcome_label'] == outcome]

        # Use color_map if available, else gray which corresponds to Unknown
        color = color_map.get(outcome, "gray")

        ax.scatter(
            subset['x'],
            subset['y'],
            color=color,
            label=outcome,
            s=30
        )

    ax.set_xlim(0,120)
    ax.set_ylim(0,80)
    ax.set_title(team_name + " Pass Outcomes")
    ax.legend(loc = "upper right")

    # plt.show()
    return fig

# Function to plot side-by-side Shots On Target
def plot_shots_side_by_side(shots_arg, shots_fra, img_path):
    img = mpimg.imread(img_path)
    
    fig, axes = plt.subplots(1, 2, figsize=(12,7))  # 1 row, 2 columns

    # France plot (left)
    ax = axes[0]
    ax.imshow(img, extent=[0,120,0,80])
    ax.scatter(shots_fra['x'], shots_fra['y'], color='red', label='France', s=100, edgecolors='white', alpha=0.8)
    ax.set_xlim(60,120)
    ax.set_ylim(0,80)
    ax.set_title("France Shots on Target")
    ax.legend()

    # Argentina plot (right)
    ax = axes[1]
    ax.imshow(img, extent=[0,120,0,80])
    ax.scatter(shots_arg['x'], shots_arg['y'], color='blue', label='Argentina', s=100, edgecolors='white', alpha=0.8)
    ax.set_xlim(60,120)
    ax.set_ylim(0,80)
    ax.set_title("Argentina Shots on Target")
    ax.legend()

    return fig
    # plt.show()