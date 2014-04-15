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

    def __init__(self, opts):

        self.options = opts

    def __enter__(self):

        # create the temporary profile directory
        self.location = tempfile.mkdtemp()

        # copy prefs.js into it
        file(os.path.join(self.location, 'prefs.js'), 'w').write(
            pkgutil.get_data('cascajal', 'data/prefs.js') % self.options
        )

        return self

    def __exit__(self, *exc_info):

        shutil.rmtree(self.location)

        return None
