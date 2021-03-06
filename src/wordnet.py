"""
Some utilities for the usae of WordNet emotion words.
Author: Kyle Hardgrave (kyleh@seas)
"""
import os
from collections import defaultdict

WORDNET_ROOT = '/home1/k/kyleh/nlp/lexicons/wordnet'
WORDNET_EMOTIONS = ['anger', 'disgust', 'fear', 'joy', 'sadness', 'surprise']


def get_emotion_words(emotion, path=WORDNET_ROOT):
  """Return a set of the words representing a given emotion."""
  with open(os.path.join(path, '%s.txt' % emotion)) as f:
    return set(word for word in f.read().split() if not word[1] == '#')


def get_word_emotion_map(path=WORDNET_ROOT, emotions=WORDNET_EMOTIONS):
  """Return a dictionary of words to list of emotions."""
  emotions_dict = defaultdict(list)
  for emotion in emotions:
    for word in emotion_words(emotion, path):
      emotions_dict[word].append(emotion)
  return dict(emotions_dict)
