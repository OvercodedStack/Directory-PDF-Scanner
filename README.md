# Directory-PDF-Scanner
Simple script for obtaining the names and information from PDF files located inside a directory and output directly to a CSV file. This program is intended to simplify research work for PDF files, specifically those for research papers.


# Version 0.1 Uploaded
## Features: 
* Ability to scan through one directory and print out a .CSV file in the directory it was ran in
* Ability to recognize most of the names of PDF files and place them into the .CSV file
* Supports currently the following labels from the PDF:
  * Index count
  * Author
  * Subject
  * Title 

## Requirements: 
* Python 3.6+
* PyPDF4 (Install in your favorite VEnv for Python using pip)

## How to use: 

* Simply use as a command line prompt in your python command line
`python <directory where this script was installed>\Main.py <directory to be scanned>`  

If on windows, use this handy feature to locate the exact execution location: 

![How_to](https://raw.githubusercontent.com/OvercodedStack/Directory-PDF-Scanner/master/Copy_paste.png)

## Goals

This program was built out of frustration in trying to track what you have read so far. While printing out all your papers is easy, it's probably not cheap or environmentally friendly. This program intends to change that by helping you to simply drop all the details into a CSV file for Excel or LibreOffice manipulation. Current features include: 

* Openning the PDFs and attempt to detect Author and Title
* Create a CSV file and allocate details to it
* Current details that can be detected include: 
  * Author
  * Title
  * Index of paper as read from directoy
  * Some publisher details


## Future Plans

This planned to become a larger program which will utilize Optical Character Recognition to read through PDFs and determine character from a paper and automatically fill in the missing details.

Missing details will include:
* Publisher details
* Page Number
* Conference published at
* Authors
* Keywords
* Abstract

## License

This is licensed under the MIT license. 
