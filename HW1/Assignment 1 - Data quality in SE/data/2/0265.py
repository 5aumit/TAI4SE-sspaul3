import pandas as pd
import plot_nn
from plot_nn import plot_nn_fake
import numpy as np 
from matplotlib import pyplot as plt

nu_max=np.arange(1980,3000,4)
for nu in range(nu_max.size):
	path="/home/rakesh/Fake_Data/MultiTrip/Spec_numax_%d.csv"%nu_max[nu]
	df=pd.read_csv(path)
	plot_nn_fake(df)
	plt.savefig("/home/rakesh/Plots/28Jan/Train/numax_%d.png"%nu_max[nu])
	plt.close()



