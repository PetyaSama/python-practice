def recursive_dict_search(dictionary, target_value, path=None, found=False):
    if path is None:
        path = []
    for key, value in dictionary.items():
        if value == target_value:
            found = True
            path.append(key)
            print(f"Found {target_value} at path: {' -> '.join(path)}")
        elif isinstance(value, dict):
            path.append(key)
            found = recursive_dict_search(value, target_value, path, found)
        path.pop()  # Remove the key from the path when backtracking
    return found


site = {
    'html': {
        'head': {
            'title': 'Мой сайт'
        },
        'body': {
            'h2': 'Здесь будет мой заголовок',
            'div': 'Тут, наверное, какой-то блок',
            'p': 'А вот здесь новый абзац'
        }
    }
}

print(recursive_dict_search(site, "div"))