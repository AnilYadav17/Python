'''127. Group words that are anagrams from an array of strings.'''
# Arr = ["eat", "tea", "tan", "ate", "nat"] -> [["eat", "tea", "ate"], ["tan", "nat"]]
s_input = input("Enter words separated by spaces: ")
words = s_input.split()

grouped = []
visited = [False] * len(words)

for i in range(len(words)):
    if not visited[i]:
        current_group = [words[i]]
        visited[i] = True
        
        # Helper to sort characters manually
        w1_sorted = sorted(words[i])
        
        for j in range(i + 1, len(words)):
            if not visited[j] and len(words[i]) == len(words[j]):
                if w1_sorted == sorted(words[j]):
                    current_group.append(words[j])
                    visited[j] = True
        grouped.append(current_group)

print("Grouped Anagrams:", grouped)
