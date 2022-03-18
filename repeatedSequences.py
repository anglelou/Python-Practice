from pip import List


class Sequence:
    def findRepeatedDNAsequences(self, s:str) -> List[str]:
        seen, res = set(), set()

        for l in range(len(s) - 9):
            current = s[l:l+10]
            if current in seen:
                res.add(current)
            seen.add(current)
        return list(res)


if __name__== "__main__":

    s = Sequence()
    res = s.findRepeatedDNAsequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT")
    print(res)
    

