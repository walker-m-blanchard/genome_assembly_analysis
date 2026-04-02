import sys
import matplotlib.pyplot as plt

k_value = int(sys.argv[1])

scaffolds = ['']
i = 0
with open(sys.argv[2], 'r') as f:
    for line in f:
        if line.startswith('>'):
            i += 1
            scaffolds.append('')
        else:
            scaffolds[i] += line.strip()

gc_difference_count = []
gc_total_count = []
genome_location = []

p = 0

for i in range(1, len(scaffolds)):
    for j in range(0, scaffolds[i].__len__(), k_value):
        g_count = 0
        c_count = 0
        for k in range(j, j + k_value):
            if k >= len(scaffolds[i]):
                break
            if scaffolds[i][k] == 'G':
                g_count += 1
            elif scaffolds[i][k] == 'C':
                c_count += 1
        genome_location.append(p * k_value)
        gc_difference_count.append((g_count - c_count) / (g_count + c_count))
        if p > 0:
            gc_difference_count[p] += gc_difference_count[p - 1]
            gc_total_count[p] += gc_total_count[p - 1]
        p += 1

plt.plot(genome_location, gc_difference_count)
plt.show()

min_idx = gc_difference_count.index(min(gc_difference_count))
max_idx = gc_difference_count.index(max(gc_difference_count))
print(f"Origin bp location: {min_idx * k_value}")
print(f"Terminus bp location: {max_idx * k_value}")