import pytest
from mylibrary import create_app
from mylibrary.models import Book, Author, Translator, Serie, Publisher, Genre, Editor, Composition


@pytest.fixture
def app():

    app = create_app()
    app.testing = True

    yield app


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def runner(app):
    return app.test_cli_runner()

@pytest.mark.parametrize(('book,status_code'), (
    ({'bname':'',
      'bisbn':'',
      'byear':'',
      'bvol':'',
      'beditor':'',
      'pname':'',
      'purl':'',
      'pcity':'',
      'cmp[0].aname':'',
      'cmp[0].ctranslator':'',
      'cmp[0].genre':'',
      'cmp[0].cname':''}, 200),
    ({'bname':'', 'bisbn':'', 'byear':'', 'bvol':'', 'beditor':'', 'pname':'', 'purl':'', 'pcity':'',
      'cmp[0].aname':'', 'cmp[0].ctranslator':'', 'cmp[0].genre':'', 'cmp[0].cname':''}, 200),
    ({'bname':'', 'bisbn':'', 'byear':'', 'bvol':'', 'beditor':'', 'pname':'', 'purl':'', 'pcity':'',
      'cmp[0].aname':'', 'cmp[0].ctranslator':'', 'cmp[0].genre':'', 'cmp[0].cname':''}, 200),
))

def test_book_add(client, book, status_code):
    response = client.post(
        '/add_book',
        data={'bname':book['bname'],
              'bisbn':book['bisbn'],
              'byear':book['byear'],
              'bvol':book['bvol'],
              'beditor':book['beditor'],
              'pname':book['pname'],
              'purl':book['purl'],
              'pcity':book['pcity'],
              'cmp[0].aname':book['cmp[0].aname'],
              'cmp[0].ctranslator':book['cmp[0].ctranslator'],
              'cmp[0].genre':book['cmp[0].genre'],
              'cmp[0].cname':book['cmp[0].cname']
        }
    )
    assert response.status_code == status_code