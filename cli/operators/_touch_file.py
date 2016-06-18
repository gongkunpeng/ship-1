def _touch_file(file_path, template):
    with open(file_path, 'w+') as f:
        f.write(template)
