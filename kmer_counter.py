import heapq
import sys

NTS = ['A', 'T', 'G', 'C']

k_value = int(sys.argv[1])

kmers = {}
scaffolds = []
i = -1
with open(sys.argv[2], 'r') as f:
    for line in f:
        if line.startswith('>'):
            i += 1
            scaffolds.append('')
        else:
            scaffolds[i] += line.strip().upper()

for scaffold in scaffolds:
    for j in range(len(scaffold) - k_value + 1):
        kmer = scaffold[j:j+k_value]
        if not all(nt in NTS for nt in kmer):
            continue
        elif kmer in kmers:
            kmers[kmer] += 1
        else:
            kmers[kmer] = 1

max_heap = []
for key, value in kmers.items():
    max_heap.append((-value, key))
heapq.heapify(max_heap)

print(f"K-Value: {k_value}")
print("Top 10 k-mers:")
for i in range(10):
    neg_count, kmer = heapq.heappop(max_heap)
    count = -neg_count
    print(f"{i + 1}: K-mer: {kmer}, Count: {count}")

unique = 0
for item in kmers.values():
    if item != 0:
        unique += 1

print(f"Unique k-mers: {unique}")