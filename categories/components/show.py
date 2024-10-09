from django_unicorn.components import UnicornView
from categories.models import Category
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

class ShowView(UnicornView):
    query = ""
    categories = []
    page = 1
    total_pages = 10
    previous_page = None
    next_page = None

    def mount(self):
        self.load_categories()

    def load_categories(self):
        categories = Category.objects.all()

        if self.query:
            categories = categories.filter(name__icontains=self.query)

        paginator = Paginator(categories, 10)

        try:
            paginated_categories = paginator.page(self.page)
        except PageNotAnInteger:
            paginated_categories = paginator.page(1)
        except EmptyPage:
            paginated_categories = paginator.page(paginator.num_pages)

        self.categories = list(paginated_categories.object_list)
        self.total_pages = paginator.num_pages

        self.previous_page = self.page - 1 if self.page > 1 else None
        self.next_page = self.page + 1 if self.page < self.total_pages else None

    def search(self):
        self.page = 1
        self.load_categories()

    def go_to_page(self, page):
        self.page = page
        self.load_categories()
