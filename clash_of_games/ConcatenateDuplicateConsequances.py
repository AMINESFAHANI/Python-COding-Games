"""
Given a sequence with duplicate members like [1, ,1,2, 3, 4, 5], and an array of sub sequences like [[1,2], [3, 4],
[5]], return True or False if the given sequence could be constructed from given sub
sequences. The selected sub sequences would concatenate to construct exactly the
given sequence.
Example test cases:
(1). CanConstruct([1, 2, 3, 4, 5], [[1, 2], [3, 4], [5]]) == True
(2). CanConstruct([1, 3, 4, 5, 2], [[2, 3], [1, 3], [4, 2], [2], [4,
5]]) == True
"""
import copy

sequance=[1,1,2,3,4,5,3]
subSequance=[[1],[1,2],[2, 3], [3],[2], [4, 5]]
resualt=False

def duplicateSequanceCunsrtuctor(i=0,subSequance =subSequance):
        global resualt
        if not resualt:
            j=i+1
            for j in range(len(sequance)+1):
                if sequance[i:j] in subSequance:
                    if j==len(sequance):
                        resualt=True
                        break
                    else:
                        x=copy.deepcopy(subSequance)
                        x.remove(sequance[i:j])
                        duplicateSequanceCunsrtuctor(j,x)
        return resualt

print(duplicateSequanceCunsrtuctor())