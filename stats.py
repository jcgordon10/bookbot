from typing import Dict, List

def get_num_words(text: str) -> int:
    words = text.split()
    num_words = len(words)
    return num_words


def get_num_char(text: str) -> Dict[str ,int]:
    text = text.lower()
    chars_counts: Dict[str ,int] = {}
    for char in text:
        if char.isalpha():
            if char in chars_counts:
                chars_counts[char] += 1
            else:
                chars_counts[char] = 1
    return chars_counts


def sort_on(d):
    return d["num"]


def sorted_dicts(chars_counts: Dict[str ,int]) -> List[Dict[str, object]]:
    sorted_list = []
    for k in chars_counts:
        sorted_list.append({"char": k, "num": chars_counts[k]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list