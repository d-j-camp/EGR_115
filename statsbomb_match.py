# pip install statsbombpy
from statsbombpy import sb
import plots_soccer_data as egrsoccer
import matplotlib.pyplot as plt
import pandas as pd

match_id = 3869685 # Arg vs France Final World Cup 2022
events = sb.events(match_id=match_id)

# keep only passes
passes = events[events['type'] == 'Pass'].copy()

# Location of passes w.r.t Pitch
passes[['x','y']] = pd.DataFrame(
    passes['location'].tolist(),
    index=passes.index
)

# End Location of passes w.r.t Pitch
passes[['end_x','end_y']] = pd.DataFrame(
    passes['pass_end_location'].tolist(),
    index=passes.index
)

# show all unique outcomes including NaN
print(passes['pass_outcome'].unique())

# Count total number per Pass Outcome
print(passes['pass_outcome'].value_counts(dropna=False))

# NaN values are for Complete Passes
passes['outcome_label'] = passes['pass_outcome'].fillna('Complete')

# Get Possesion Team
passes_arg = passes[passes['possession_team'] == 'Argentina']
passes_fra = passes[passes['possession_team'] == 'France']

img = "Horizontal_LightGreen_White.png"
fig1 = egrsoccer.plot_passes(passes_arg, "Argentina",img)
fig1.savefig("img_output/Argentina_passes.png")

fig2 = egrsoccer.plot_passes(passes_fra, "France",img)
fig2.savefig("img_output/France_passes.png")

# Filter shots
shots = events[events['type'] == 'Shot'].copy()

# Keep only shots on target (Goal or Saved)
shots_on_target = shots[shots['shot_outcome'].isin(['Goal', 'Saved'])]

# Extract shot coordinates
shots_on_target[['x','y']] = pd.DataFrame(shots_on_target['location'].tolist(), index=shots_on_target.index)

# Split by team
shots_arg = shots_on_target[shots_on_target['team'] == 'Argentina']
shots_fra = shots_on_target[shots_on_target['team'] == 'France']

fig3 = egrsoccer.plot_shots_side_by_side(shots_arg, shots_fra, img)
fig3.savefig("img_output/Argentina_France_shots_on_target.png")
plt.show()