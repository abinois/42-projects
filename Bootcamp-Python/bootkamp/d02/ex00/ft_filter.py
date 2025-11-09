def ft_filter(function_to_apply, list_of_inputs):
    if callable(function_to_apply) and hasattr(list_of_inputs, '__iter__'):
        return [elem for elem in list_of_inputs if function_to_apply(elem)]
    return None

if __name__ == '__main__':
    memes = ["It's over 9000 !", "All your base are belong to us."]
    res = list(filter(lambda elem: True if '9' in elem else False , memes))
    print(memes)
    print(res)
    res = ft_filter(lambda elem: True if '9' in elem else False, memes)
    print(memes)
    print(res)
    