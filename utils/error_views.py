from django.http import JsonResponse

def handler404(request,exception):
    message = ('path nor found')
    response = JsonResponse(data={'error' : message})
    response.status_code = 404
    return response