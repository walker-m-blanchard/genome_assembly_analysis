import heapq
import sys

NTS = ['A', 'T', 'G', 'C']

def build_kmer(n, counter, prefix):
    if n == 0:
        counter[prefix] = 0
    else:
        for nt in NTS:
            new_kmer = prefix + nt
            build_kmer(n - 1, counter, new_kmer)

k_value = int(sys.argv[1])

kmers = {}
build_kmer(k_value, kmers, '')

scaffolds = ['']
i = 0
with open(sys.argv[2], 'r') as f:
    for line in f:
        if line.startswith('>'):
            i += 1
            scaffolds.append('')
        else:
            scaffolds[i] += line.strip()

for i in range(len(scaffolds)):
    for j in range(len(scaffolds[i])):
        if scaffolds[i][j:j+k_value] in kmers:
            kmers[scaffolds[i][j:j+k_value]] += 1

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