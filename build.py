import os
import json

baseDir = os.path.join(os.path.dirname(__file__), 'docs/')
result = dict()
for dirpath, dirs, files in os.walk(baseDir):
    for filename in files:
        basename, ext = os.path.splitext(filename);
        if ext != '.md':
            continue

        filepath = os.path.join(dirpath, filename)
        pagepath = '/' + os.path.relpath(os.path.join(dirpath, basename), start='docs')

        if pagepath.lower() == '/readme':
            # We don't include the readme so that we can
            # document the documentation system without it
            # being included on the site.
            continue

        if os.path.islink(filepath):
            if pagepath == '/Index':
                # Special case; /Index just means /
                pagepath = '/'

            linkpath = os.path.join(os.path.dirname(pagepath), os.readlink(filepath))
            linkpath = os.path.normpath(linkpath)
            linkpath, _ = os.path.splitext(linkpath)
            result[pagepath] = {'link': linkpath}
        else:
            with open(filepath) as myfile:
                result[pagepath] = {'page': myfile.read()}

print(json.dumps(result))
