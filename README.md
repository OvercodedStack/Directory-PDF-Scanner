# Directory-PDF-Scanner
Simple script for obtaining the names and information from PDF files located inside a directory and output directly to a CSV file. This program is intended to simplify research work for PDF files, specifically those for research papers.

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
