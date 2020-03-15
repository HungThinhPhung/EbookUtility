def merge_url(patches: list, is_https=False):
    if not isinstance(patches, list) or len(patches) == 0:
        return ''

    prefix = 'https://' if is_https else 'http://'
    url = patches[0] if patches[0].startswith('http') else prefix + patches[0]
    if not patches[0].endswith('/'):
        url += '/'
    for patch in patches[1:]:
        url += patch if patch.endswith('/') else patch + '/'

    return url
