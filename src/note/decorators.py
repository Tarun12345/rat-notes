from note.util import has_access_to_note
from models import Set, Note, Commit
from django.shortcuts import get_object_or_404, redirect

def private(model, function=None):

    def decorator(view_func):
        def _wrapped_view(request, pk, *args, **kwargs):
            object = get_object_or_404(model, pk=pk)
            note_set = None

            if model == Set:
                note_set = object
            elif model == Commit:
                note_set = object.parent_set
            elif model == Note:
                note_set = object.revision.parent_set

            if has_access_to_note(request, note_set, kwargs.get('private_key')):
                return view_func(request, pk, object, *args, **kwargs)
            return redirect('note')

        return _wrapped_view

    if function:
        return decorator(function)
    return decorator
