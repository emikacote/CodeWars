import sys
from collections import OrderedDict
sys.setrecursionlimit(2000)

class Array(object):
    seq = []
    def __init__(self, arr = []): self.arr = arr
    num_elements = lambda self: len(self.arr)
    num_values = lambda self: len(set(self.arr))
    start_end = lambda self: [self.arr[0], self.arr[-1]]  
    range_ = lambda self: [min(self.arr), max(self.arr)]
        
    def largest_increas_subseq(self, i=0, rev=0):
        new_seq = [self.arr[i]]
        for num in range(i+1, len(self.arr)):
            if self.arr[num] > self.arr[num-1]: new_seq.append(self.arr[num])
            else: break
        if (len(new_seq) > len(self.seq) and not rev) or (len(new_seq) >= len(self.seq) and rev):            
            self.seq = new_seq
        if len(self.arr)-(i+1) < len(self.seq):
                return self.seq if len(self.seq) >= 3 else "No increasing subsequence"
        return self.largest_increas_subseq(i+1, rev)
        
    def largest_decreas_subseq(self):
        self.arr = self.arr[::-1]
        self.seq = []
        dec_seq = self.largest_increas_subseq(rev = 1)
        self.arr = self.arr[::-1]
        return "No decreasing subsequence" if type(dec_seq) == str else dec_seq[::-1]
        
    def __str__(self):
        d = OrderedDict()
        d['1.number of elements'] = self.num_elements()
        d['2.number of different values'] = self.num_values()
        d['3.first and last terms'] = self.start_end()
        d['4.range of values'] = self.range_()
        d['5.increas subseq'] = self.largest_increas_subseq()
        d['6.decreas subseq'] = self.largest_decreas_subseq()
        return str(d)
