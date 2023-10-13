def make_clusters(rect):
    height,length = rect.shape
    clusters = []
    for i in range(length):
        j_prev = -1
        for j in range(height):
            if rect[j][i] == 1:
                if j_prev == -1:
                    j_prev = j
            else:
                if j_prev != -1:
                    clusters.append((i,j_prev,j-1))
                    j_prev = -1
    return clusters
