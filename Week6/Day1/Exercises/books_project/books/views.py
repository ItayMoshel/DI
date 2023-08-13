from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import Book
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render


def list_books(request):
    books = Book.objects.all()

    book_data = []
    for book in books:
        book_data.append({
            'title': book.title,
            'author': book.author,
            'published_date': book.published_date.strftime('%Y-%m-%d'),
            'description': book.description,
            'page_count': book.page_count,
            'categories': book.categories,
            'thumbnail_url': book.thumbnail_url,
        })

    return JsonResponse(book_data, safe=False)


def book_detail(request, id):
    book = get_object_or_404(Book, id=id)

    book_data = {
        'title': book.title,
        'author': book.author,
        'published_date': book.published_date.strftime('%Y-%m-%d'),
        'description': book.description,
        'page_count': book.page_count,
        'categories': book.categories,
        'thumbnail_url': book.thumbnail_url,
    }

    return JsonResponse(book_data)


@csrf_exempt
def create_book(request):
    if request.method == 'POST':
        data = request.POST
        title = data.get('title')
        author = data.get('author')
        published_date = data.get('published_date')
        description = data.get('description')
        page_count = data.get('page_count')
        categories = data.get('categories')
        thumbnail_url = data.get('thumbnail_url')

        if not title or not author or not published_date or not description or not page_count or not categories:
            return JsonResponse({'error': 'Missing required fields'}, status=400)

        try:
            page_count = int(page_count)
            if page_count <= 0:
                return JsonResponse({'error': 'Invalid page_count value'}, status=400)
        except ValueError:
            return JsonResponse({'error': 'Invalid page_count format'}, status=400)

        new_book = Book.objects.create(
            title=title,
            author=author,
            published_date=published_date,
            description=description,
            page_count=page_count,
            categories=categories,
            thumbnail_url=thumbnail_url,
        )

        book_data = {
            'id': new_book.id,
            'title': new_book.title,
            'author': new_book.author,
            'published_date': new_book.published_date.strftime('%Y-%m-%d'),
            'description': new_book.description,
            'page_count': new_book.page_count,
            'categories': new_book.categories,
            'thumbnail_url': new_book.thumbnail_url,
        }
        return JsonResponse(book_data, status=201)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)
