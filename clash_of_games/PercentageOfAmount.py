"""
Input
        acidName: The name of the acid.
        acidCount: The number of drops of acid.
        waterCount: The number of drops of water
Output
        The percentage of acid in the solution (eg: 20%) and the acid name (if it is valid, else print "Unknown Acid").
        (Valid acid names: Hydrochloric, Sulfuric, Nitric, Citric)
        Round the the percentage to 1 decimal place (eg: 28.3%, 39.0%)
        Constraints
        Length of acidName > 0
"""

acidName= input()
acidcount= float(input())
waterCount= float(input())
def percentageOfAcid(acidName,acidCount,waterCount):
   if acidName not in ['Hydrochloric', 'Sulfuric', 'Nitric', 'Citric'] :
       acidName="Unknown Acid"
   return f'The percentage of {acidName} Acid in the solution is {100*acidcount/(acidcount+waterCount):.1f}%'

print(percentageOfAcid(acidName,acidcount,waterCount))

