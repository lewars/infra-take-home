import pytest
from reverse import main


def test_reverse_call(client):
    rv = client.post('/reverse', data='foo')
    rev_str = rv.json['payload']
    assert 'oof' == rev_str

