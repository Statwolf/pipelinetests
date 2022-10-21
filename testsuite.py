def params():
    ts = {}

    ts['fake'] = []

    ts['fake'].append({
        'name': 'My fake test',
        'params': {
            'yolo': 'My yolo param',
            'nolo': 42069
        }
    })

    def fakeCheck(data):
        raise Exception('A fake Exception')

    ts['fake'].append({
        'name': 'With check',
        'params': {
            'auff': True
        },
        'check': fakeCheck
    })

    ts['fake'].append({
        'params': {
            'auff': True
        }
    })

    return ts
