def wordSquares(words):
    res = []
    for t in range(len(words)): 
        for l in range(len(words)):
            if words[t][0] == words[l][0] and words[t] != words[l]: 
                for r in range(len(words)): 
                    if words[t][3] == words[r][0]:
                        for b in range(len(words)):             
                            if words[b][3] == words[r][3] and words[b][0] == words[l][3] and words[b] != words[r]:
                                res.append([words[t], words[l], words[r], words[b]])
    return res            
    
    
print(wordSquares(words = ["avvj","dooe","exxj","diia"]))