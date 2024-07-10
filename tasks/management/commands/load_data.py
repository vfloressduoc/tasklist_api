
from django.core.management.base import BaseCommand
from tasks.models import MotivationalQuote, Reminder

class Command(BaseCommand):
    help = 'Carga inical de frases y recordatorios en la base de datos'

    def handle(self, *args, **kwargs):
        # Agregar frases
        quotes = [
            ("No te conformes con menos de lo que mereces.", "Unknown"),
            ("Fallar es parte del éxito. Cada tropiezo te acerca más a tus metas.", "Michael Jordan"),
            ("Sé tú mismo y arrasa todos los días.", "Unknown"),
            ("Confía en ti mismo y todo será posible.", "Unknown"),
            ("Disfruta lo que haces y lo harás genial.", "Steve Jobs"),
            ("No dejes que el miedo te detenga. Ve por lo que quieres.", "Robert Kiyosaki"),
            ("Tu tiempo es tuyo, úsalo sabiamente.", "Steve Jobs"),
            ("La felicidad es la clave del éxito, no al revés.", "Albert Schweitzer"),
            ("La vida es 10% lo que te pasa y 90% cómo reaccionas.", "Charles R. Swindoll"),
            ("La suerte es la combinación perfecta de preparación y oportunidad.", "Seneca")
        ]

        for quote, author in quotes:
            MotivationalQuote.objects.create(
                quote_text=quote,
                author=author
            )

        # Agregar recordatorios
        reminders = [
            "No olvides tomar breaks para mantener tu energía alta.",
            "Mantén una actitud positiva incluso cuando las cosas se pongan difíciles.",
            "Si necesitas ayuda, pídela. No tienes que hacerlo solo/a.",
            "Establece metas claras y trabaja duro para lograrlas.",
            "Haz tiempo para desconectar y hacer lo que te gusta.",
            "Cuida tu salud mental y física. Escucha a tu cuerpo.",
            "Aprovecha cada oportunidad para aprender algo nuevo.",
            "Rodéate de personas que te inspiren y motiven.",
            "No te compares con los demás. Cada uno tiene su propio camino.",
            "Confía en ti mismo/a y en tus habilidades para superar cualquier obstáculo."
        ]

        for reminder in reminders:
            Reminder.objects.create(
                text=reminder
            )

        self.stdout.write(self.style.SUCCESS('Datos cargados exitosamente en la base de datos.'))
