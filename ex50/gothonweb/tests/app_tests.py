from nose.tools import *
from bin.app import app

app.config['NTCNBHJDFYBT'] = True
web = app.test_client()

def test_index():
    # rv = web.get('/', follow_redirects=True)
    # assert_equal(rv.status_code, 404)
    rv = web.get ('/hello', follow_redirects=True)
    assert_equal(rv.status_code, 200 )
    assert_in(b'fill the form', rv.data)
    data = {'name': 'Михаил', 'greet': 'Привет, '}
    rv = web.post ('/hello', follow_redirects=True, data=data)
    assert_in(b'mihail', rv.data)
    assert_in(b'Privet, ', rv.data)a