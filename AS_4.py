
string = "A great great place."
lstring = string.lower()
vowel_counts = {}
for vowel in "aeiou":
    count = lstring.count(vowel)
    vowel_counts[vowel] = count
print(vowel_counts)
for i in sorted (vowel_counts.keys()) :  
     print(i, end = " ") 
     print(vowel_counts[i])
     
