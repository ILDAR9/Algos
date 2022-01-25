from typing import List
import collections 

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        k = len(words)
        n = len(s)
        word_len = len(words[0])
        sublen = k * word_len
        answer = []
        word_dict = collections.Counter(words)

        def moving_window_search(left):
            wordcount = collections.defaultdict(int)
            is_exceed = False
            count_found = 0

            for right in range(left, n, word_len):
                if right + word_len > n:
                    break
            
                subword = s[right:right+word_len]
                if subword not in word_dict:
                    count_found = 0
                    left = right+word_len
                    wordcount = collections.defaultdict(int)
                    is_exceed = False
                    continue

                # disambiguation
                while is_exceed or right - left == sublen:
                    leftmostword = s[left:left + word_len]
                    wordcount[leftmostword] -= 1
                    left += word_len
                    if wordcount[leftmostword] == word_dict[leftmostword]:
                        # that's exceed
                        is_exceed = False
                    else:
                        # that's not excee but we must remove it
                        count_found -= 1

                wordcount[subword] += 1
                if wordcount[subword] > word_dict[subword]:
                    is_exceed = True
                else:
                    count_found += 1

                if not is_exceed and count_found == k:
                    nonlocal answer
                    answer.append(left)

        for i in range(word_len):
            moving_window_search(left=i)
        
        return answer


if __name__ == "__main__":
    inputs = [
        ("barfoothefoobarman", ["foo", "bar"]),
        ("wordgoodgoodgoodbestword", ["word", "good", "best", "word"]),
        ("barfoofoobarthefoobarman", ["bar", "foo", "the"]),
    ]
    outputs = [
        [0, 9],
        [],
        [6, 9, 12]
    ]

    sol = Solution()
    for (s, words), expected in zip(inputs, outputs):
        res = sol.findSubstring(s, words)
        assert sorted(res) == expected, f"{res} while expected {expected}"
        print('pass')
