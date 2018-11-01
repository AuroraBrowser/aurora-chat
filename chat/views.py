from auroravr import gamelift
from django.http import JsonResponse
from django.shortcuts import redirect
from django.urls import reverse
from django.views import generic


class IndexView(generic.TemplateView):
    template_name = 'chat/index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['game_sessions'] = gamelift.search(alias_id='alias-784566b2-47e5-43e6-b19a-3271e09efd1f')
        return context


def create_view(request):
    gamelift.create(alias_id='alias-784566b2-47e5-43e6-b19a-3271e09efd1f',
                html=request.build_absolute_uri(reverse('chat:room')), max_player=4)
    return redirect(request.build_absolute_uri(reverse('chat:index')))


def redirect_view(request):
    return redirect(request.build_absolute_uri(reverse('chat:room')))


class RoomView(generic.TemplateView):
    template_name = 'chat/room.html'


def enter_view(request):
    return JsonResponse(gamelift.enter(room_id=request.GET.get('room_arn'), player_id='new'))
