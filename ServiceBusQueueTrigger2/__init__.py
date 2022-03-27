import logging
import json
from xml.dom.minidom import Document
import azure.functions as func


def main(msg: func.ServiceBusMessage, outputDoc: func.Out[func.Document]):
    sb2_msg = msg.get_body().decode("utf-8") # msg string from service bus

    logging.info('Python ServiceBus queue trigger processed message: %s',
                 sb2_msg)

    doc_item = func.Document.from_json(sb2_msg) # pass msg string and return document object

    outputDoc.set(doc_item) # store document as items in CosmosDB container using CosmosDB output binding

    # outdata = {}
    # outdata['content'] = msgBody
    # outputDoc.set(func.Document.from_dict(outdata))
    
   
 