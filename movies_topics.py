from nltk.tokenize import RegexpTokenizer
from stop_words import get_stop_words
from nltk.stem.porter import PorterStemmer
from gensim import corpora, models
import gensim

tokenizer = RegexpTokenizer(r'\w+')

# create English stop words list
en_stop = get_stop_words('en') + ['Allison', 'bruno', 'george','Arthur','Ana','Alex','Arlene','Alberto','Barry','Bertha','Bill','Bonnie','Bret','Beryl','Chantal','Cristobal','Claudette','Charley','Cindy','Chris','Dean','Dolly','Danny','Danielle','Dennis','Debby','Erin','Edouard','Erika','Earl','Emily','Ernesto','Felix','Fay','Fabian','Frances','Franklin','Florence','Gabielle','Gustav','Grace','Gaston','Gert','Gordon','Humberto','Hanna','Henri','Hermine','Harvey','Helene','Iris','Isidore','Isabel','Ivan','Irene','Isaac','Jerry','Josephine','Juan','Jeanne','Jose','Joyce','Karen','Kyle','Kate','Karl','Katrina','Kirk','Lorenzo','Lili','Larry','Lisa','Lee','Leslie','Michelle','Marco','Mindy','Maria','Michael','Noel','Nana','Nicholas','Nicole','Nate','Nadine','Olga','Omar','Odette','Otto','Ophelia','Oscar','Pablo','Paloma','Peter','Paula','Philippe','Patty','Rebekah','Rene','Rose','Richard','Rita','Rafael','Sebastien','Sally','Sam','Shary','Stan','Sandy','Tanya','Teddy','Teresa','Tomas','Tammy','Tony','Van','Vicky','Victor','Virginie','Vince','Valerie','Wendy','Wilfred','Wanda','Walter','Wilma','William','Kumiko','Aki','Miharu','Chiaki','Michiyo','Itoe','Nanaho','Reina','Emi','Yumi','Ayumi','Kaori','Sayuri','Rie','Miyuki','Hitomi','Naoko','Miwa','Etsuko','Akane','Kazuko','Miyako','Youko','Sachiko','Mieko','Toshie','Junko', 'allison','arthur','ana','alex','arlene','alberto','barry','bertha','bill','bonnie','bret','beryl','chantal','cristobal','claudette','charley','cindy','chris','dean','dolly','danny','danielle','dennis','debby','erin','edouard','erika','earl','emily','ernesto','felix','fay','fabian','frances','franklin','florence','gabielle','gustav','grace','gaston','gert','gordon','humberto','hanna','henri','hermine','harvey','helene','iris','isidore','isabel','ivan','irene','isaac', 'jerry', 'josephine', 'juan', 'jeanne', 'jose', 'joyce','karen','kyle','kate','karl','katrina','kirk','lorenzo','lili','larry','lisa','lee','leslie','michelle','marco','mindy','maria','michael','noel','nana','nicholas','nicole','nate','nadine','olga','omar','odette','otto','ophelia','oscar', 'pablo','paloma','peter','paula','philippe','patty', 'rebekah', 'rene', 'rose', 'richard', 'rita', 'rafael','sebastien','sally','sam','shary','stan','sandy','tanya','teddy','teresa','tomas','tammy','tony','van','vicky','victor','virginie','vince','valerie','wendy','wilfred','wanda','walter','wilma','william','kumiko','aki','miharu','chiaki','michiyo','itoe','nanaho', 'reina','emi','yumi','ayumi','kaori','sayuri', 'rie','miyuki','hitomi','naoko','miwa','etsuko','akane','kazuko','miyako','youko','sachiko','mieko','toshie', 'junko','joey']
# Create p_stemmer of class PorterStemmer
p_stemmer = PorterStemmer()
    
# create sample documents

stream = open('processed/movies.dat')
doc_set = []
for line in stream.readlines():
    movie = line.split('::')
    doc_set.append(movie[3].replace("'",""))

# list for tokenized documents in loop
texts = []

# loop through document list
for i in doc_set:
    
    # clean and tokenize document string
    raw = i.lower()
    tokens = tokenizer.tokenize(raw)

    # remove stop words from tokens
    stopped_tokens = [i for i in tokens if not i in en_stop]
    
    # stem tokens
    # stemmed_tokens = [p_stemmer.stem(i) for i in stopped_tokens]
    
    # add tokens to list
    texts.append(stopped_tokens)

# turn our tokenized documents into a id <-> term dictionary
dictionary = corpora.Dictionary(texts)
    
# convert tokenized documents into a document-term matrix
corpus = [dictionary.doc2bow(text) for text in texts]

# generate LDA model
ldamodel = gensim.models.ldamodel.LdaModel(corpus, num_topics=50, id2word = dictionary, alpha = 'auto' ,  eval_every = 5)
print(ldamodel.print_topics(num_topics=50, num_words=5))
