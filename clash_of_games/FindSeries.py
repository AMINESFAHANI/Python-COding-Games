"""
 	Goal
You have a digital lock which can be opened typing a series of K digits from 0 - 9.
You can also type any digits before or after any member of the K digits,
the lock will open after typing each digit of K at least once in order.

Print yes or no whether the given T digits opens the lock.
"""
class FindSeries:
    def evaluate_Sesries(self):
        k=input()
        N=int(input())
        for i in range(N):
            T=input()
            j=0
            R="No"
            for x in T:
                if x==k[j]:
                    j+=1
                    if j==len(k):
                        R="Yes"
                        break
            print(R)

solution = FindSeries()
solution.evaluate_Sesries()


