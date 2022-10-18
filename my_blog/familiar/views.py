from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from familiar.models import Familiar

from familiar.models import Familiar


def create_familiar(request, name: str, last_name: str, kin: str,email: str, birth_day: str):

    template = loader.get_template("template_familiar.html")

    familiar = Familiar(
        name=name, last_name=last_name, kin=kin, email=email, birth_day=birth_day
    )
    familiar.save()  # save into the DB

    context_dict = {"familiar": familiar}
    render = template.render(context_dict)
    return HttpResponse(render)


def familiars(request):
    familiars = Familiar.objects.all()

    context_dict = {"familiars": familiars}

    return render(
        request=request,
        context=context_dict,
        template_name="familiar/familiar_list.html",
    )
    