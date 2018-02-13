
import random
from html_template import *
from HTMLGenerator import *

hg = HTMLGenerator()

##dict of response for each type of intent











intent_response_dict = {
    "intro": ["This is a EDPI FAQ bot. One stop-shop to all your EDPI related queries"],
    "greet":["Hey, how can i help you?","Hello,How can i help you?","Hi,How can i help you?"],
    "goodbye":["Bye","It was nice talking to you","See you","ttyl"],
    "affirm":["Cool","I know you would like it"],
    "edpi_intro": "<html><body>EDPI is an Enterprise Data Platform Interface. Once onboarded consumers can access AM/WM Data from predefined Data towers. Choose one from below <br/><input type=\"button\" name=\"submit\" class=\"btn btn-info btn-lg active\" value=\"AM EDPI\" onclick=\"javascript:window.open('http://edpiamui')\">&nbsp;<input type=\"button\" name=\"submit\" class=\"btn btn-info btn-lg active\" value=\"WM EDPI\" onclick=\"javascript:window.open('http://edpiwmui')\"> </form></body></html>",
    "edpi_faq": "EDPI is an Enterprise Data Platform Interface. Once onboarded consumers can access AM/WM Data from predefined Data towers.",
    "edpi_offer": "EDPI Offers below feautures. <br>Metadata Driven Interface.<br>Single point of Control<br>High Performance<br>Business Definition Link<br>Robus and Scalable<br>Cross Domain queries",
    "onboard_edpi": "You need to have Janus entitlements to onboard application and create queries. More details <a target='_blank' href='http://edpihelppage'>here</a>",
    "edpi_consume": "EDPI allows you to construct GraphQL from its UI and expose the same as a rest Endpoint which streams out the data ",
    "create_query": "Click on the me@edpi on the top menu. Click on Build queries, and write GraphQL",
    "edpi_gql": "Stored queries are defined in a format based on <a target='_blank' href='https://reactjs.org/blog/2015/05/01/graphql-introduction.html'>GraphQL.</a>. Stored queries are team specific and owned/managed by them ",
    "benefits": "EDPI is a data distribution layer for AWM which acts as golden source",
    "faq_link": "You can check all the answers here AM EDPI: <a target='_blank' href=\"go/edpi\"</a>, WM EDPI:\"<a target='_blank' href=\"go/edpiwm\"</a>",
    "data_entitlement": "Which LOB?Options:AM#WM",
    "AM_data_entitlement": "You need to have an EDPI parent Query Entitlement and also we have data sourced from below towers. Which tower are you interested in?Options:Reference#Securities & Pricing#Funds",
    "WM_data_entitlement": "You need to have an EDPI parent Query Entitlement and also we have data sourced from below towers. Which tower are you interested in?Options:Reference#Transaction & Holdings#Morningstar",
    "Reference_AM_data_entitlement": "Please find the Link:www.entitlement.com/am/Reference",
    "Securities & Pricing_AM_data_entitlement": "Please find the Link:www.entitlement.com/am/s&p",
    "Funds_AM_data_entitlement": "Please find the Link:www.entitlement.com/am/funds",
    "Reference_WM_data_entitlement": "Please find the Link:www.entitlement.com/wm/Reference",
    "Transaction & Holdings_WM_data_entitlement": "Please find the Link:www.entitlement.com/WM/t&h",
    "MorningStar_WM_data_entitlement": "Please find the Link:www.entitlement.com/wm/morningstar",
    "Entitlement_info":"EDPI uses janus entitlements to authorize user, Which one you look for?Options:Self Service#Data",
    "Self Service_Entitlement_info":"For Individual Users accessing Self Service or EDPI UI, please raise EDPI Consumer entitlement",
    "Data_Entitlement_info":"Raise the Janus data entitlement specific to data tower, Reference/Instrument/Funds etc.",
    "UI_entitlement": "Which LOB?Options:AM#WM",
    "AM_UI_entitlement":"Please raise EDPI COnsumer entitlement for AM in RMT Prod. Visit RMT",
    "WM_UI_entitlement":"Please raise EDPI COnsumer entitlement for WM in RMT Prod. Visit RMT"
    
}

edpifaq_response_dict = {    
    #"edpi_intro": "EDPI is an Enterprise Data Platform Interface. Once onboarded consumers can access AM/WM Data from predefined Data towers. Choose from below two options <br/><br/><html><body><form action=\"http://localhost:5000\" method=\"POST\"><div class=\"btn btn-info btn-lg\">AM EDPI</div>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<div class=\"btn btn-info btn-lg\">WM EDPI</div></form></body></html>",
    #"edpi_intro": "EDPI is an Enterprise Data Platform Interface. Once onboarded consumers can access AM/WM Data from predefined Data towers. Choose one from below <br/><br/><html><body><form action=\"http://127.0.0.1:8080/result\" method=\"POST\"><input type=\"submit\" name=\"submit\" class=\"btn btn-info btn-lg active\" value=\"AM EDPI\">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<input type=\"submit\" name=\"submit\" class=\"btn btn-info btn-lg active\" value=\"WM EDPI\"> </form></body></html>",
    "edpi": "EDPI is an Enterprise Data Platform Interface. Once onboarded consumers can access AM/WM Data from predefined Data towers.",
    "benefits":"EDPI is a data distribution layer for AWM which acts as golden source",
    "faq_link":'You can check all the answers here AM EDPI: <a href=\"go/edpi\"</a>, WM EDPI:\"<a href=\"go/edpiwm\"</a>',
    #"reference":"You want EDPI reference data ... visit Data model browser",
    "reference": "Which LOB?Options:AM#WM",
    "AM_reference": "Which Version do you want to see?Options:v0#v1#v2",
    "WM_reference": "Which Version do you want to see?Options:v3#v4#v5",
    "v0_AM_reference": "Please find the Link:www.google.com",
}

entitlements_info_response_dict = {
    "entitlements_intro": "EDPI Needs two types of entitlements. One is for accessing the EDPI UI to onboard and build queries. Another type is to access the data using the built stored queries",
    "me@edpi": "One Needs EDPI Consumer entitlements to onboard and build queries."
}



edpi_query_value_dict = {
    "faq_link":'You can check all the answers here AM EDPI: <a href=\"go/edpi\", WM EDPI:\"<a href=\"go/edpiwm\"</a>'
}

def general_response(intent):
    print(" ########## ",intent," ################")
    return intent_response_dict[intent]

def button_generator(buttons,append_text):
    button_template = []
    for b in buttons:
        entry = Entry(ResponseType.BUTTON,b+"_"+append_text,b)
        button_template.append(entry)
    return button_template


def link_generator(links):
    link_template=[]
    for l in links:
        entry = Entry(ResponseType.LINK,l,l)
        link_template.append(entry)
    return link_template



def define_html_template(response_text,append_text):
    entry = []
    
    if response_text.find("Options")!= -1:
        a=response_text.find("Options")
        text=response_text[0:a]
        button_text=response_text[a+8:len(response_text)]
        buttons=button_text.split("#")
        entry = button_generator(buttons,append_text)
                    
    elif response_text.find("Link")!= -1:
        a=response_text.find("Link")
        text=response_text[0:a+5]
        link_text=response_text[a+5:len(response_text)]
        links=link_text.split("#")
        entry= link_generator(links)
    else:
        text = response_text
        
    

    h_t=Response()
    print (str(h_t))
    h_t.summaryText = text
    h_t.submitAction = "javascript:sendToServer(value)"
    h_t.entries = entry
    return h_t



get_random_response = lambda intent:random.choice(intent_response_dict[intent])

def getBotResponse(intent,entities):

    if intent == "entitlements_info":
        print('OK inside entitlements_info')
        response_text = entitlements_info(entities)
    elif intent == "intro":
        response_text = get_random_response(intent)
    elif intent == "greet":
        response_text = get_random_response(intent)
        print(response_text)
    elif intent == "goodbye":
        response_text = get_random_response(intent)
    elif intent == "affirm":
        response_text = get_random_response(intent)
    elif intent in intent_response_dict:
        print ("is it working??")
        response_text=intent_response_dict[intent]
        h_t=define_html_template(response_text,intent)
        response_text= hg.generateHTML(h_t)
    elif intent == "edpi_faq":
        #response_text = gst_info(entities)# "Sorry will get answer soon" #get_event(entities["day"],entities["time"],entities["place"])
        print (intent)
        response_text = edpi_faq(entities)
        append_text=''
        if len(entities)>0:
            ent=entities[0]
            append_text=ent["entity"]
        h_t=define_html_template(response_text,append_text)
        response_text= hg.generateHTML(h_t)

    else:
        response_text = "Sorry I am not trained to do that yet..." 

    return response_text


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
