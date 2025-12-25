import heapq

def huffman(freq):
    heap = [[f,[ch,""]] for ch,f in freq.items()]
    heapq.heapify(heap)

    while len(heap)>1:
        l=heapq.heappop(heap)
        r=heapq.heappop(heap)
        for p in l[1:]:
            p[1]="0"+p[1]
        for p in r[1:]:
            p[1]="1"+p[1]
        heapq.heappush(heap,[l[0]+r[0]]+l[1:]+r[1:])
    return sorted(heap[0][1:],key=lambda x:(len(x[1]),x))

print(huffman({'a':5,'b':9,'c':12,'d':13,'e':16,'f':45}))
