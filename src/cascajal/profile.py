import os
import pkgutil
import shutil
import tempfile


def find_firefox():
    """Attempt to find a Firefox-like executable and return the path."""

    candidates = [
        '/usr/bin/firefox',
        '/usr/bin/iceweasel',
    ]

    for c in candidates:
        if os.path.exists(c):
            return c


class Profile(object):

    TEMPLATE_FILES = [
        'prefs.js',
        'extensions.ini',
    ]

    def __init__(self, opts):

        self.options = opts

    def __enter__(self):

        # create the temporary profile directory
        self.location = tempfile.mkdtemp()

        os.mkdir(
            os.path.join(self.location, 'extensions')
        )

        file(
            os.path.join(
                self.location,
                'extensions',
                'jid1-bwQXQ9ZfPZiqdw@jetpack.xpi',
            ),
            'wb',
        ).write(
            pkgutil.get_data('cascajal', 'data/prontoprint/prontoprint.xpi'),
        )

        context = self.options.copy()
        context['profile_dir'] = self.location

        # copy templated files into it
        for filename in self.TEMPLATE_FILES:
            file(os.path.join(self.location, filename), 'w').write(
                pkgutil.get_data('cascajal', 'data/%s' % (filename,)) % context
            )

        return self

    def __exit__(self, *exc_info):

        shutil.rmtree(self.location)

        return None
