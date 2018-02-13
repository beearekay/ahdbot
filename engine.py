
##dict of response for each type of intent
intent_response_dict = {
    "intro": ["This is a EDPI FAQ bot. One stop-shop to all your EDPI related queries"],
    "greet":["Hey","Hello","Hi"],
    "goodbye":["Bye","It was nice talking to you","See you","ttyl"],
    "affirm":["Cool","I know you would like it"]
}

edpifaq_response_dict = {    
    #"edpi_intro": "EDPI is an Enterprise Data Platform Interface. Once onboarded consumers can access AM/WM Data from predefined Data towers. Choose from below two options <br/><br/><html><body><form action=\"http://localhost:5000\" method=\"POST\"><div class=\"btn btn-info btn-lg\">AM EDPI</div>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<div class=\"btn btn-info btn-lg\">WM EDPI</div></form></body></html>",
    "edpi_intro": "EDPI is an Enterprise Data Platform Interface. Once onboarded consumers can access AM/WM Data from predefined Data towers. Choose one from below <br/><br/><html><body><form action=\"http://127.0.0.1:8080/result\" method=\"POST\"><input type=\"submit\" name=\"submit\" class=\"btn btn-info btn-lg active\" value=\"AM EDPI\">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<input type=\"submit\" name=\"submit\" class=\"btn btn-info btn-lg active\" value=\"WM EDPI\"> </form></body></html>",
    "benefits":"EDPI is a data distribution layer for AWM which acts as golden source",
    "faq_link":'You can check all the answers here AM EDPI: <a href=\"go/edpi\"</a>, WM EDPI:\"<a href=\"go/edpiwm\"</a>',
    #"reference":"You want EDPI reference data ... visit Data model browser",
    "reference": " Which LOB?Options:AM#WM",
    "AM_reference": "v0#v1#v2",
    "WM_reference": "v3#v4#v5",
    "AM_reference_v0": "<html><body> <a href = 'abc.com'>abc</a></body></html>",
    "benefits":"GST consumes more than a dozen taxes, thus making it hassle free and efficient.",
    "faq_link":'You can check all the answers here http://www.cbec.gov.in/resources//htdocs-cbec/deptt_offcr/faq-on-gst.pdf'
}

entitlements_info_response_dict = {
    "entitlements_intro": "EDPI Needs two types of entitlements. One is for accessing the EDPI UI to onboard and build queries. Another type is to access the data using the built stored queries",
    "me@edpi": "One Needs EDPI Consumer entitlements to onboard and build queries."
}


data_access_dict = {
   
}

edpi_query_value_dict = {
    "faq_link":'You can check all the answers here AM EDPI: <a href=\"go/edpi\", WM EDPI:\"<a href=\"go/edpiwm\"</a>'
}

def general_response(intent):
    print(" ########## ",intent," ################")
    return intent_response_dict[intent]

'''def data_access(entities):
    #print("hello world")
    print ("entities-->" + entities)
    if entities == None:
        return "Could not find out specific information about this ..." +  gstinfo_response_dict["faq_link"]
    else:
        print(data_access_dict[entities])
        return data_access_dict[entities]
    return "Sorry.." + gstinfo_response_dict["faq_link"]
    '''




def edpi_faq(entities):
    print("----------")
    print(entities)
    if len(entities) == 0:
        return edpifaq_response_dict["edpi_intro"]
    if len(entities) == 1:
        print(" ************** ")
        #print(entities[0].entity)
        ent = entities[0]
        return edpifaq_response_dict[ent["entity"]]
        '''for ent in entities:
            qtype = ent["type"]
            qval = ent["entity"]
            print(qtype)
            print(qval)
        if qtype == "tower":
            return edpifaq_response_dict[qval]'''
    return "Sorry.." + edpifaq_response_dict["faq_link"]

def entitlements_info(entities):
    print("----------")
    print(entities)
    if len(entities) == 0:
        return entitlements_info_response_dict["entitlements_intro"]
    for ent in entities:
        qtype = ent["type"]
        qval = ent["entity"]
        print(qtype)
        print(qval)
        if qtype == "edpi_ui":
            return entitlements_info_response_dict[qval]
    return "Sorry.." + edpifaq_response_dict["faq_link"]
