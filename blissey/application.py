# -*- coding: utf-8 -*-

import collections
import datetime
import logging
import re
import sys

import dateutil.parser
import jira
import twilio.twiml

import blissey

if sys.version_info == (2, 7):
    import httplib as HttpStatusCode
    import urlparse as urllib_parse
    str = unicode
elif sys.version_info >= (3, 0):
    import http.client as HttpStatusCode
    import urllib.parse as urllib_parse


class BlisseyService(object):

    def __init__(self, people_repository=None, notes_repository=None):
        self.logger = logging.getLogger(name='blissey')
        self.logger.debug(msg='ServiceInitialize is pending.')
        self.logger.debug(msg='ServiceInitialize is starting.')

        if people_repository is None:
            people_repository = jira.JIRA
        if notes_repository is None:
            notes_repository = jira.JIRA

        credentials = (blissey.configuration['jira']['username'],
                       blissey.configuration['jira']['password'])
        self._people_repository = people_repository(
            server=blissey.configuration['jira']['hostname'],
            basic_auth=credentials)
        self._notes_repository = notes_repository(
            server=blissey.configuration['jira']['hostname'],
            basic_auth=credentials)

        self.logger.debug(msg='ServiceInitialize is complete.')

    def add_note(self, message):

        """
        Add a note for the specified person.

        Parameters
        ----------
        message : string
            Message specifying the person context and note. It must be
            formatted according to the following pattern:

            "set {first_name} {last_name} {note}"
        """

        self.logger.info(msg='NoteAdd is pending.')
        self.logger.debug(msg='NoteAdd is accepting <{}>.'.format(locals()))

        parsed_message = self._parse_message(message)
        person = self._get_person(first_name=parsed_message.first_name,
                                  last_name=parsed_message.last_name)
        todays_note = self._get_todays_note(person=person)

        self.logger.info(msg='NoteAdd is starting.')

        if todays_note:
            body = '\r\n\r\n'.join([todays_note.body, parsed_message.note])
            self.logger.debug(msg='NoteAdd is updating the most recent '
                                  'note from today <{}>.'.format(body))
            todays_note.update(body=body)
        else:
            self.logger.debug(msg='NoteAdd is adding a new note for '
                                  'today.'.format(parsed_message.note))
            self._notes_repository.add_comment(issue=person,
                                               body=parsed_message.note)

        self.logger.info(msg='NoteAdd is complete.')

    @staticmethod
    def _parse_message(message):

        """
        Parse the message to extract the person context and note.

        Returns
        -------
        namedtuple
            Parsed message. Three-element named tuple of strings. The
            first element is the person's first name. The second
            element is the person's last name. The third element is the
            note related to that person.

        Raises
        ------
        ValueError
            If the message was not formatted correctly.
        """

        ParsedMessage = collections.namedtuple(
            typename='ParsedMessage',
            field_names=['first_name', 'last_name', 'note'])
        pattern = '^set (?P<first_name>\w+) (?P<last_name>\w+) (?P<note>.+)$'

        match = re.match(pattern=pattern, string=message)

        if match:
            parsed_message = ParsedMessage(**match.groupdict())
            return parsed_message
        else:
            raise ValueError('The message was not formatted correctly.')

    def _get_person(self, first_name, last_name):

        """
        Returns
        -------
        jira.Resources.Issue
            The person matching the search.
        None
            If there were no results.

        Raises
        ------
        LookupError
            If there were multiple results.
        """

        jql = 'summary ~ "{first_name}" AND summary ~ "{last_name}"'.format(
            first_name=first_name, last_name=last_name)
        self.logger.debug(msg='JQL query is executing <{}>.'.format(jql))
        results = self._people_repository.search_issues(jql_str=jql)

        if not results:
            person = None
        elif len(results) > 1:
            raise LookupError('The search returned multiple results.')
        else:
            person = results[0]

        return person

    def _get_todays_note(self, person):

        """
        Parameters
        ----------
        person : jira.Resources.Issue

        Returns
        -------
        jira.Resources.Comment
            The most recent note from today.
        None
            If there wasn't a note from today.
        """

        todays_note = None

        comments = {dateutil.parser.parse(timestr=comment.created): comment
                    for comment
                    in self._notes_repository.comments(issue=person)}

        if comments:
            most_recent_created_at = sorted(comments, reverse=True)[0]
            if most_recent_created_at.date() == datetime.date.today():
                todays_note = comments[most_recent_created_at]

        return todays_note


def handler(event, context):

    blissey_service = BlisseyService()

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
