def precision_recall_at_k(recommended, relevant, k):
    """
    Compute precision@k and recall@k for a recommendation list.
    """
    # Write code here
    t = k;
    rink = 0
    for r in recommended:
        if(t == 0):
            break
        
        if(r in relevant):
            rink = rink + 1

        t = t - 1

    precision = rink/k
    recall = rink/len(relevant)
    
    return [precision, recall]