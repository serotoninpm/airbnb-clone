from django.core.management.base import BaseCommand


class Command(BaseCommand):

    help = "This command tells me that he loves me"

    def add_arguments(self, parser):
        parser.add_argument(
            "--times", help="How many times do you want me to tell....."
        )

    def handle(self, *args, **options):
        times = options.get("times")
        for t in range(int(times)):
            self.stdout.write(self.style.SUCCESS("i love you"))