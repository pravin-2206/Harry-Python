
def groupAnagrams(strs: list[str]) -> list[list[str]]:
    anagram_map = {}

    for s in strs:
        key = "".join(sorted(s))

        if key not in anagram_map:
            anagram_map[key] = []

        anagram_map[key].append(s)

    groups = []

    for group in anagram_map.values():
        group.sort()
        groups.append(group)

    groups.sort(key=lambda g: g[0])

    return groups

print(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))