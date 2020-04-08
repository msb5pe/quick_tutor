from django.test import TestCase
from django.contrib.auth.models import User
from .views import get_same_location
# Create your tests here.


class LocationTests(TestCase):

    def test_users_are_at_same_location(self):
        """
        Tests whether the users are all at the same location or not
        :return:
        """
        self.user1 = User.objects.create_user(username='testuser1', password='12345')
        self.user2 = User.objects.create_user(username='testuser2', password='12345')
        self.user3 = User.objects.create_user(username='testuser3', password='12345')

        self.profile1 = self.user1.userprofile
        self.profile1.location = 'Alderman'
        self.profile2 = self.user2.userprofile
        self.profile2.location = 'Alderman'
        self.profile3 = self.user3.userprofile
        self.profile3.location = 'Clemons'
        self.input_profiles = []
        self.input_profiles.extend([self.profile1, self.profile2, self.profile3])

        self.output_profiles = get_same_location('Alderman', self.input_profiles)

        self.correct_profiles = []
        self.correct_profiles.append(self.profile1)
        self.correct_profiles.append(self.profile2)

        self.assertEqual(self.output_profiles, self.correct_profiles)
        # self.assertIs(True, True)

    def test_users_are_not_at_same_location(self):
        """

        :return:
        """
        self.user1 = User.objects.create_user(username='testuser1', password='12345')
        self.user2 = User.objects.create_user(username='testuser2', password='12345')
        self.user3 = User.objects.create_user(username='testuser3', password='12345')

        self.profile1 = self.user1.userprofile
        self.profile1.location = 'Alderman'
        self.profile2 = self.user2.userprofile
        self.profile2.location = 'Alderman'
        self.profile3 = self.user3.userprofile
        self.profile3.location = 'Clemons'
        self.input_profiles = []
        self.input_profiles.extend([self.profile1, self.profile3])

        self.output_profiles = get_same_location('Alderman', self.input_profiles)

        self.correct_profiles = []
        self.correct_profiles.append(self.profile1)
        self.correct_profiles.append(self.profile2)
        self.correct_profiles.append(self.profile3)

        self.assertNotEqual(self.output_profiles, self.correct_profiles)
        # self.assertIs(True, True)

