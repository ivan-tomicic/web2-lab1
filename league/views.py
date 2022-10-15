import json, logging

from django.http import HttpResponse
from django.shortcuts import render

logger = logging.getLogger('info')


def index(request):
    logger.info(request.session.get("user"))
    return render(
        request,
        "index.html",
        context={
            "session": request.session.get("user"),
            "pretty": json.dumps(request.session.get("user"), indent=4),
        },
    )




