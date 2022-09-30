from bisect import bisect_left

def lookup(x, xs, ys):
    if x <= xs[0]:  return ys[0]
    if x >= xs[-1]: return ys[-1]

    i = bisect_left(xs, x)
    k = (x - xs[i-1])/(xs[i] - xs[i-1])
    y = k*(ys[i]-ys[i-1]) + ys[i-1]

    return y
  
# testing
xs = [1, 2, 4, 8, 16, 32, 64, 128, 256]
ys = [0, 1, 2, 3, 4, 5, 6, 7, 8]
i_xs = [i/1000-500 for i in range(1000000)]

start_time = time.time()
ys = [lookup(x, xs, ys) for x in i_xs]
print("%s secs" % (time.time() - start_time))
