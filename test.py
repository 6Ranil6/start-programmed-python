def dictinary():
    dictinary = dict(zip([1, 2, 3], ["Ranil", "Naill", "Vera"]))
    print(dictinary)
    print(dictinary.keys())
    print(dictinary.values())
    print(dictinary.items())
    print(dictinary.pop(1))
    print(dictinary)
    print(dictinary.popitem())
    print(dictinary)
    dictinary.clear()
    dictinary[1] = "Ranil"
    dictinary[1] = "NAil"
    print(dictinary)
    dictinary = { **{1: "ranil"}, **{2: "nail"}}
    print(dictinary)

def sets():
    set1 = {1, 2, 3}
    set1 = frozenset(set1)
    set2 = set([1, 2])
    print(set1, set2)
    set2.discard(0)
    set2.clear()
    print(set2)
    set2.add(2)
    set2.update({1, 5})
    print(set2)
    print(set2.union(set1)) # |
    print(set2.intersection(set1)) # &
    print(set2.difference(set1)) # -
    print(set2.symmetric_difference(set1)) # ^
    print(set2.issubset(set1)) # >=
    print(set2.issuperset(set1)) # <=
    
def paking():
    *age, = 38, 68
    dictinary = {
        1:"Ranil",
        2:"Vera"
    }
    
    print()

def string():
    word = "hello"
    print(word.isdigit(), word.isalnum(), word.isalpha(), word.isnumeric())
    print(word.isupper(), word.islower(), word.isspace())
    print("-" *  20)
    print(word.capitalize(), word.upper(), word.lower(), (word + " world").title())
    print(word.strip('h'))
    print("-" *  20)
    print(word.startswith("he"), word.endswith("ll"), word.split('l'), word.partition('l'), word.count('l'), word.replace(('l'), ('trash')))
    print(word.ljust(10), word.center(10, 'p'))

import re
def regex():
    word = "324 Ranil"
    pattern = re.compile(r"[a-z]+\d?", flags= re.IGNORECASE)
    print(re.match(pattern, word))
    print(re.search(pattern, word).group())
    print(re.sub(pattern, "Nail", word ))
    print(re.fullmatch(pattern, word))
    print(re.findall(pattern, word))
    print(re.split(pattern, word))
    print(re.escape(word))

def main():
    # dictinary()
    sets()
    # paking()
    # string()
    # regex()

if __name__ == "__main__":
    main()