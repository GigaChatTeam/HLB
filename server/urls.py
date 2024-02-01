from django.http import HttpResponse
from django.urls import path, include

from .views import handlers


def passer(*_, **__):
    return HttpResponse(status=501)


urlpatterns = [
    path('channel/', include([
        path('invitation', handlers.Channels.Invitations.verify_uri),
        path('<int:channel>', include([
            path('', passer),
            path('/message/<int:message>', passer),
            path('/messages/', include([
                path('history', handlers.Channels.Messages.History.messages),
                path('edited', passer),
                path('deleted', passer)
            ]))
        ])),
    ])),
    path('user', include([
        path('', include([
            path('/channels', passer),
            path('/profile', passer)
        ])),
        path('/<int:account>', passer)
    ]))
]
