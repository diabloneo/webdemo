
import wsmeext.pecan as wsme_pecan


def expose(*args, **kwargs):
    """Ensure that only JSON, and not XML, is supported."""
    if 'rest_content_types' not in kwargs:
        kwargs['rest_content_types'] = ('json',)

    return wsme_pecan.wsexpose(*args, **kwargs)
