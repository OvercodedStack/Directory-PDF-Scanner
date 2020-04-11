import sys
import csv
import os
import PyPDF4

#python Main.py C:\Users\LiTho\OneDrive\DR_WU_PAPERWORK_PUBLICATIONS


directory_pdfs = {}

def create_and_manage_csv(pdf_file_address,dict_pdfs_write):
    # pass_list = []
    # try:
    #     with open(pdf_file_address + '\\results.csv', 'r', newline='') as file:
    #         reader = csv.reader(file)
    #         pass_list.extend(reader)
    # except:
    #     print("Making new csv")
    #

    #data = {counter_pdfs:[counter_pdfs, pdf_file_obj.author, pdf_file_obj.subject, title, page_num]}
    with open( pdf_file_address + '\\results.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Index", "Author", "Subject", "Title"])
        index = 0
        for i, (k,j) in enumerate(dict_pdfs_write.items()):
            name = k
            obj_pdf = j
            title = ""

            if (j.title == None):
                title = name
            else:
                title = j.title

            writer.writerow([index, j.author, j.subject, title])
            index = index + 1



#######################################################################



#A helper for the pdf reader
def open_pdf(pdf_file_address, file_address_withoutpdf, name, counter_pdfs):
    pdfFile_obj = open(pdf_file_address,"rb")
    pdfReader = PyPDF4.PdfFileReader(pdfFile_obj)
    #print(pdfReader.numPages)

    # creating a page object
    information = pdfReader.getDocumentInfo()
    pageObj = pdfReader.getPage(0)
    txt = f"""
 
    Author: {information.author}
    Creator: {information.creator}
    Producer: {information.producer}
    Subject: {information.subject}
    Title: {information.title}
    Number of pages: {pdfReader.numPages}
    """

    #print(txt)
    #Open and drop in the file results.
    directory_pdfs.update({name:information})


    # closing the pdf file object
    pdfFile_obj.close()


#Check if the input is a single string and santized
if (len(sys.argv) <= 2 and type(sys.argv[1]) == str ):
    print("Valid input, printing...")
    print("There are " + str(len(os.listdir(sys.argv[1]))) + " matches in the directory.")
    print("==========================================================================")

    cnt_rows = 0
    #walk through the directory and seek pdfs to ship out to the pdf reader.
    counter = 0
    for x in os.listdir(sys.argv[1]):

        if (".pdf" in x):
            open_pdf(sys.argv[1] + "\\" + os.listdir(sys.argv[1])[counter], sys.argv[1],
                     x.replace(".pdf",""),cnt_rows)

            #x = x.replace(".pdf","")
            #print(x + "\n")
            cnt_rows =cnt_rows+1
        counter = counter + 1
    create_and_manage_csv(sys.argv[1],directory_pdfs)



    print("Done.")
else:
    #Immediately terminate
    print("Not valid input")










