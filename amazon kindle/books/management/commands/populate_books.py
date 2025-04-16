from django.core.management.base import BaseCommand
from books.models import Book
from decimal import Decimal

class Command(BaseCommand):
    help = 'Populates the database with sample books across different categories'

    def handle(self, *args, **kwargs):
        # Clear existing books
        self.stdout.write('Clearing existing books...')
        Book.objects.all().delete()
        
        # Sample books data
        books_data = [
            # Fiction
            {
                'title': 'The Great Gatsby',
                'author': 'F. Scott Fitzgerald',
                'description': 'A story of the fabulously wealthy Jay Gatsby and his love for the beautiful Daisy Buchanan.',
                'price': Decimal('9.99'),
                'category': 'FICTION',
            },
            {
                'title': 'To Kill a Mockingbird',
                'author': 'Harper Lee',
                'description': 'The story of racial injustice and the loss of innocence in the American South.',
                'price': Decimal('12.99'),
                'category': 'FICTION',
            },
            {
                'title': '1984',
                'author': 'George Orwell',
                'description': 'A dystopian social science fiction novel and cautionary tale.',
                'price': Decimal('10.99'),
                'category': 'FICTION',
            },
            {
                'title': 'Pride and Prejudice',
                'author': 'Jane Austen',
                'description': 'A romantic novel of manners that satirizes 19th century society and the necessity of marrying for love.',
                'price': Decimal('8.99'),
                'category': 'FICTION',
            },
            {
                'title': 'The Catcher in the Rye',
                'author': 'J.D. Salinger',
                'description': 'A story of teenage alienation and loss of innocence in New York City.',
                'price': Decimal('11.99'),
                'category': 'FICTION',
            },
            
            # Non-Fiction
            {
                'title': 'Sapiens: A Brief History of Humankind',
                'author': 'Yuval Noah Harari',
                'description': 'A book exploring the history of the human species from evolution to the present day.',
                'price': Decimal('14.99'),
                'category': 'NONFICTION',
            },
            {
                'title': 'Becoming',
                'author': 'Michelle Obama',
                'description': 'A memoir by the former First Lady of the United States.',
                'price': Decimal('16.99'),
                'category': 'NONFICTION',
            },
            {
                'title': 'Educated',
                'author': 'Tara Westover',
                'description': 'A memoir about a woman who leaves her survivalist family and goes on to earn a PhD from Cambridge University.',
                'price': Decimal('15.99'),
                'category': 'NONFICTION',
            },
            {
                'title': 'Atomic Habits',
                'author': 'James Clear',
                'description': 'A guide to breaking bad habits and building good ones.',
                'price': Decimal('13.99'),
                'category': 'NONFICTION',
            },
            {
                'title': 'The Subtle Art of Not Giving a F*ck',
                'author': 'Mark Manson',
                'description': 'A counterintuitive approach to living a good life.',
                'price': Decimal('12.99'),
                'category': 'NONFICTION',
            },
            
            # Science
            {
                'title': 'A Brief History of Time',
                'author': 'Stephen Hawking',
                'description': 'An exploration of cosmology for the general reader.',
                'price': Decimal('14.99'),
                'category': 'SCIENCE',
            },
            {
                'title': 'The Selfish Gene',
                'author': 'Richard Dawkins',
                'description': 'A book on evolution that popularizes the gene-centered view of evolution.',
                'price': Decimal('13.99'),
                'category': 'SCIENCE',
            },
            {
                'title': 'Cosmos',
                'author': 'Carl Sagan',
                'description': 'A popular science book about the universe and humanity\'s place in it.',
                'price': Decimal('15.99'),
                'category': 'SCIENCE',
            },
            {
                'title': 'The Immortal Life of Henrietta Lacks',
                'author': 'Rebecca Skloot',
                'description': 'The story of a woman whose cells were taken without her knowledge and used for medical research.',
                'price': Decimal('12.99'),
                'category': 'SCIENCE',
            },
            {
                'title': 'The Sixth Extinction',
                'author': 'Elizabeth Kolbert',
                'description': 'An investigation of the current mass extinction of species caused by human activity.',
                'price': Decimal('14.99'),
                'category': 'SCIENCE',
            },
            
            # History
            {
                'title': 'Guns, Germs, and Steel',
                'author': 'Jared Diamond',
                'description': 'A book that attempts to explain why Eurasian civilizations have survived and conquered others.',
                'price': Decimal('15.99'),
                'category': 'HISTORY',
            },
            {
                'title': 'Sapiens: A Brief History of Humankind',
                'author': 'Yuval Noah Harari',
                'description': 'A book exploring the history of the human species from evolution to the present day.',
                'price': Decimal('14.99'),
                'category': 'HISTORY',
            },
            {
                'title': 'The Wright Brothers',
                'author': 'David McCullough',
                'description': 'The story of the two brothers who invented the first successful airplane.',
                'price': Decimal('13.99'),
                'category': 'HISTORY',
            },
            {
                'title': 'The Diary of a Young Girl',
                'author': 'Anne Frank',
                'description': 'The diary of a young Jewish girl during the Holocaust.',
                'price': Decimal('9.99'),
                'category': 'HISTORY',
            },
            {
                'title': 'The Rise and Fall of the Third Reich',
                'author': 'William L. Shirer',
                'description': 'A comprehensive history of Nazi Germany.',
                'price': Decimal('16.99'),
                'category': 'HISTORY',
            },
            
            # Business
            {
                'title': 'Rich Dad Poor Dad',
                'author': 'Robert Kiyosaki',
                'description': 'A personal finance book that emphasizes the importance of financial literacy and independence.',
                'price': Decimal('12.99'),
                'category': 'BUSINESS',
            },
            {
                'title': 'The 7 Habits of Highly Effective People',
                'author': 'Stephen R. Covey',
                'description': 'A self-help book that presents a principle-centered approach for solving personal and professional problems.',
                'price': Decimal('14.99'),
                'category': 'BUSINESS',
            },
            {
                'title': 'Good to Great',
                'author': 'Jim Collins',
                'description': 'A management book that describes how companies transition from being average companies to great companies.',
                'price': Decimal('15.99'),
                'category': 'BUSINESS',
            },
            {
                'title': 'Zero to One',
                'author': 'Peter Thiel',
                'description': 'A book about building startups and creating new things.',
                'price': Decimal('13.99'),
                'category': 'BUSINESS',
            },
            {
                'title': 'The Lean Startup',
                'author': 'Eric Ries',
                'description': 'A book about applying lean manufacturing principles to startups.',
                'price': Decimal('14.99'),
                'category': 'BUSINESS',
            },
            
            # Technology
            {
                'title': 'Clean Code',
                'author': 'Robert C. Martin',
                'description': 'A handbook of agile software craftsmanship.',
                'price': Decimal('16.99'),
                'category': 'TECHNOLOGY',
            },
            {
                'title': 'The Pragmatic Programmer',
                'author': 'Andrew Hunt and David Thomas',
                'description': 'A guide to software development best practices.',
                'price': Decimal('15.99'),
                'category': 'TECHNOLOGY',
            },
            {
                'title': 'Design Patterns',
                'author': 'Erich Gamma, Richard Helm, Ralph Johnson, and John Vlissides',
                'description': 'A book about software design patterns.',
                'price': Decimal('17.99'),
                'category': 'TECHNOLOGY',
            },
            {
                'title': 'The Mythical Man-Month',
                'author': 'Frederick P. Brooks Jr.',
                'description': 'A book about software project management.',
                'price': Decimal('14.99'),
                'category': 'TECHNOLOGY',
            },
            {
                'title': 'Code Complete',
                'author': 'Steve McConnell',
                'description': 'A comprehensive guide to software construction.',
                'price': Decimal('16.99'),
                'category': 'TECHNOLOGY',
            },
            
            # Biography
            {
                'title': 'Steve Jobs',
                'author': 'Walter Isaacson',
                'description': 'The biography of Apple co-founder Steve Jobs.',
                'price': Decimal('15.99'),
                'category': 'BIOGRAPHY',
            },
            {
                'title': 'Einstein: His Life and Universe',
                'author': 'Walter Isaacson',
                'description': 'A biography of Albert Einstein.',
                'price': Decimal('14.99'),
                'category': 'BIOGRAPHY',
            },
            {
                'title': 'Long Walk to Freedom',
                'author': 'Nelson Mandela',
                'description': 'The autobiography of Nelson Mandela.',
                'price': Decimal('13.99'),
                'category': 'BIOGRAPHY',
            },
            {
                'title': 'The Autobiography of Malcolm X',
                'author': 'Malcolm X with Alex Haley',
                'description': 'The autobiography of civil rights activist Malcolm X.',
                'price': Decimal('12.99'),
                'category': 'BIOGRAPHY',
            },
            {
                'title': 'Benjamin Franklin: An American Life',
                'author': 'Walter Isaacson',
                'description': 'A biography of Benjamin Franklin.',
                'price': Decimal('14.99'),
                'category': 'BIOGRAPHY',
            },
            
            # Children
            {
                'title': 'Charlotte\'s Web',
                'author': 'E.B. White',
                'description': 'The story of a pig named Wilbur and his friend Charlotte, a spider.',
                'price': Decimal('8.99'),
                'category': 'CHILDREN',
            },
            {
                'title': 'The Very Hungry Caterpillar',
                'author': 'Eric Carle',
                'description': 'The story of a caterpillar who eats his way through various foods before transforming into a butterfly.',
                'price': Decimal('7.99'),
                'category': 'CHILDREN',
            },
            {
                'title': 'Where the Wild Things Are',
                'author': 'Maurice Sendak',
                'description': 'The story of a boy named Max who is sent to bed without supper and imagines sailing away to the land of the Wild Things.',
                'price': Decimal('8.99'),
                'category': 'CHILDREN',
            },
            {
                'title': 'The Cat in the Hat',
                'author': 'Dr. Seuss',
                'description': 'The story of a cat who visits two children on a rainy day and causes chaos.',
                'price': Decimal('7.99'),
                'category': 'CHILDREN',
            },
            {
                'title': 'Harry Potter and the Sorcerer\'s Stone',
                'author': 'J.K. Rowling',
                'description': 'The first book in the Harry Potter series, following the adventures of a young wizard.',
                'price': Decimal('12.99'),
                'category': 'CHILDREN',
            },
            
            # Poetry
            {
                'title': 'The Waste Land',
                'author': 'T.S. Eliot',
                'description': 'A long poem that is considered one of the most important poems of the 20th century.',
                'price': Decimal('9.99'),
                'category': 'POETRY',
            },
            {
                'title': 'Leaves of Grass',
                'author': 'Walt Whitman',
                'description': 'A collection of poetry by Walt Whitman.',
                'price': Decimal('10.99'),
                'category': 'POETRY',
            },
            {
                'title': 'The Complete Poems of Emily Dickinson',
                'author': 'Emily Dickinson',
                'description': 'A collection of poetry by Emily Dickinson.',
                'price': Decimal('11.99'),
                'category': 'POETRY',
            },
            {
                'title': 'The Collected Poems of Langston Hughes',
                'author': 'Langston Hughes',
                'description': 'A collection of poetry by Langston Hughes.',
                'price': Decimal('12.99'),
                'category': 'POETRY',
            },
            {
                'title': 'The Sun and Her Flowers',
                'author': 'Rupi Kaur',
                'description': 'A collection of poetry about growth and healing.',
                'price': Decimal('10.99'),
                'category': 'POETRY',
            },
            
            # Other
            {
                'title': 'The Alchemist',
                'author': 'Paulo Coelho',
                'description': 'A philosophical novel about a young Andalusian shepherd and his journey to Egypt.',
                'price': Decimal('11.99'),
                'category': 'OTHER',
            },
            {
                'title': 'The Four Agreements',
                'author': 'Don Miguel Ruiz',
                'description': 'A self-help book that offers a code of conduct based on ancient Toltec wisdom.',
                'price': Decimal('10.99'),
                'category': 'OTHER',
            },
            {
                'title': 'The Power of Now',
                'author': 'Eckhart Tolle',
                'description': 'A self-help book that emphasizes the importance of living in the present moment.',
                'price': Decimal('12.99'),
                'category': 'OTHER',
            },
            {
                'title': 'The Art of War',
                'author': 'Sun Tzu',
                'description': 'An ancient Chinese text on military strategy and tactics.',
                'price': Decimal('9.99'),
                'category': 'OTHER',
            },
            {
                'title': 'The Little Prince',
                'author': 'Antoine de Saint-Exupéry',
                'description': 'A philosophical children\'s book about a young prince who visits various planets.',
                'price': Decimal('8.99'),
                'category': 'OTHER',
            },
        ]
        
        # Create books
        self.stdout.write('Creating books...')
        for book_data in books_data:
            Book.objects.create(**book_data)
        
        self.stdout.write(self.style.SUCCESS(f'Successfully created {len(books_data)} books')) 