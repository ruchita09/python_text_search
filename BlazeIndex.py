import sys
import csv
import json
import nltk
import stopwords
from nltk.corpus import stopwords
import pandas as pd


class TextSearch():

    def __init__(self):

        self.documents = []
        self.dFrameDocuments = pd.DataFrame(self.documents)

        self.invertedindex = dict()
        self.invertedpath = os.path.join('/InvertedIndex.csv')
        self.documentpath = os.path.join('/Documents.csv')
        
        # Read Inverted Index to dictionary    
        #Create an Index if it does not exist already
        with open(self.invertedpath, mode='a+') as csvfile:
            flag = 0

        with open(self.invertedpath, mode='r') as infile:
            reader = csv.reader(infile)
            for rows in reader:
                if not rows:
                    self.invertedindex = {}
                if rows:
                    self.invertedindex[rows[0]] = rows[1]


    def Add(self,doc):
        flag = 0

        #Format the input string to a proper json format
        formatted_json = (doc.replace("{", "{\"").replace(":", "\":\"").replace("}", "\"}").replace(",", "\",\"").replace("'",""))

        #Read the Json to python
        json_doc = dict(json.loads(formatted_json))

        #Write the Json document to a csv file, Create one if it does not exist already
        with open(self.documentpath, 'a+') as csvfile:
             flag = 0

        with open(self.documentpath, 'r') as csvfile:
             csv_dict = [row for row in csv.DictReader(csvfile)]
             if len(csv_dict) == 0:
                 flag = 1

        f = csv.writer(open(self.documentpath, "ab+"))
        if(flag == 1):
             f.writerow(["id", "text"]) #Header for csv file
        f.writerow([json_doc['id'],json_doc['text']])


        #Creating tokens and normalising them, removing stopwords as well

        stop_words = nltk.download('stopwords')

        stop_words = (stopwords.words('english'))

        norm_tokens = []

        tokens = json_doc['text'].split()  # split string into a list

        for temp in tokens:
             temp = temp.lower()
             if temp not in stop_words:
                 norm_tokens.append(temp)

        index = []

        #Add/Update the index with new tokens
        for token in norm_tokens:
            if token in self.invertedindex.keys():
                self.invertedindex[token] = (self.invertedindex[token] + "/" + json_doc['id'])
            else:
                self.invertedindex[token] = json_doc['id']

        #Save the index to csv file
        with open(self.invertedpath, 'w') as f:
             for key in self.invertedindex.keys():
                 f.write("%s,%s\n" % (key, self.invertedindex[key]))

        print("Added" + " " + formatted_json)

        return self.dFrameDocuments, self.documents


    #Function for querying the data provided
    def Query(self, words):

        length = len(words)

        #Formatting the input
        words[0] = words[0].replace("'","")
        words[length-1] = words[length-1].replace("'","")

        for i in range(length):
            words[i] = words[i].lower()

        #Search the inverted index

        result = dict()

        for word in words:
            if word in self.invertedindex.keys():
                docs = self.invertedindex[word]
                docs = docs.split("/")

                for doc in docs:
                    if doc in result.keys():
                        result[doc] = result[doc]+1
                    else:
                        result[doc]=1


        #Sort the result obtained according to relevancy of documents
        result = sorted(result.iteritems(),key = lambda x : x[1], reverse=True)

        len_result = len(result)

       # Reading the Documents file for getting the result

        tempdocs = []

        with open(self.documentpath, 'r') as f:
             for i in range(len_result):
                 f.seek(0,0)
                 reader = csv.DictReader(f)
                 for row in reader:
                    tempobj = dict(row)
                    if(int(tempobj['id'])==int(result[i][0])):
                        tempobj['id'] = (tempobj['id'])
                        tempobj['text'] = tempobj['text']
                        tempdocs.append(tempobj)

        self.documents = tempdocs

        print(json.dumps({"count": len(self.documents),"documents": self.documents}))

        return self.documents



t=TextSearch()
if (sys.argv[1] == "add"):
    t.Add(sys.argv[2])


if (sys.argv[1] == "query"):
    t.Query(sys.argv[2:])
