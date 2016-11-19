
import mediacloud, datetime
import json, ast 
class MediaFrenzy:
    
    def __init__(self, tag):
        self.hashtag = tag;
      
    def load(self):
        mc = mediacloud.api.MediaCloud(self.hashtag)
        
    def getCount(self, word):
        return ast.literal_eval(json.dumps(word[0]))['count']
    def getName(self, name):
        return ast.literal_eval(json.dumps(name[0]))['term']

        
    
    def dataCount(self):    
        #remove unicode and extract number of mentions and name for politician 1
        self.dict1 =  ast.literal_eval(json.dumps(self.polit_data1[0] ))
        self.num_Mentions_polit1 = self.dict1['count']  
       
        self.dict2 =  ast.literal_eval(json.dumps(self.polit_data2[0] ))
        self.num_Mentions_polit2 = self.dict2['count'] 
    
    def dataName(self):    
        #remove unicode and extract number of mentions and name for politician 
        self.dictN_polit1=  ast.literal_eval(json.dumps(self.polit_data1[0] ))
        self.name_polit1 = self.dictN_polit1['term']  
    
        self.dictN_polit2=  ast.literal_eval(json.dumps(self.polit_data2[0] ))
        self.name_polit2 = self.dictN_polit2['term']  
    
    def checkMediaLove(self):
        
        
        if (self.polit_data1 > self.polit_data2):
            print "In the month of September %s was mentioned more then %s in the media" %(self.name_polit1, self.name_polit2)
        else:
            print "In the month of September %s was mentioned more then %s in the media" %(self.name_polit2, self.name_polit1)
    


