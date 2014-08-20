def has_access_to_note(request, note_set, private_key=None):
    """ Check whether a user has access to a note based on the request """
    if note_set.private and not user_owns_note(note_set, request.user):
        if private_key != note_set.private_key:
            return False
    return True

def user_owns_note(note_set, user):
    return user.id and note_set.owner and (user.pk == note_set.owner.pk)