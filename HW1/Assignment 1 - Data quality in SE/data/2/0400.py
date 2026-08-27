import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

for i in range(0, 1000):
    df = pd.read_hdf("LAr_Env.h5", key='data')
    time = np.array(df['Time'], dtype=float)
    time = time/60
    plt.figure(0)
    press = np.array(df['Pressure (arb)'], dtype=float)
    plt.plot(time, press, color='blue')
    plt.xlabel("Time (min)")
    plt.ylabel("Pressure (arb)")

    plt.figure(2)
    flow = np.array(df['Flow (L)'], dtype=float)
    flow = 1000*(flow/784)
    print("Liquid Volume: ", flow[-1])
    plt.plot(time, flow)
    plt.figure(3)
    temp = np.array(df['Temperature (K)'], dtype=float)
    plt.ylabel("Temperature (K)")
    plt.xlabel("Time (min)")
    plt.plot(time, df['Temperature (K)'], color='blue')
    #plt.pause(30)
    plt.show()
'''
plt.figure(2)
print(df.columns)
press = np.array(df['Pressure (arb)'])
print(press[-40:])
plt.plot(df['Pressure (arb)'])
'''
plt.show()
