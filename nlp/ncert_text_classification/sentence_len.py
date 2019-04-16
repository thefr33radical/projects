##Average Sentence Length Calculation Module
    #BEGIN

#Open a File, for multiple files put this in a loop
sentence = open("/home/deathwing/Documents/input.txt",'r',encoding = 'utf-8')
x=sentence.read()
print(x)

#Split into individual terms, including charecters which might not be a meaningful word
terms = x.split()

#Calculate the length of all the charecters in the file
s=0
for i in terms:
    s=s+len(i)
    
total_length=s
no_of_terms=len(terms)

#Find average by dividing total length of charecters by number of terms presesnt
average = total_length/no_of_terms
average

print("The average sentence length for the document is =",average)

    #END
