# -*- coding: utf-8 -*-

import collections
import uuid

from nose.tools import assert_equal, assert_in, assert_is_none, raises

from blissey import services


class MockPeopleRepository(object):

    def __init__(self, *args, **kwargs):
        pass

    def search_issues(self, *args, **kwargs):
        return ['foo', 'bar']


class MockNotesRepository(object):

    def __init__(self, *args, **kwargs):
        pass

    def comments(self, *args, **kwargs):
        Comment = collections.namedtuple(typename='Comment',
                                         field_names=['created'])
        comments = [Comment(created='2000-01-01')]
        return comments


class TestBlisseyService(object):

    def __init__(self):
        self.service = None

    def setup(self):
        self.service = services.BlisseyService()

    def test_parse_message(self):
        message = 'set Bruiser Nguyen foo'
        parsed_message = self.service._parse_message(message)
        assert_equal(len(parsed_message), 3)
        assert_equal(parsed_message.first_name, 'Bruiser')
        assert_equal(parsed_message.last_name, 'Nguyen')
        assert_equal(parsed_message.note, 'foo')

    @raises(ValueError)
    def test_parse_message_has_invalid_format(self):
        message = 'Bruiser Nguyen foo'
        self.service._parse_message(message)

    def test_get_person(self):
        first_name = 'Bruiser'
        last_name = 'Nguyen'
        person = self.service._get_person(first_name=first_name,
                                          last_name=last_name)
        assert_in(first_name, person.fields.summary)
        assert_in(last_name, person.fields.summary)

    def test_get_person_no_results(self):
        person = self.service._get_person(first_name=str(uuid.uuid4()),
                                          last_name=str(uuid.uuid4()))
        assert_is_none(person)

    @raises(LookupError)
    def test_get_person_multiple_results(self):
        people_repository = MockPeopleRepository
        service = services.BlisseyService(people_repository=people_repository)
        service._get_person(first_name='', last_name='')

    def test_get_todays_note(self):
        person = self.service._get_person(first_name='Bruiser',
                                          last_name='Nguyen')
        note = self.service._notes_repository.add_comment(issue=person,
                                                          body='foo')
        todays_note = self.service._get_todays_note(person=person)
        assert_equal(todays_note.body, note.body)

        note.delete()

    def test_get_todays_note_no_results(self):
        notes_repository = MockNotesRepository
        service = services.BlisseyService(notes_repository=notes_repository)
        todays_note = service._get_todays_note(person=None)
        assert_is_none(todays_note)
