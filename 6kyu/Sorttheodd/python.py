def sort_array(source_array):
    odds = sorted((x for x in source_array if x%2), reverse=True)
    return [x if x%2==0 else odds.pop() for x in source_array]
