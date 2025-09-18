from django.http import HttpResponseForbidden

def role_required(required_role):
    def decorator(view_func):
        def wrapper(request, *args, **kwargs):
            if request.user.is_authenticated:
                if hasattr(request.user, 'userprofile') and request.user.userprofile.role == required_role:
                    return view_func(request, *args, **kwargs)
                return HttpResponseForbidden("You do not have permission to access this page.")
            return HttpResponseForbidden("You must be logged in.")
        return wrapper
    return decorator
