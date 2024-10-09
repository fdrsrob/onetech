from django_unicorn.components import UnicornView
from products.models import Product
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

class ProductsearchView(UnicornView):
    query = ""
    min_price = ""
    max_price = ""
    products = []
    page = 1
    total_pages = 10
    previous_page = None
    next_page = None

    def mount(self):
        self.load_products()

    def load_products(self):
        products = Product.objects.all()

        if self.query:
            products = products.filter(name__icontains=self.query)

        if self.min_price:
            products = products.filter(price__gte=float(self.min_price))

        if self.max_price:
            products = products.filter(price__lte=float(self.max_price))

        # Paginamos los productos
        paginator = Paginator(products, 10)

        try:
            paginated_products = paginator.page(self.page)
        except PageNotAnInteger:
            paginated_products = paginator.page(1)
        except EmptyPage:
            paginated_products = paginator.page(paginator.num_pages)

            # Convertimos el objeto `Page` en una lista
        self.products = list(paginated_products.object_list)
        self.total_pages = paginator.num_pages

        self.previous_page = self.page - 1 if self.page > 1 else None
        self.next_page = self.page + 1 if self.page < self.total_pages else None

    def search(self):
        self.page = 1
        self.load_products()

    def go_to_page(self, page):
        self.page = page
        self.load_products()

    def clear(self):
        self.query = ""
        self.min_price = ""
        self.max_price = ""
        self.products = Product.objects.all()