import json, re, collections
import typing as t

day_to_num = {"Mo": 0, "Di": 1, "Mi": 2, "Do": 3, "Fr": 4, "Sa": 5, "So": 6}
num_to_day = ["Mo", "Di", "Mi", "Do", "Fr", "Sa", "So"]

def json_read(path: str) -> t.Any:
    with open(path) as f: return json.load(f)

def fmt_hm(h: int, m: int) -> str:
    return str(h).zfill(2) + ":" + str(m).zfill(2)

def parse_hm(h_m: str) -> t.Tuple[int, int]:
    h, m = h_m.split(":", 1)
    return int(h), int(m)

def roman_to_latin_numbers(title: str) -> str:
    return (title
            .replace(" I ", " 1 ")
            .replace(" II ", " 2 ")
            .replace(" III ", " 3 ")
            .replace(" IV ", " 4 ")
            .replace(" V ", " 5 ")
            )

def remove_bracketed_part(title: str) -> str:
    return " ".join(re.match("([^(]*)(?:[(][^)]*[)])?(.*)", title).groups())

def from_stream(tuples: t.Iterator[t.Tuple]) -> t.Dict[t.Any, t.Any]:
    """
    Creates a nested dictionary structure, where the tuples are the path
    into the structure, and the last tuple element is the value.
    each tuple must have at least 2 components.
    example: [(1,'a'), (1,'b'), (2,3,4,'c')] --> {1:['a','b'],2:{3:{4:'c'}}}
    """
    result = collections.OrderedDict()
    for t in tuples:
        thing = result
        for k in t[:-2]:
            if k not in thing: thing[k] = collections.OrderedDict()
            thing = thing[k]
        if len(t) >= 2 and t[-2] not in thing: thing[t[-2]] = []
        thing[t[-2]].append(t[-1])
    return result

