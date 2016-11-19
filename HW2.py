import mediacloud, datetime
import json, ast 

mc = mediacloud.api.MediaCloud('0a65d2b3a0780cf15a40ca6914fe2dfeed17257e30b440c0ddffdfbc179635cd')
wordsC = mc.wordCount('( Clinton )',  solr_filter=[mc.publish_date_query( datetime.date( 2016, 7, 1), datetime.date( 2016, 8, 1) ), 'tags_id_media:1' ] )
wordsT = mc.wordCount('( Trump )',  solr_filter=[mc.publish_date_query( datetime.date( 2016, 7, 1), datetime.date( 2016, 8, 1) ), 'tags_id_media:1' ] )


def mediaLove(PolName1, PolName2):

    
    #remove unicode and extract number of mentions and name for politician 1
    dict1 =  ast.literal_eval(json.dumps(PolName1[0] ))
    num_Mentions_polit1 = dict1['count']  
    dictN_polit1=  ast.literal_eval(json.dumps(PolName1[0] ))
    name_polit1 = dictN_polit1['term']  
    #remove unicode and extract number of mentions and name for politician 2
    dict2 =  ast.literal_eval(json.dumps(PolName2[0] ))
    num_Mentions_polit2 = dict2['count']  
    dictN_polit2 =  ast.literal_eval(json.dumps(PolName2[0] ))
    name_polit2 = dictN_polit2['term']     
    
    
    if (num_Mentions_polit1 > num_Mentions_polit2):
    
    
        print "In the month of September %s was mentioned more then %s in the media" % (name_polit1, name_polit2)
    
    else:
    
    
        print "In the month of September %s was mentioned more then %s in the media" % (name_polit2, name_polit1)

    
    return;

mediaLove(wordsC, wordsT)
