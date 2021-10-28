#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 25 22:41:55 2021

@author: gabrielsoto
"""

import os, sys
import bibtexparser as btp

def main(bibfile, me):
    """ Method to read in bib file entries and convert to markdown language
    
    Each entry is formatted in a way that I prefer and written to a text file
    in markdown language. The entries are divided into: first author journal 
    articles, first author conference papers, and contributing authors. Entries
    are considered contributing author if they are not the first author in the 
    author list. Final format is generally:
        Author[s] (Year) "Publication Title" Publisher [Link]
    
    Inputs:
        bibfile : str
            Filename for bib file.
        me : str
            Name of main author.

    """
    with open(bibfile) as f:
        bib_data = btp.load(f)
    
    # numer of entries in bib file
    E = len( bib_data.entries )
    
    first_author_journal = []
    first_author_confrcn = []
    contr_author = []
    
    # =============================================================================
    # looping through entries
    for e in range(E):
        entry = bib_data.entries[e]
        full_txt = ''
        
        # ==========================
        # AUTHORS 
        authors = entry['author']
        authors_names = authors.split(' and ')
    
        for a, auth in enumerate(authors_names):
            phrases = auth.split(' ')
            # if it's not {Last Name, First Name} then we re-format it
            if ',' not in authors:
                # this is the case where there is a middle name or initial
                if len(phrases) > 2:
                    phrases = [ '{0}. {1}'.format(phrases[0][0], phrases[1]), phrases[2] ] # just using first letter of first name
                else:
                    phrases = [ '{0}.'.format(phrases[0][0]), phrases[1]]
                # switching the name order
                authors_names[a] = '{0}, {1}'.format(phrases[1], phrases[0])
            else:
                # this is the case where there is a middle name or initial
                if len(phrases) > 2:
                    phrases = [phrases[0], '{0}. {1}'.format(phrases[1][0], phrases[2]) ] # just using first letter of first name
                else:
                    phrases = [phrases[0], '{0}.'.format( phrases[1][0] ) ] 
                authors_names[a] = '{0} {1}'.format(phrases[0], phrases[1])
            
        # authors portion
        for auth in authors_names:
            if auth == me:
                full_txt += '**{0}**, '.format(auth)
            else:
                full_txt += '{0}, '.format(auth)
        
        # ==========================
        # YEARS 
        year = entry['year']
        full_txt += '({0}) '.format(year)
        
        # ==========================
        # TITLE
        title = entry['title']
        full_txt += '"{0}" '.format(title)
        
        # ==========================
        # PUBLICATION
        entrytype = entry['ENTRYTYPE']
        
        publication = entry['journal'] if entrytype=='article' else \
                      'Proceedings from {0} - {1}'.format(entry['publisher'], entry['booktitle']) if entrytype=='inproceedings' else ''
        
        full_txt += '*{0}*. '.format(publication)
    
        # ==========================
        # URL
        url = entry['url']
        
        full_txt += '[Link]({0}).'.format(url)
        
        # =========================================================================
        # storing this entry
        
        # first author    
        if full_txt[0] == '*':
            # conference paper
            if publication.split(' ')[0] == "Proceedings":
                first_author_confrcn.append(full_txt)
            # journal paper
            else:
                first_author_journal.append(full_txt)
        else:
            contr_author.append(full_txt)
    
    # full text output to be written
    print_txt  = 'First Author Journal Publications \n\n'
    print_txt += '\n'.join(first_author_journal)
    print_txt += '\n\nFirst Author Conference Paper \n\n' + '\n'.join(first_author_confrcn)
    print_txt += '\n\nContributing Author \n\n' + '\n'.join(contr_author)
    
    # this filename should be the same name as the bib file
    output_filename = bibfile.split('.')[-2]
    output_dirname  = os.path.dirname( os.path.realpath(__file__) )
    output_filepath = os.path.join( output_dirname, 'outputs', output_filename + '.txt')
    
    # writing to file
    text_file = open(output_filepath, 'w')
    text_file.write( print_txt )
    text_file.close()


if __name__=="__main__":
    # main("bib_sample.bib", "Soto, G. J.") #example of a main call
    main( sys.argv[1], sys.argv[2])