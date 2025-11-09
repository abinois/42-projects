def ft_map(function_to_apply, list_of_inputs):
    if callable(function_to_apply) and hasattr(list_of_inputs, '__iter__'):
       return [function_to_apply(elem) for elem in list_of_inputs]
    return None
            

if __name__ == '__main__':
    memes = ["It's over 9000 !", "All your base are belong to us."]
    res = list(map(str.upper , memes))
    print(memes)
    print(res)
    res = ft_map(str.upper , memes)
    print(res)
    print(memes)
