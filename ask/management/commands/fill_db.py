# -*- coding: utf-8 -*-

import os
import random
import time
from os import path
from django import db
from django.conf import settings
from django.core.management.base import BaseCommand


counter = 1
f = open(path.join(settings.BASE_DIR, 'res', 'words-en.txt'), 'rb')
WORDS = f.read().split('\n')
f.close()
unique_words_counter = 1


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
    f = '%Y-%m-%d %H:%M:%S'
    start_time = time.mktime(time.strptime('1995-01-01 01:01:01', f))
    end_time = time.mktime(time.strptime('2015-01-01 01:01:01', f))
    t = start_time + (end_time - start_time) * random.random()
    return time.strftime(f, time.localtime(t))

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
    write_entry(response_file, random.randint(1, QUESTIONS_COUNT))
    write_entry(response_file, random.randint(0, 1))
    write_entry(response_file, get_date())
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


USERS_COUNT = 13000
QUESTIONS_COUNT = 120000
RESPONSES_COUNT = 1200000
TAGS_COUNT = 120
QUESTION_TAGS_COUNT = QUESTIONS_COUNT * 3

SIMPLE_TABLES = {
    'ask_question': {
        'WRITER': write_question,
        'COUNT': QUESTIONS_COUNT,
    },
    'ask_response': {
        'WRITER': write_response,
        'COUNT': RESPONSES_COUNT
    },
    'ask_tag': {
        'WRITER': write_tag,
        'COUNT': TAGS_COUNT
    },
    'ask_question_tags': {
        'WRITER': write_question_tag,
        'COUNT': QUESTION_TAGS_COUNT
    },
}


def fill_table(cursor, table, filename):
    cursor.execute('LOAD DATA INFILE %s IGNORE INTO TABLE ' + table, [filename, ])

def get_filename(table):
    return path.join(settings.BASE_DIR, table + '.csv')

class Command(BaseCommand):
    help = 'Fills the DB with some random data.'

    def handle(self, *args, **options):
        cursor = db.connection.cursor()
        cursor.execute('SET foreign_key_checks = 0')

        auth_user_filename = get_filename('auth_user')
        ask_user_filename = get_filename('ask_user')
        django_user = open(auth_user_filename, 'wb')
        ask_user = open(ask_user_filename, 'wb')
        for i in xrange(USERS_COUNT):
            write_user(django_user, ask_user)
        django_user.close()
        ask_user.close()
        fill_table(cursor, 'auth_user', auth_user_filename)
        fill_table(cursor, 'ask_user', ask_user_filename)
        os.remove(auth_user_filename)
        os.remove(ask_user_filename)

        for table, info in SIMPLE_TABLES.iteritems():
            counter = 1
            filename = get_filename(table)
            f = open(filename, 'wb')
            writer = info['WRITER']
            for i in xrange(info['COUNT']):
                writer(f)
            f.close()
            fill_table(cursor, table, filename)
            os.remove(filename)

        cursor.execute('SET foreign_key_checks = 1')
