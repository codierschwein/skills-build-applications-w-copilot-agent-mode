from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard
from django.db import transaction

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        with transaction.atomic():
            self.stdout.write(self.style.WARNING('Lösche alte Daten ...'))
            Activity.objects.all().delete()
            Leaderboard.objects.all().delete()
            Workout.objects.all().delete()
            User.objects.all().delete()
            Team.objects.all().delete()

            self.stdout.write(self.style.SUCCESS('Lege Teams an ...'))
            marvel = Team.objects.create(name='Marvel', description='Marvel Superhelden')
            dc = Team.objects.create(name='DC', description='DC Superhelden')

            self.stdout.write(self.style.SUCCESS('Lege Users an ...'))
            users = [
                User.objects.create(email='ironman@marvel.com', username='Iron Man', team=marvel),
                User.objects.create(email='spiderman@marvel.com', username='Spider-Man', team=marvel),
                User.objects.create(email='batman@dc.com', username='Batman', team=dc),
                User.objects.create(email='wonderwoman@dc.com', username='Wonder Woman', team=dc),
            ]

            self.stdout.write(self.style.SUCCESS('Lege Workouts an ...'))
            workout1 = Workout.objects.create(name='Pushups', description='20 Pushups')
            workout2 = Workout.objects.create(name='Running', description='5km Lauf')
            workout1.suggested_for.add(marvel, dc)
            workout2.suggested_for.add(marvel, dc)

            self.stdout.write(self.style.SUCCESS('Lege Activities an ...'))
            Activity.objects.create(user=users[0], activity_type='Pushups', duration=10)
            Activity.objects.create(user=users[1], activity_type='Running', duration=30)
            Activity.objects.create(user=users[2], activity_type='Pushups', duration=15)
            Activity.objects.create(user=users[3], activity_type='Running', duration=25)

            self.stdout.write(self.style.SUCCESS('Lege Leaderboard an ...'))
            Leaderboard.objects.create(team=marvel, points=100)
            Leaderboard.objects.create(team=dc, points=80)

            self.stdout.write(self.style.SUCCESS('Testdaten erfolgreich angelegt!'))
