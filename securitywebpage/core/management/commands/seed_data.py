from django.core.management.base import BaseCommand
from django.core.files.base import File
from django.db import transaction
from pathlib import Path
from core.models import ResearchTopic, Member, Publication


class Command(BaseCommand):
    help = 'Populate the database with sample data'

    def handle(self, *args, **kwargs):
        self.stdout.write('Seeding database...')

        if ResearchTopic.objects.exists():
            self.stdout.write(self.style.WARNING('Research topics already exist. Skipping.'))
        else:
            topics_data = [
                {
                    'title': 'Privacy and Data Protection',
                    'description': 'Formal change impact analysis of privacy policies, data protection regulations, and privacy-preserving technologies to ensure compliance and safeguard user data.',
                },
                {
                    'title': 'Formal Verification of Protocols and Systems',
                    'description': 'Verifying the security properties of cryptographic protocols, secure multi-party computation, and distributed systems using formal methods and model checking techniques.',
                },
                {
                    'title': 'AI and Security',
                    'description': 'Investigating the use of Large Language Models (LLMs) for security applications, including adversarial attacks, defenses, and the development of secure AI systems.',
                },
            ]

            for topic_data in topics_data:
                topic = ResearchTopic.objects.create(**topic_data)
                self.stdout.write(self.style.SUCCESS(f'Created topic: {topic.title}'))

        if Member.objects.exists():
            Member.objects.all().delete()

        members_data = [
            {
                'full_name': 'Prof. David Basin',
                'role': 'Group Lead',
                'category': Member.Category.FACULTY,
                'topic': 'Cybersecurity, Information Security, Formal Methods',
                'personal_website': 'https://insait.ai/prof-david-basin/',
                'photo_name': 'david-basin.jpg',
            },
            {
                'full_name': 'Nadia Markova',
                'role': 'PhD Student',
                'category': Member.Category.PHD,
                'topic': 'Formal Methods, Data Privacy',
                'email': 'nadia.markova@insait.ai',
                'personal_website': 'https://insait.ai/nadia-markova/',
                'photo_name': 'nadia-markova.PNG',
            },
        ]

        with transaction.atomic():
            for member_data in members_data:
                photo_name = member_data.pop('photo_name')
                member = Member.objects.create(**member_data)
                member.photo.save(photo_name, File(open(Path(__file__).resolve().parent.parent.parent.parent / 'media' / 'members' / photo_name, 'rb')))
                self.stdout.write(self.style.SUCCESS(f'Created member: {member.full_name}'))



        if Publication.objects.exists():
            self.stdout.write(self.style.WARNING('Publications already exist. Skipping.'))
        else:
            publications_data = [
                {
                    'title': 'Placeholder Title for Publication 1',
                    'authors': 'Placeholder Author 1, Placeholder Author 2',
                    'year': 2026,
                    'conference': 'Placeholder Conference 2026',
                    'paper_link': 'Placeholder Paper Link',
                    'project_link': 'Placeholder Project Link',
                },
                {
                    'title': 'Placeholder Title for Publication 2',
                    'authors': 'Placeholder Author 1, Placeholder Author 2',
                    'year': 2026,
                    'conference': 'Placeholder Conference 2026',
                    'paper_link': 'Placeholder Paper Link',
                    'project_link': 'Placeholder Project Link',
                },
                {
                    'title': 'Placeholder Title for Publication 3',
                    'authors': 'Placeholder Author 1, Placeholder Author 2',
                    'year': 2026,
                    'conference': 'Placeholder Conference 2026',
                    'paper_link': 'Placeholder Paper Link',
                    'project_link': 'Placeholder Project Link',
                },
                {
                    'title': 'Placeholder Title for Publication',
                    'authors': 'Placeholder Author 1, Placeholder Author 2',
                    'year': 2025,
                    'conference': 'Placeholder Conference 2025',
                    'paper_link': 'Placeholder Paper Link',
                    'project_link': 'Placeholder Project Link',
                },
            ]

            for pub_data in publications_data:
                pub = Publication.objects.create(**pub_data)
                self.stdout.write(self.style.SUCCESS(f'Created publication: {pub.title}'))

        self.stdout.write(self.style.SUCCESS('\nDatabase seeding complete!'))
