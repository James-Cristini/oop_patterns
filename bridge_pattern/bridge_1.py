### Bridge: Decouple an abstraction from its implementation so that the two can vary independently
# Favor composition over inheritance
# Instead of a LongFormArtist, LongFormBook, ThumbnailArtist, ThumbnailBook, etc. via inheritance,
# Have LongForm, Thumbnail separate classes which accept Artist, Book, etc. as resources
# Some similarities here to strategy and adapter patterns


class IResource(object):
    """ Resource Interface. """

    def snippet(self):
        raise NotImplementedError

    def image(self):
        raise NotImplementedError

    def title(self):
        raise NotImplementedError


class Artist(IResource):
    @property
    def snippet(self):
        return 'Artist snippet'

    @property
    def image(self):
        return 'Artist image'

    @property
    def title(self):
        return 'Artist title'

    def __str__(self):
        return 'ARTIST'


class Book(IResource):
    @property
    def snippet(self):
        return 'Book snippet'

    @property
    def image(self):
        return 'Book image'

    @property
    def title(self):
        return 'Book title'

    def __str__(self):
        return 'BOOK'


class View(object):
    """ View Interface. """
    def __init__(self, resource):
        self.resource = resource

    def show(self):
        raise NotImplementedError


class LongFormView(View):
    def show(self):
        print('LongFormView show method for resource: {0}'.format(self.resource))
        print('Showing: {0}'.format(self.resource.title))
        print('Showing: {0}'.format(self.resource.image))
        print('Showing: {0}'.format(self.resource.snippet))


class Thumbnail(View):
    def show(self):
        print("Thumbnail show method for resource: {0}".format(self.resource))
        print('Showing: {0}'.format(self.resource.title))
        print('Showing: {0}'.format(self.resource.image))
        print('Showing: {0}'.format(self.resource.snippet))


def main():
    artist_resource = Artist()
    book_resource = Book()

    long_view_artist = LongFormView(artist_resource)
    long_view_book = LongFormView(book_resource)

    thumbnail_view_artist = Thumbnail(artist_resource)
    thumbnail_view_book = Thumbnail(book_resource)

    long_view_artist.show()
    long_view_book.show()
    thumbnail_view_artist.show()
    thumbnail_view_book.show()

if __name__ == '__main__':
    main()