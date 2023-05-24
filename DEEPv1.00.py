#
# PYTHON CODE 
# 
# DEEP NUMBERS K11
#
# BY
#
# _Jacques Timmermans_
#
K = 11
MAX = 200
OEIS = ' '
for i in range(MAX) :
    Deep = 0
    for j in range(K) :
        Anal = (i % ( j + 1 ) )
        if ( Anal == 0 ):
            Deep = Deep + (2 ** j)
    DeepS = str(Deep) + ','
    OEIS += DeepS
print(OEIS,'...')
# END 
