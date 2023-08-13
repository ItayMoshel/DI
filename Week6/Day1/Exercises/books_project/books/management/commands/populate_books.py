import requests
from django.core.management.base import BaseCommand
from datetime import datetime
from books.models import Book


class Command(BaseCommand):
    help = 'Populate the Book model with sample data using Google Books API'

    def handle(self, *args, **options):
        search_terms = 'manga'

        url = f'https://www.googleapis.com/books/v1/volumes?q={search_terms}'
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            books = data.get('items', [])

            for book in books:
                volume_info = book.get('volumeInfo', {})
                title = volume_info.get('title', 'Unknown Title')
                authors = ', '.join(volume_info.get('authors', ['Unknown Author']))
                published_date_str = volume_info.get('publishedDate', 'Unknown Date')

                try:
                    published_date = datetime.strptime(published_date_str, '%Y-%m-%d').date()
                except (ValueError, TypeError):
                    published_date = None

                description = volume_info.get('description', 'No description available')
                page_count = volume_info.get('pageCount', 0)
                categories = ', '.join(volume_info.get('categories', ['Uncategorized']))
                thumbnail_url = volume_info.get('imageLinks', {}).get('thumbnail', '')

                # Create a new Book object
                if published_date is not None:
                    # Create a new Book object
                    Book.objects.create(
                        title=title,
                        author=authors,
                        published_date=published_date,
                        description=description,
                        page_count=page_count,
                        categories=categories,
                        thumbnail_url=thumbnail_url,
                    )

            self.stdout.write(self.style.SUCCESS('Sample data populated successfully!'))
        else:
            self.stdout.write(self.style.ERROR('Failed to fetch data from Google Books API'))
