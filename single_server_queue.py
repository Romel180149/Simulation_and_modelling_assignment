import numpy as np
import matplotlib.pyplot as plt

# Simulation Parameters
arrival_rate = 5  # Average arrivals per unit time (lambda)
service_rate = 6  # Average services per unit time (mu)
simulation_time = 1000  # Total simulation time

# Initialize System State
time = 0  # Simulation clock
queue = 0  # Number of customers in the system
arrival_times = []  # Record of arrival times
departure_times = []  # Record of departure times

# Generate interarrival and service times (i.i.d random variables)
# Interarrival times are i.i.d. exponential random variables with mean 1/lambda
interarrival_times = np.random.exponential(1 / arrival_rate, size=simulation_time)
# Service times are i.i.d. exponential random variables with mean 1/mu
service_times = list(np.random.exponential(1 / service_rate, size=simulation_time))

for i in range(simulation_time):
    if i == 0:
        arrival_times.append(interarrival_times[i])
    else:
        arrival_times.append(arrival_times[-1] + interarrival_times[i])

# Process each arrival and determine departure times
for arrival in arrival_times:
    if len(departure_times) == 0 or arrival >= departure_times[-1]:
        # No queue, serve immediately
        departure_times.append(arrival + service_times.pop(0))
    else:
        # Customer waits in the queue
        departure_times.append(departure_times[-1] + service_times.pop(0))

# Calculate system statistics
waiting_times = np.array(departure_times) - np.array(arrival_times)
queue_lengths = np.maximum(0, np.arange(len(arrival_times)) - np.searchsorted(departure_times, arrival_times))

# Visualization
plt.figure(figsize=(10, 5))
plt.plot(arrival_times, queue_lengths, label='Queue Length')
plt.xlabel('Time')
plt.ylabel('Number of Customers in Queue')
plt.title('Single Server Queue Simulation (M/M/1)')
plt.legend()
plt.savefig("plot.png")

plt.show()

# Print Results
print(f"Average waiting time: {np.mean(waiting_times):.2f} units")
print(f"Maximum queue length: {np.max(queue_lengths)} customers")