import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation
from heapq import nlargest
text="""After learning the harmful effects of pollution, one must get on the task of preventing or reducing pollution as soon as possible. To reduce air pollution, people should take public transport or carpool to reduce vehicular smoke. While it may be hard, avoiding firecrackers at festivals and celebrations can also cut down on air and noise pollution. Above all, we must adopt the habit of recycling. All the used plastic ends up in the oceans and land, which pollutes them.



So, remember to not dispose of them off after use, rather reuse them as long as you can. We must also encourage everyone to plant more trees which will absorb the harmful gases and make the air cleaner. When talking on a bigger level, the government must limit the usage of fertilizers to maintain the soil’s fertility. In addition, industries must be banned from dumping their waste into oceans and rivers, causing water pollution.

To sum it up, all types of pollution is hazardous and comes with grave consequences. Everyone must take a step towards change ranging from individuals to the industries. As tackling this problem calls for a joint effort, so we must join hands now. Moreover, the innocent lives of animals are being lost because of such human activities. So, all of us must take a stand and become a voice for the unheard in order to make this earth pollution-free."""
def summarizer(rawtext):
    stopwords=list(STOP_WORDS)
    #print(stopwords)
    nlp=spacy.load('en_core_web_sm')
    doc=nlp(rawtext)
    #print(text)
    tokens=[token.text for token in doc]
    word_freq={}
    for word in doc:
        if word.text.lower() not in stopwords and word.text.lower() not in punctuation:
            if word.text not in word_freq.keys():
                word_freq[word.text]=1
            else:
                word_freq[word.text]+=1

            
    #print(word_freq)
    maxfreq=max(word_freq.values())
    #print(maxfreq)
    for word in word_freq.keys():
        word_freq[word]=word_freq[word]/maxfreq

    #print(word_freq)
    sent_tokens=[sent for sent in doc.sents]
    #print(sent_tokens)
    sent_scores={}
    for sent in sent_tokens:
        for word in sent:
            if word.text in word_freq.keys():
                if sent not in sent_scores.keys():
                    sent_scores[sent]=word_freq[word.text]
                else:
                    sent_scores[sent]+=word_freq[word.text]

    print(sent_scores)
    select_len=int(len(sent_tokens)*0.4)
    print(select_len)
    summary=nlargest(select_len,sent_scores,key=sent_scores.get)
    #print(summary)
    final_summary=[word.text for word in summary]
    summary=' '.join(final_summary)
    #Print(summary)
    return summary,doc,len(rawtext.split(' ')),len(summary.split(' ')) 
