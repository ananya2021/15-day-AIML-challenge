studentbank = { 'ananya' : '932121202',
               'sujal' : '87458739',
               'vaishnavi': '8905869' ,
               'pari' : '6768686875',
               'satvik' : '896768976' , 
               'fgvhvjk' : '76896987'
               }
print("ananya's phone number is ", studentbank['ananya'])
studentbank['fgvhv'] = '876987098' 
print("fgvhv phone number is ", studentbank['fgvhv'])

sb = dict.copy(studentbank)
print("ananya's phone number is ", sb['ananya'])
b = dict.keys(sb)
print(b) 