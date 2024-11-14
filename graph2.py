import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv("C://Users/Delll/Downloads/matches.csv")
rcb_matches = data[(data['Team1'] == 'Royal Challengers Bangalore') | (data['Team2'] == 'Royal Challengers Bangalore')]
matches_played = rcb_matches.groupby('Season').size().reset_index(name='Matches_Played')
matches_won = rcb_matches[rcb_matches['Winner'] == 'Royal Challengers Bangalore']
matches_won = matches_won.groupby('Season').size().reset_index(name='Matches_Won')
season_stats = pd.merge(matches_played, matches_won, on='Season', how='left')
season_stats['Matches_Won'].fillna(0, inplace=True)
print(season_stats)
plt.figure(figsize=(12, 6))

# Create a bar plot with two bars for each season: Matches Played and Matches Won
bar_width = 0.35
index = range(len(season_stats))

plt.bar(index, season_stats['Matches_Played'], bar_width, label='Matches Played', color='skyblue')
plt.bar([i + bar_width for i in index], season_stats['Matches_Won'], bar_width, label='Matches Won', color='green')
plt.xlabel('Season', fontsize=12)
plt.ylabel('Number of Matches', fontsize=12)
plt.title('Matches Played and Won by Royal Challengers Bangalore per Season', fontsize=14)

# Adjust the x-axis to show the season names
plt.xticks([i + bar_width / 2 for i in index], season_stats['Season'], rotation=45, ha='right')

# Add a legend
plt.legend()
plt.tight_layout()
plt.show()