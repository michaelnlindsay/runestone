# the answer is: ['c', 'a', 't', 'd', 'o', 'g', 'r', 'b', 'i']
wordlist = ['cat','dog','rabbit']
letterlist = []
letterlist = [ch for word in wordlist for ch in word if ch not in letterlist]
letterlist = [ch for word in wordlist for ch in word]
# for aword in wordlist:
#     for aletter in aword:
#         if aletter not in letterlist:
#             letterlist.append(aletter)
# print(letterlist)


wordlist = ['cat','dog','rabbit']
letterlist = {}
letterlist = [ch for word in wordlist for ch in word if ch not in letterlist]
letterlist = [ch for word in ['cat','dog','rabbit'] for ch in word]
letterlist = [ch for ch in "".join(['cat','dog','rabbit']) if ch not in letterlist]

ll = list(set(word[i] for word in ['cat','dog','rabbit'] for i in range(len(word))))

ll = []
ll = [word[i] for word in ['cat','dog','rabbit'] for i in range(len(word))]