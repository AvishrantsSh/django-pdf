from django.http import HttpResponse
from django.views import View

from django_pdfview.decorators import test_decorator


@test_decorator
def Home(request):
    return HttpResponse("Hello, world. You're at the home page.")


class PDFView(View):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    @classmethod
    def as_view(cls, **initkwargs):
        view = super().as_view(**initkwargs)
        return view

    def render_template(self):
        pass
