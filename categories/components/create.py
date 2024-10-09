from django_unicorn.components import UnicornView
from categories.models import Category

class CreateView(UnicornView):
    name = ""

    def create_category(self):
        if self.name.strip():
            Category.objects.create(name=self.name)
            self.name = ""
            self.emit("categoryCreated")
            self.call("closeModal")