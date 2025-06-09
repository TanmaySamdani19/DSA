import collections
import heapq
def reorganize_string(str):
        count = collections.Counter(s)
        maxHeap = [[-cnt, char] for char, cnt in count.items()]
        heapq.heapify(maxHeap)
        
        prev = None
        result = []
        
        while maxHeap or prev:
            if not maxHeap:
                return ""  # Cannot reorganize

            cnt, char = heapq.heappop(maxHeap)
            result.append(char)
            cnt += 1  # Since we store count as negative, adding 1 moves it toward 0

            if prev:
                heapq.heappush(maxHeap, prev)
                prev = None

            if cnt != 0:
                prev = [cnt, char]

        return ''.join(result)