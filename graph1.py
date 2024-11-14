import pandas as pd
import matplotlib.pyplot as plt
data=pd.read_csv("C://Users/Delll/Downloads/matches.csv")
matches_per_season= data.groupby('Season').size().reset_index(name='Match_Count')
print(matches_per_season)


plt.bar(matches_per_season['Season'], matches_per_season['Match_Count'])
plt.xlabel('Season')
plt.ylabel('Number of matches')
plt.title('Number of matches')
plt.show()