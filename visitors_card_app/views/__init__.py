from .create_read_views import *
from .update_delete_views import *
from .analysis_views import *


def analysis_index(request):
    return render(request, 'visitors_card_app/analysis/analysis_index.html')