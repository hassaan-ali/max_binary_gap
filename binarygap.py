def intToBin(n):
    binary = format(n, "b")
    return binary

    
def calcGap(bin):
    started = False
    max_gap = 0
    tmp_gap = 0

    for c in bin:
        if c == '1':
            max_gap = max(max_gap, tmp_gap)
            tmp_gap = 0
        else:
            tmp_gap += 1
    
    return max_gap

def solution(N):
    bin = intToBin(N)
    return calcGap(bin)
