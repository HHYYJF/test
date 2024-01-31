import random
from django_seed import Seed
from test.models import Requisite, PaymentRequest
seeder = Seed.seeder()

def generate_phone_number(x):
    return ''.join([str(random.randint(0, 9)) for _ in range(10)])

requisites = Requisite.objects.all()  # Assuming that Requisite objects exist in the database

seeder.add_entity(
    Requisite,
    150,
    {
        'pay': lambda x: random.choice(['Карта', 'Cчет']),
        'account': lambda x: seeder.faker.text(max_nb_chars=50),
        'owner': lambda x: seeder.faker.name(),
        'number': generate_phone_number,
        'limit': lambda x: round(random.uniform(1000, 1000000), 2)
    }
)
for _ in range(5):
    requisite = Requisite.objects.order_by('?').first()
    seeder.add_entity(
        PaymentRequest,
        5500,
        {
            'sum': lambda x: round(random.uniform(1000, 100000), 2),
            'req': requisite,
            'status': lambda x: random.choice(['Ожидает', 'Оплачена', 'Отменена'])
        }
    )
inserted_pks = seeder.execute()