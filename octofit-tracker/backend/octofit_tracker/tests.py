from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class ModelSmokeTest(TestCase):
    def test_team_create(self):
        team = Team.objects.create(name='Marvel', description='Marvel Heroes')
        self.assertEqual(str(team), 'Marvel')
    def test_user_create(self):
        team = Team.objects.create(name='DC', description='DC Heroes')
        user = User.objects.create(email='batman@dc.com', username='batman', team=team)
        self.assertEqual(str(user), 'batman')
    def test_activity_create(self):
        team = Team.objects.create(name='Test', description='Test Team')
        user = User.objects.create(email='test@user.com', username='test', team=team)
        activity = Activity.objects.create(user=user, activity_type='run', duration=30)
        self.assertEqual(activity.activity_type, 'run')
    def test_workout_create(self):
        team = Team.objects.create(name='WorkoutTeam', description='Team')
        workout = Workout.objects.create(name='Pushups', description='Do pushups')
        workout.suggested_for.add(team)
        self.assertEqual(str(workout), 'Pushups')
    def test_leaderboard_create(self):
        team = Team.objects.create(name='LBTeam', description='Team')
        lb = Leaderboard.objects.create(team=team, points=100)
        self.assertEqual(str(lb), 'LBTeam - 100 Punkte')
