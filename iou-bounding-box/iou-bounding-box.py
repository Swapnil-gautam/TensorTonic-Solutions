def iou(box_a, box_b):
    """
    Compute the Intersection over Union of two bounding boxes.
    """
    # Write code here
    
    if(box_b[0] > box_a[2] or box_b[1] > box_a[3] or
        box_b[1] > box_a[3] or box_b[3] < box_a[1]):
        return 0.0
        
    area_a = (box_a[2] - box_a[0]) * (box_a[3] - box_a[1])
    # print(area_a)
    area_b = (box_b[2] - box_b[0]) * (box_b[3] - box_b[1])
    # # print(area_b)
    
    # intersection =  (box_a[2] - box_b[0]) * (box_a[3] - box_b[1])
    # Intersection rectangle
    inter_x1 = max(box_a[0], box_b[0])
    inter_y1 = max(box_a[1], box_b[1])
    inter_x2 = min(box_a[2], box_b[2])
    inter_y2 = min(box_a[3], box_b[3])

    intersection = (inter_x2 - inter_x1) * (inter_y2 - inter_y1)
    # print(intersection)
    iou = intersection / (area_a + area_b - intersection)
    return iou
    pass