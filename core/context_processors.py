from settings.models import Assignment, MyDetail

def get_my_details(request):
    my_detail = MyDetail.load()
    if my_detail:
        return {'my_detail': {'success': True, 'data': my_detail}}
    else:
        return {'my_detail': {'success': False, 'data': None}}

def get_assignments(request):
    assignment = Assignment.load()
    if assignment:
        return {'assignment': {'success': True, 'data': assignment}}
    else:
        return {'assignment': {'success': False, 'data': None}}