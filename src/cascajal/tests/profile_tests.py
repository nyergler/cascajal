import os
from unittest import TestCase

import cascajal.profile


class ProfileManagerTests(TestCase):

    STUB_OPTS = {
        'output_filename': '',
    }

    def test_creates_dir_with_prefs(self):

        with cascajal.profile.Profile(self.STUB_OPTS) as profile:

            self.assertTrue(
                os.path.isdir(profile.location),
            )
            self.assertTrue(
                os.path.exists(
                    os.path.join(profile.location, 'prefs.js'),
                ),
            )

    def test_cleans_up_on_exit(self):

        location = None

        with cascajal.profile.Profile(self.STUB_OPTS) as profile:

            location = profile.location
            self.assertTrue(
                os.path.isdir(location),
            )

        self.assertFalse(
            os.path.exists(location)
        )

    def test_expands_prefs(self):

        with cascajal.profile.Profile({
            'output_filename': 'test_expands_prefs.pdf',
        }) as profile:

            self.assertTrue(
                os.path.isdir(profile.location),
            )
            self.assertIn(
                'test_expands_prefs.pdf',
                file(
                    os.path.join(profile.location, 'prefs.js'),
                ).read(),
            )
