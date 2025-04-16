from django.core.management.base import BaseCommand
from books.models import Book
from django.conf import settings
import os
from django.core.files.base import ContentFile

class Command(BaseCommand):
    help = 'Generates sample book content files for all books'

    def handle(self, *args, **options):
        # Create media directory if it doesn't exist
        media_root = settings.MEDIA_ROOT
        books_dir = os.path.join(media_root, 'book_files')
        os.makedirs(books_dir, exist_ok=True)

        # Get all books
        books = Book.objects.all()
        self.stdout.write(f'Found {books.count()} books to process')

        for book in books:
            self.stdout.write(f'Generating content for "{book.title}"...')
            
            # Generate sample content based on book category
            content = self.generate_sample_content(book)
            
            # Create filename
            filename = f'book_{book.id}_content.txt'
            
            # Save the content file
            book.book_file.save(filename, ContentFile(content.encode()), save=True)
            self.stdout.write(self.style.SUCCESS(f'Successfully generated content for "{book.title}"'))

        self.stdout.write(self.style.SUCCESS('Successfully generated all book content files'))

    def generate_sample_content(self, book):
        # Generate different sample content based on book category
        if book.category == 'FICTION':
            return self.generate_fiction_content(book)
        elif book.category == 'NONFICTION':
            return self.generate_nonfiction_content(book)
        elif book.category == 'SCIENCE':
            return self.generate_science_content(book)
        elif book.category == 'HISTORY':
            return self.generate_history_content(book)
        elif book.category == 'BIOGRAPHY':
            return self.generate_biography_content(book)
        elif book.category == 'BUSINESS':
            return self.generate_business_content(book)
        elif book.category == 'TECHNOLOGY':
            return self.generate_technology_content(book)
        elif book.category == 'CHILDREN':
            return self.generate_children_content(book)
        elif book.category == 'POETRY':
            return self.generate_poetry_content(book)
        else:
            return self.generate_general_content(book)

    def generate_fiction_content(self, book):
        return f"""Chapter 1: The Beginning

{book.title}

By {book.author}

It was a bright cold day in April, and the clocks were striking thirteen. Winston Smith, his chin nuzzled into his breast in an effort to escape the vile wind, slipped quickly through the glass doors of Victory Mansions, though not quickly enough to prevent a swirl of gritty dust from entering along with him.

The hallway smelt of boiled cabbage and old rag mats. At one end of it a coloured poster, too large for indoor display, had been tacked to the wall. It depicted simply an enormous face, more than a metre wide: the face of a man of about forty-five, with a heavy black moustache and ruggedly handsome features.

[Sample content continues...]

This is a sample content file for {book.title}. In a real application, this would contain the actual book content."""

    def generate_nonfiction_content(self, book):
        return f"""Introduction

{book.title}

By {book.author}

In this groundbreaking work, we explore the fascinating world of {book.title.lower()}. This book aims to provide readers with a comprehensive understanding of the subject matter, drawing from years of research and practical experience.

Chapter 1: Understanding the Basics

The fundamental principles that underlie {book.title.lower()} are both simple and complex. On the one hand, we have basic concepts that anyone can grasp; on the other, we have intricate details that require careful study and contemplation.

[Sample content continues...]

This is a sample content file for {book.title}. In a real application, this would contain the actual book content."""

    def generate_science_content(self, book):
        return f"""Preface

{book.title}

By {book.author}

The study of {book.title.lower()} represents one of the most exciting frontiers in modern science. This book presents a comprehensive overview of current research and developments in the field, making complex concepts accessible to readers of all backgrounds.

Chapter 1: The Scientific Method

Science is not just a collection of facts. It's a way of thinking, a method of approaching problems, and a process for understanding the natural world.

[Sample content continues...]

This is a sample content file for {book.title}. In a real application, this would contain the actual book content."""

    def generate_history_content(self, book):
        return f"""Foreword

{book.title}

By {book.author}

History is not merely a record of past events; it is a window into the human experience. This book explores the fascinating journey of {book.title.lower()}, examining how past events have shaped our present and continue to influence our future.

Chapter 1: The Origins

The story begins in a time when the world was very different from what we know today. Understanding these origins is crucial to comprehending the full scope of {book.title.lower()}.

[Sample content continues...]

This is a sample content file for {book.title}. In a real application, this would contain the actual book content."""

    def generate_biography_content(self, book):
        return f"""Prologue

{book.title}

By {book.author}

The life of {book.title.split(':')[0] if ':' in book.title else book.title} is a remarkable tale of triumph, tragedy, and transformation. This biography delves deep into the personal and professional journey of one of history's most fascinating figures.

Chapter 1: Early Years

The story begins in {book.title.split(':')[0] if ':' in book.title else book.title}'s childhood, a period that would shape the course of their life and legacy.

[Sample content continues...]

This is a sample content file for {book.title}. In a real application, this would contain the actual book content."""

    def generate_business_content(self, book):
        return f"""Introduction

{book.title}

By {book.author}

In today's rapidly evolving business landscape, understanding {book.title.lower()} is more crucial than ever. This book provides practical insights and strategies for navigating the complex world of modern business.

Chapter 1: The Fundamentals

Success in business requires a solid foundation of knowledge and skills. This chapter explores the essential principles that every business professional should understand.

[Sample content continues...]

This is a sample content file for {book.title}. In a real application, this would contain the actual book content."""

    def generate_technology_content(self, book):
        return f"""Preface

{book.title}

By {book.author}

Technology is transforming our world at an unprecedented pace. This book explores the latest developments in {book.title.lower()}, providing readers with a comprehensive understanding of current trends and future possibilities.

Chapter 1: The Digital Revolution

The technological landscape is constantly evolving, bringing new opportunities and challenges. Understanding these changes is essential for staying ahead in the digital age.

[Sample content continues...]

This is a sample content file for {book.title}. In a real application, this would contain the actual book content."""

    def generate_children_content(self, book):
        return f"""Once upon a time...

{book.title}

By {book.author}

In a world full of wonder and magic, there lived a special character who would change everything. This is their story, a tale of adventure, friendship, and discovery that will capture the imaginations of young readers everywhere.

Chapter 1: The Adventure Begins

The sun was shining brightly on the day our story begins. Birds were singing, flowers were blooming, and something extraordinary was about to happen...

[Sample content continues...]

This is a sample content file for {book.title}. In a real application, this would contain the actual book content."""

    def generate_poetry_content(self, book):
        return f"""{book.title}

By {book.author}

I.
In the quiet of the morning,
When the world is still asleep,
Thoughts like gentle whispers,
Through my mind do creep.

II.
Words flow like a river,
Through the pages of my mind,
Each verse a new discovery,
Each stanza a new find.

[Sample content continues...]

This is a sample content file for {book.title}. In a real application, this would contain the actual book content."""

    def generate_general_content(self, book):
        return f"""Introduction

{book.title}

By {book.author}

Welcome to this exploration of {book.title.lower()}. This book aims to provide readers with a comprehensive understanding of the subject, combining theoretical knowledge with practical insights.

Chapter 1: Getting Started

The journey begins here, with an introduction to the fundamental concepts that form the foundation of our exploration.

[Sample content continues...]

This is a sample content file for {book.title}. In a real application, this would contain the actual book content.""" 