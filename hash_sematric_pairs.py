'''
 Given a list of number pairs.
 If pair(i,j) exist, and pair(j,i) exist report all such pairs.
'''

listing = {
    '1': '3',
    '3': '1',
    '2': '6',
    '4': '5',
    '7': '4',
    '5': '3',
    '8': '7'
}

pairs = [(key,value) for key,value in listing.items()]
answer = [(x,y) for (x,y) in pairs if (y,x) in pairs]
print(answer)
