from django.test import TestCase
from django.contrib.auth.models import User
from .views import get_same_location, get_students_only
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
        Tests if tutors are not at the same location
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
        self.correct_profiles.append(self.profile3)

        self.assertNotEqual(self.output_profiles, self.correct_profiles)
        # self.assertIs(True, True)

class tutor_tests(TestCase):

    def test_get_students_only(self):
        self.user1 = User.objects.create_user(username='testuser1', password='12345')
        self.user2 = User.objects.create_user(username='testuser2', password='12345')
        self.user3 = User.objects.create_user(username='testuser3', password='12345')

        self.profile1 = self.user1.userprofile
        self.profile1.is_tutor = True
        self.profile2 = self.user2.userprofile
        self.profile2.is_tutor = False
        self.profile3 = self.user3.userprofile
        self.profile3.is_tutor = False
        self.input_profiles = []
        self.input_profiles.extend([self.profile1, self.profile2, self.profile3])

        self.output_profiles = get_students_only(self.input_profiles)

        self.correct_profiles = []
        self.correct_profiles.append(self.profile2)
        self.correct_profiles.append(self.profile3)

        self.assertEqual(self.output_profiles, self.correct_profiles)


    def test_get_students_only(self):
        self.user1 = User.objects.create_user(username='testuser1', password='12345')
        self.user2 = User.objects.create_user(username='testuser2', password='12345')
        self.user3 = User.objects.create_user(username='testuser3', password='12345')

        self.profile1 = self.user1.userprofile
        self.profile1.is_tutor = True
        self.profile2 = self.user2.userprofile
        self.profile2.is_tutor = True
        self.profile3 = self.user3.userprofile
        self.profile3.is_tutor = False
        self.input_profiles = []
        self.input_profiles.extend([self.profile1, self.profile2, self.profile3])

        self.output_profiles = get_students_only(self.input_profiles)

        self.correct_profiles = []
        self.correct_profiles.append(self.profile2)
        self.correct_profiles.append(self.profile3)

        self.assertNotEqual(self.output_profiles, self.correct_profiles)


    def test_is_tutor_default(self):
        self.user1 = User.objects.create_user(username='testuser1', password='12345')
        self.user2 = User.objects.create_user(username='testuser2', password='12345')
        self.user3 = User.objects.create_user(username='testuser3', password='12345')
        self.profile1 = self.user1.userprofile
        self.profile2 = self.user2.userprofile
        self.profile3 = self.user3.userprofile
        self.input_profiles = []
        self.input_profiles.extend([self.profile1, self.profile2, self.profile3])
        self.output_profiles = get_students_only(self.input_profiles)
        self.correct_profiles = []
        self.correct_profiles.append(self.profile1)
        self.correct_profiles.append(self.profile2)
        self.correct_profiles.append(self.profile3)
        self.assertEqual(self.output_profiles, self.correct_profiles)

class userprofile_test(TestCase):

    def createusertest(self):
        self.user1 = User.objects.create_user(username='testuser1', password='12345')
        self.profile1 = self.user1.userprofile
        self.assertEqual(self.find_user(self.profile1), self.profile1)

    def find_user_test(self):
        self.user1 = User.objects.create_user(username='testuser1', password='12345')
        self.profile1 = self.user1.userprofile
        self.user2 = User.objects.create_user(username='testuser2', password='12345')
        self.profile2 = self.user2.userprofile
        self.assertNotEqual(self.find_user(self.profile2), self.profile1)

    def add_location_test(self):
        self.user1 = User.objects.create_user(username='testuser1', password='12345')
        self.profile1 = self.user1.userprofile
        self.profile1.location = 'Alderman'
        self.assertEqual('Alderman',self.profile1.location)

    def helped_test(self):
        self.user1 = User.objects.create_user(username='testuser1', password='12345')
        self.profile1 = self.user1.userprofile
        self.profile1.helped = False
        self.assertEqual(False,self.profile1.helped)
        self.profile1.helped = True
        self.assertEqual(True, self.profile1.helped)

    def firsttimeuser_test(self):
        self.usernew = User.objects.create_user(username='testusernew', password='12345')
        self.profilenew = self.usernew.userprofile
        self.assertEqual(True, self.profile1.first_time_user)

