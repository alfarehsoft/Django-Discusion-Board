
from boards.models import *
from django.core.management.base import BaseCommand
from django_seed import Seed
seeder = Seed.seeder()

def seed_boards(num):
    seeder.add_entity(Board,num)
    seeder.add_entity(Topic,num,{
        'boards.Topic.crated_by':7
    })
    seeder.execute()

class Command(BaseCommand):
    help = 'Seed the database with fake data.'

    def add_arguments(self, parser):
        parser.add_argument('number', type=int, help='Number of boards.')

    def handle(self, *args, **options):
        nums = options['number']
        seed_boards(nums)