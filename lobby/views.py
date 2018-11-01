import os

from django.views import generic

from lobby.aws import gamelift


class IndexView(generic.TemplateView):
    template_name = 'lobby/index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['game_sessions'] = gamelift.search()
        return context
