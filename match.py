def match(ref, input):
    output = [None for _ in range(len(ref))]
    output_index = [0 for _ in range(len(ref))]
    for i in range(len(ref)):
        closest = 0
        dist = abs(ref[i][1] - input[closest][1])
        for j in range(len(input)):
            if abs(ref[i][1] - input[j][1]) < dist:
                dist = abs(ref[i][1] - input[j][1])
                closest = j
        output[i] = input[closest]
        output_index[i] = closest
    
    for i in range(len(output_index)):
        for j in range(i+1, len(output_index)):
            if output_index[i] == output_index[j]:
                output[i] = None
                output_index[i] = -1
            break
    
    return output