from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from django.utils import timezone

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Clear existing data
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()

        # Create Teams
        marvel = Team.objects.create(name='marvel')
        dc = Team.objects.create(name='dc')

        # Create Users
        users = [
            User.objects.create(email='ironman@marvel.com', name='Iron Man', team='marvel'),
            User.objects.create(email='captainamerica@marvel.com', name='Captain America', team='marvel'),
            User.objects.create(email='batman@dc.com', name='Batman', team='dc'),
            User.objects.create(email='superman@dc.com', name='Superman', team='dc'),
        ]

        # Create Activities
        Activity.objects.create(user=users[0], type='run', duration=30, date=timezone.now().date())
        Activity.objects.create(user=users[1], type='cycle', duration=45, date=timezone.now().date())
        Activity.objects.create(user=users[2], type='swim', duration=60, date=timezone.now().date())
        Activity.objects.create(user=users[3], type='run', duration=25, date=timezone.now().date())

        # Create Leaderboard
        Leaderboard.objects.create(user=users[0], points=100)
        Leaderboard.objects.create(user=users[1], points=90)
        Leaderboard.objects.create(user=users[2], points=110)
        Leaderboard.objects.create(user=users[3], points=95)

        # Create Workouts
        Workout.objects.create(name='Hero HIIT', description='High intensity workout for heroes', suggested_for='marvel')
        Workout.objects.create(name='Justice Strength', description='Strength workout for justice league', suggested_for='dc')

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
