# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
    value = 0.
    # write your code here
    #import pdb; pdb.set_trace()
    unit_value = [values[i]/weights[i] for i in range(len(values))]
    while capacity>0:
        max_index = unit_value.index(max(unit_value))
        if capacity - weights[max_index] < 0:
            weights[max_index] -= capacity
            value += unit_value[max_index] * capacity
            return value
        else:
            capacity -= weights[max_index]
            unit_value.pop(max_index)
            weights.pop(max_index)
            value += values[max_index]
            values.pop(max_index)
            if weights == []:
                return value

    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
