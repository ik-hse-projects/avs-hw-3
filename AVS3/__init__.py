UINT_MAX = 2**64 - 1
UINT_MIN = 0
INT_MAX = 2**63 - 1
INT_MIN = -2**63

def selection_sort_by_perimiter(shapes):
    for i in range(len(shapes)):
        smallest = i
        perimiter = shapes[i].perimiter()
        for j in range(i+1, len(shapes)):
            p = shapes[j].perimiter()
            if p < perimiter:
                smallest = j
                perimiter = p
        shapes[i], shapes[smallest] = shapes[smallest], shapes[i]
