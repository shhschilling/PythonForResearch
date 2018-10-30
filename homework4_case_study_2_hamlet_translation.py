#------------------------------------------------
# Homework 4 of course "Python for Research"
# HarvardX -  PH526xEdX, EdX
# Hamlet translation
#------------------------------------------------

#Exercise 1--------------------------------------
import pandas as pd
hamlets = pd.DataFrame(columns=["language","text"])## Enter code here! ##
book_dir = "Books"
title_num = 1
for language in book_titles:
    for author in book_titles[language]:
        for title in book_titles[language][author]:
            if title=='Hamlet':
                inputfile = data_filepath+"Books/"+language+"/"+author+"/"+title+".txt"
                text = read_book(inputfile)
                hamlets.loc[title_num] = language, text
                title_num += 1
#Exercise 2--------------------------------------
language, text = hamlets.iloc[0]
def count_words_fast(text):
    import collections
    text=text.lower()
    skips=[".",";",",","!","?","''",'""',"%","$"]
    for char in skips:
        text=text.replace(char,"")
    word_counts=collections.Counter(text.split(" ")) #type: collections.Counter
    return(word_counts)

language, text = hamlets.iloc[0]

counted_text = count_words_fast(text)

data = pd.DataFrame({
    "word": list(counted_text.keys()),
    "count": list(counted_text.values())
})




#Exercise 3--------------------------------------

data["length"]=list(map(len,data["word"]))
column_word=data["word"]

def word_frequency(count):
    if (count>10):
        frequency="frequent"
    elif(1<count<=10):
        frequency="infrequent"
    else:
        frequency="unique"
    return(frequency)


data["frequency"]=list(map(word_frequency,data["count"]))

#Exercise 4--------------------------------------
language, text = hamlets.iloc[0]
counted_text = count_words_fast(text)

data = pd.DataFrame({
    "word": list(counted_text.keys()),
    "count": list(counted_text.values())
})

data["length"] = data["word"].apply(len)

data.loc[data["count"] > 10,  "frequency"] = "frequent"
data.loc[data["count"] <= 10, "frequency"] = "infrequent"
data.loc[data["count"] == 1,  "frequency"] = "unique"





sub_data=pd.DataFrame({"language": hamlets["language"]})
