import matplotlib.pyplot as plt
import numpy as np

steps = 10
num_tests = 100

res = []

with open('txt.txt', 'r') as f:
    data = f.readlines()
    line = 0
    for i in range(10, 110, 10):
        agg = 0
        for j in range(num_tests):
            agg += int(data[line])
            line += 1
        res.append(agg/num_tests)

x = list(range(10, 110, steps))
y = res

z = np.polyfit(x, res, 2)
# print(z)
p = np.poly1d(z)
plt.plot(x, y, 'o')
plt.plot(x, p(x),label = "Best fit 2 degree polynomial")

plt.title("#messages vs. #nodes in graph (GHS algo.) (Averaged over 100 runs)")
plt.xlabel("Number of nodes in fully connected graph")
plt.ylabel("Number of messages")

plt.legend()
# plt.show()

plt.savefig("Messages.svg")

plt.clf()
steps = 10
num_tests = 10

res = []

with open('txt2.txt', 'r') as f:
    data = f.readlines()
    line = 0
    for procs in range(1,13):
        times = []
        for i in range(10, 110, 10):
            temp = 0
            for num in range(num_tests):
                temp += float(data[line].split()[1])
                line += 3
            times.append(temp/num_tests)
        res.append(times)

x = list(range(10, 110, steps))
y = res

# z = np.polyfit(x, res, 2)
# print(z)
# p = np.poly1d(z)
# plt.plot(x, y, 'o')
# plt.plot(x, p(x),label = "Best fit 2 degree polynomial")

plt.title("Time taken vs. number of cores used (Averaged over 10 runs)")
plt.xlabel("Number of nodes in fully connected graph")
plt.ylabel("Time taken (in seconds)")

# for procs in range(1,13):
for procs in [1,2,4,8,12]:
    plt.plot(x,res[procs-1],label = str((procs))+' Cores')

plt.legend()
# plt.show()

plt.savefig("Time.svg")
