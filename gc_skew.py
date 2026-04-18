import sys
import matplotlib.pyplot as plt

bp_window = int(sys.argv[1])

scaffolds = []
i = -1
with open(sys.argv[2], 'r') as f:
    for line in f:
        if line.startswith('>'):
            i += 1
            scaffolds.append('')
        else:
            scaffolds[i] += line.strip().upper()

gc_difference_count = []
genome_location = []

p = 0

for scaffold in scaffolds:
    for j in range(0, scaffold.__len__(), bp_window):
        g_count = 0
        c_count = 0
        for k in range(j, j + bp_window):
            if k >= len(scaffold):
                break
            if scaffold[k] == 'G':
                g_count += 1
            elif scaffold[k] == 'C':
                c_count += 1
        genome_location.append(p * bp_window)

        total_gc = g_count + c_count
        if total_gc == 0:
            gc_difference_count.append(0)
        else:
            gc_difference_count.append((g_count - c_count) / total_gc)
        if p > 0:
            gc_difference_count[p] += gc_difference_count[p - 1]
        p += 1

min_idx = gc_difference_count.index(min(gc_difference_count))
max_idx = gc_difference_count.index(max(gc_difference_count))

plt.title('GC Skew')
plt.xlabel('Genome Position (bp)')
plt.ylabel('(G - C) / (G + C)')
plt.axvline(x = genome_location[min_idx], color='r', linestyle='--')
plt.axvline(x = genome_location[max_idx], color='r', linestyle='--')
plt.plot(genome_location, gc_difference_count)
plt.show()