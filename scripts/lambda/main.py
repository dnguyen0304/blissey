# -*- coding: utf-8 -*-

import sys

import twilio.twiml

from blissey import services

if sys.version_info >= (2, 7):
    import httplib as HttpStatusCode
    import urlparse as urllib_parse
    str = unicode
elif sys.version_info >= (3, 0):
    import http.client as HttpStatusCode
    import urllib.parse as urllib_parse


def handler(event, context):

    blissey_service = services.BlisseyService()

    query = urllib_parse.parse_qs(event['body'])
    message = query['Body'][0]

    error_message = 'NoteAdd is encountering an error <{}>.'

    try:
        blissey_service.add_note(message=message)
        status_code = HttpStatusCode.CREATED
        message_ = 'The note was added successfully.'
    except LookupError as error:
        blissey_service.logger.debug(msg=error_message.format(str(error)))
        status_code = HttpStatusCode.UNPROCESSABLE_ENTITY
        message_ = str(error)
    except ValueError as error:
        blissey_service.logger.debug(msg=error_message.format(str(error)))
        status_code = HttpStatusCode.BAD_REQUEST
        message_ = str(error)

    reply = twilio.twiml.Response()
    reply.message(message_)

    response = {'statusCode': status_code,
                'headers': {'Content-Type': 'text/xml'},
                "body": str(reply)}

    return response
