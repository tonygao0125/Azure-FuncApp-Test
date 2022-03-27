import logging

import azure.functions as func


def main(msg: func.ServiceBusMessage,outputSbMsg: func.Out[str]) -> str:
    sb1_msg = msg.get_body().decode("utf-8")

    logging.info('Python ServiceBus queue trigger processed message: %s', sb1_msg)

    outputSbMsg.set(sb1_msg)
 