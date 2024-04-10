'''
In an alien language, surprisingly, they also use English lowercase letters, but possibly in a different order. The order of the alphabet is some permutation of lowercase letters.

Given a sequence of words written in the alien language, and the order of the alphabet, return true if and only if the given words are sorted lexicographically in this alien language.


Example 1:

Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
Output: true
Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.
Example 2:

Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
Output: false
Explanation: As 'd' comes after 'l' in this language, then words[0] > words[1], hence the sequence is unsorted.
Example 3:

Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
Output: false
Explanation: The first three characters "app" match, and the second string is shorter (in size.) According to lexicographical rules "apple" > "app", because 'l' > '∅', where '∅' is defined as the blank character which is less than any other character (More info).
 

Constraints:

1 <= words.length <= 100
1 <= words[i].length <= 20
order.length == 26
All characters in words[i] and order are English lowercase letters.
'''



class Solution:
    def isAlienSorted(self, words, order):

        index = 0

        def dfs(word1, word2, index1, index2):
            
            #this dfs function should terminate either when the the current comparisson is invalid open OR
            #we are the end but the length of word2 < word1

            if order.index(word1[index1]) > order.index(word2[index2]):
                return False

            if order.index(word1[index1]) == order.index(word2[index2]) and index2 == len(word2)-1  and len(word1) > len(word2):
                return False

            if order.index(word1[index1]) <= order.index(word2[index2]) and index1 == len(word1)-1 and len(word1) <= len(word2):
                return True
            
            
            return dfs(word1, word2, index1+1, index2+1)


        while index < len(words)-1:


            current_word = words[index]
            next_word = words[index+1]
            print(index)
            print("here")

            if order.index(current_word[0]) < order.index(next_word[0]):
                index += 1
                continue
            elif order.index(current_word[0]) == order.index(next_word[0]):
                 #do further search
                 ret = dfs(current_word, next_word, 1,1)
                 index += 1

                 if not ret:
                    return False      
            else:
                return False
            
        
        return True

sol = Solution()
words = [["hello","leetcode"], ["apple","app"], ["word","world","row"], ["apple", "banana", "cherry", "date", "fig"], ["apple", "fig", "cherry", "date", "basil"]]
orders = ["hlabcdefgijkmnopqrstuvwxyz", "abcdefghijklmnopqrstuvwxyz", "worldabcefghijkmnpqstuvxyz", "abcdefghijklmnopqrstuvwxyz", "abcdefghijklmnopqrstuvwxyz"]


for word, order in zip(words, orders):
    print(word, order)
    print(sol.isAlienSorted(word, order))

'''
Expected results for each word/order combination:
    # ["hello","leetcode"], "hlabcdefgijkmnopqrstuvwxyz" -> True
    # ["apple","app"], "abcdefghijklmnopqrstuvwxyz" -> False
    # ["word","world","row"], "worldabcefghijkmnpqstuvxyz" -> False
    # ["apple", "banana", "cherry", "date", "fig"], "abcdefghijklmnopqrstuvwxyz" -> True
    # ["apple", "fig", "cherry", "date", "basil"], "abcdefghijklmnopqrstuvwxyz" -> True
'''

        
        