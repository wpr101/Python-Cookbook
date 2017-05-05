def remainder(number, divisor):
    return number % divisor

assert remainder(20, 7) == 6

remainder(20,7)
remainder(20, divisor=7)
remainder(number=20, divisor=7)
remainder(divisor=7, number=20)

def flow_rate(weight_diff, time_diff, period=1):
    return (weight_diff / time_diff) * period

weight_diff = 0.5
time_diff = 3
flow = flow_rate(weight_diff, time_diff, 1)
print('%.3f kg per second' % flow)

flow_per_second = flow_rate(weight_diff, time_diff)
flow_per_hour = flow_rate(weight_diff, time_diff, period=3600)
