from django_unicorn.components import UnicornView
from users.models import ProfileUser
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q

class UsersshowView(UnicornView):
    query = ''
    profile_users = []
    page = 1
    total_pages = 10
    previous_page = None
    next_page = None

    def mount(self):
        self.load_profile_users()

    def load_profile_users(self):
        profile_users = ProfileUser.objects.exclude(user_id=1).order_by('id')

        if self.query:
            profile_users = profile_users.filter(
                Q(first_name__icontains=self.query) | Q(last_name__icontains=self.query)
            )

        paginator = Paginator(profile_users, 10)

        try:
            paginated_profile_users = paginator.page(self.page)
        except PageNotAnInteger:
            paginated_profile_users = paginator.page(1)
        except EmptyPage:
            paginated_profile_users = paginator.page(paginator.num_pages)

        self.profile_users = list(paginated_profile_users.object_list)
        self.total_pages = paginator.num_pages

        self.previous_page = self.page - 1 if self.page > 1 else None
        self.next_page = self.page + 1 if self.page < self.total_pages else None

    def search(self):
        self.page = 1
        self.load_profile_users()

    def go_to_page(self, page):
        self.page = page
        self.load_profile_users()

    def clear(self):
        self.query = ''
        self.profile_users = ProfileUser.objects.all()
