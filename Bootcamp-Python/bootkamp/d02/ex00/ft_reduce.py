from functools import reduce

def ft_reduce(function_to_apply, list_of_inputs):
    if callable(function_to_apply) and hasattr(list_of_inputs, '__iter__') and len(list_of_inputs) > 1:
        res = function_to_apply(list_of_inputs[0], list_of_inputs[1])
        if len(list_of_inputs) > 2:
            for elem in list_of_inputs[2::]:
                res = function_to_apply(res, elem)
        return res
    return None

if __name__ == '__main__':
 
    res = reduce(lambda a,b: a + b, range(10))
    print(res)
    res = ft_reduce(lambda a,b: a + b, range(10))
    print(res)