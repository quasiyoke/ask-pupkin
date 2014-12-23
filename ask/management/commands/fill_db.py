# -*- coding: utf-8 -*-

from django.core.management.base import BaseCommand
import random


counter = 1
f = open('/home/quasiyoke/ya/text/words-en.txt')
WORDS = f.read().split('\r\n')
f.close()
unique_words_counter = 1

USERS_COUNT = 13000
QUESTIONS_COUNT = 120000
RESPONSES_COUNT = 1200000
TAGS_COUNT = 120
QUESTION_TAGS_COUNT = QUESTIONS_COUNT * 3


def write_entry(f, s):
    f.write(str(s))
    f.write('\t')

    
def get_word():
    return random.choice(WORDS)

def get_sentence():
    s = ' '.join([get_word() for i in xrange(random.randint(3, 15))])
    s = s[0].upper() + s[1:] + '.'
    return s

def get_question():
    s = ' '.join([get_word() for i in xrange(random.randint(3, 15))])
    s = s[0].upper() + s[1:] + '?'
    return s

def get_text():
    s = ' '.join([get_sentence() for i in xrange(random.randint(3, 15))])
    return s

def get_email():
    return '%s@%s.com' % (get_unique_word(), get_unique_word(), )

def get_date():
    return '2014-12-23 11:13:42'

def get_unique_word():
    global unique_words_counter
    unique_words_counter += 1
    while not WORDS[unique_words_counter]:
        unique_words_counter += 1
    return WORDS[unique_words_counter]

def end_entry(f):
    f.write('\n')
    

def write_user(django_file, ask_file):
    global counter
    write_entry(django_file, str(counter))
    write_entry(django_file, 'pbkdf2_sha256$12000$D7RZV4A5ep3C$sEkgOSCvc5DBRLYn2qO0Tf3l8GRROxSBKh+FGzgJGOw=')
    write_entry(django_file, get_date())
    write_entry(django_file, 0)
    write_entry(django_file, get_unique_word())
    write_entry(django_file, '')
    write_entry(django_file, '')
    write_entry(django_file, get_email())
    write_entry(django_file, 0)
    write_entry(django_file, 1)
    write_entry(django_file, get_date())
    end_entry(django_file)

    write_entry(ask_file, counter)
    write_entry(ask_file, counter)
    write_entry(ask_file, '')
    write_entry(ask_file, random.randint(-20, 300))
    end_entry(ask_file)
    counter += 1

def write_question(question_file):
    global counter
    write_entry(question_file, counter)
    write_entry(question_file, get_question())
    write_entry(question_file, get_text())
    write_entry(question_file, random.randint(1, USERS_COUNT))
    write_entry(question_file, get_date())
    end_entry(question_file)
    counter += 1

def write_response(response_file):
    global counter
    write_entry(response_file, counter)
    write_entry(response_file, get_text())
    write_entry(response_file, random.randint(1, USERS_COUNT))
    write_entry(response_file, random.randint(0, 1))
    end_entry(response_file)
    counter += 1

def write_tag(response_file):
    global counter
    write_entry(response_file, counter)
    write_entry(response_file, get_unique_word())
    end_entry(response_file)
    counter += 1

def write_question_tag(response_file):
    global counter
    write_entry(response_file, counter)
    write_entry(response_file, random.randint(1, QUESTIONS_COUNT))
    write_entry(response_file, random.randint(1, TAGS_COUNT))
    end_entry(response_file)
    counter += 1


class Command(BaseCommand):
    help = 'Fills the DB with some random data.'

    def handle(self, *args, **options):
        django_user = open('django_user.dat', 'wb')
        ask_user = open('ask_user.dat', 'wb')
        for i in xrange(USERS_COUNT):
            write_user(django_user, ask_user)
        f.close()
        f.close()

        counter = 1
        question = open('question.dat', 'wb')
        for i in xrange(QUESTIONS_COUNT):
            write_question(question)
        question.close()

        counter = 1
        response = open('response.dat', 'wb')
        for i in xrange(RESPONSES_COUNT):
            write_response(response)        
        response.close()

        counter = 1
        unique_words_counter = 1
        tag = open('tag.dat', 'wb')
        for i in xrange(TAGS_COUNT):
            write_tag(tag)        
        tag.close()

        counter = 1
        question_tag = open('question_tag.dat', 'wb')
        for i in xrange(QUESTION_TAGS_COUNT):
            write_question_tag(question_tag)        
        question_tag.close()
