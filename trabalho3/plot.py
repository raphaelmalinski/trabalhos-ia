import eight_queens as eq
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches


result, allGens = eq.run_ga_plot(60, 30, 4, 0.3, True)

print('Best candiadte:', result, 'with', eq.evaluate(result), 'colisions.')
print("Plot has been saved as 'ga.png'")

bestNumberConflits = []
worstNumberConflits = []
averageNumberConflits = []

for generation in allGens:

	conflicts = [eq.evaluate(a) for a in generation]
	
	bestNumberConflits.append(np.amin(conflicts))
	worstNumberConflits.append(np.amax(conflicts))
	averageNumberConflits.append(np.mean(conflicts))
	
plt.plot(bestNumberConflits,'g')
plt.plot(averageNumberConflits, 'y')
plt.plot(worstNumberConflits, 'r')
plt.xlabel('Generation')
plt.ylabel('Conflicts')

red_patch = mpatches.Patch(color='red', label='Worst')
green_patch = mpatches.Patch(color='green', label='Best')
yellow_patch = mpatches.Patch(color='yellow', label='Average')
plt.legend(handles=[red_patch,yellow_patch,green_patch])
plt.savefig('ga.png')

