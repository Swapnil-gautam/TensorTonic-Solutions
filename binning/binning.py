def binning(values, num_bins):
    """
    Assign each value to an equal-width bin.
    """
    # Write code here
    res = []
    w = (max(values) - min(values))/num_bins
    if(w == 0):
        return [0]*len(values)
    
    mi = min(values)
    for v in values:
        b = (v-mi)//w
        t = min(b, num_bins-1)
        res.append(t)

    return res