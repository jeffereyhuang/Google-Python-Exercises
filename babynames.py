#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re

"""Baby Names exercise

Define the extract_names() function below and change main()
to call it.
"""

def extract_names(filename):

  f = open(filename, 'r'); ##what is this? string or what
  year = re.findall(r'Popularity in (\d\d\d\d)', f.read());
  f.seek(0);
  names = re.findall(r'<td>(\d+)</td><td>(\w+)</td><td>(\w+)', f.read());
  rankings = year;
  for name in names:
    i = 0;
    rank = name[i + 1] + " " + name[i];
    rankings.append(rank);
    rank = name[i + 2] + " " + name[i];
    rankings.append(rank);
    i += 1;
  f.close();
  return sorted(rankings);


def main():
  # This command-line parsing code is provided.
  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]

  if not args:
    print 'usage: [--summaryfile] file [file ...]'
    sys.exit(1)

  # Notice the summary flag and remove it from args if it is present.
  summary = False
  if args[0] == '--summaryfile':
    summary = True
    del args[0]
    
  rankings = extract_names(sys.argv[1]);
  for ranking in rankings:
    print ranking;
  
  
if __name__ == '__main__':
  main()
