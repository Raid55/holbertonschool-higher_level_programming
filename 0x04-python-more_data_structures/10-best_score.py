#!/usr/bin/python3
def best_score(my_dict):
    if my_dict is None:
        return None
    max_score = max(zip(my_dict.values(), my_dict.keys()))
    if isinstance(max_score[0], int) is False:
        return None
    return max_score[1] if max_score[1] else None
