a = [8823421, 514005, 323446936, 79019, 44825350, 3541879, 5, 9, 93935, 0, 17, 5509405, 68958147, 79652294, 19869, 299928929, 5, 7795098, 36765389, 80579128, 6981]
result = 0
for i in range(len(a)):
    result = ((result + a[i]) * 113) % 10000007
print(result)
