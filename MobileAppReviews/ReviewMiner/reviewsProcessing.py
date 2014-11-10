__author__ = 'Chetan'

import csv
import re
import nltk.corpus
from nltk import word_tokenize
import xlrd



def getprocessedreviews():

    performance = "Performance"
    userinterface = "UserInterface"
    compatibility = "Compatibility"
    request = "Request"
    general = "General"

    performance_total = 0
    userinterface_total = 0
    compatibility_total = 0
    request_total = 0
    general_total = 0

    performance_tags = []
    userinterface_tags = []
    compatibility_tags = []
    request_tags = []
    general_tags = []
    hit_words_tags = []


    performance_final_list = []
    userinterface_final_list = []
    compatibility_final_list = []
    request_final_list = []
    general_final_list = []
    all_reviews = []
    all_processed_review = []
    reviews = []
    tokenized = []
    imp_words = []
    file = open('uploaded_files/ReviewMiner/test1.csv')
    freader = csv.reader(file, quotechar = '"')

    c=0
    for row in freader:
        if (row[1] == 'English' and int(row[2]) <=2):
            reviews.append([row[6]])
            all_reviews.append([row[0],row[2],row[3],row[6].split()])

    stopwords = nltk.corpus.stopwords.words('english')

    for review in reviews:
        print(review)
        tokenized.append(word_tokenize(review[0]))


    for x in tokenized:
        imp_words.append([word for word in x if word.lower()
                          not in stopwords and word.isalpha()])

    print(imp_words)



    criteria = xlrd.open_workbook('uploaded_files/ReviewMiner/Review_Criteria.xlsx',on_demand=True)

    review_line_count=0
    for review_line in imp_words:
        #print(review_line)

        for name in criteria.sheet_names():
            category_total_score = 0
            sheet = criteria.sheet_by_name(name)
            request_count =0
            hit_words_tags = []
            for [category,score] in zip(sheet.col(0),sheet.col(1)):
                in_string = category.value

                for review_word in review_line:

                        if in_string != "":
                            if (name == request and request_count == 0):
                                if in_string in " ".join(review_line):
                                    request_count += 1
                                    hit_words_tags.append(in_string)
                                    category_total_score += score.value
                            else:
                                string_length = len(in_string)
                                if in_string in review_word and in_string[0:string_length] == review_word[0:string_length]:
                                    hit_words_tags.append(review_word)
                                    category_total_score += score.value

            if(name == performance):
                    performance_total = category_total_score
                    performance_tags = hit_words_tags
            elif(name == userinterface):
                    userinterface_total = category_total_score
                    userinterface_tags = hit_words_tags
            elif(name == compatibility):
                    compatibility_total = category_total_score
                    compatibility_tags = hit_words_tags
            elif(name == request):
                    request_total = category_total_score
                    request_tags = hit_words_tags
            elif(name == general):
                    general_total = category_total_score
                    general_tags = hit_words_tags

        if performance_total != 0:
            performance_final_list.append([all_reviews[review_line_count],performance,performance_tags,performance_total])
        if compatibility_total != 0:
            compatibility_final_list.append([all_reviews[review_line_count],compatibility,compatibility_tags,compatibility_total])
        if userinterface_total != 0:
            userinterface_final_list.append([all_reviews[review_line_count],userinterface,userinterface_tags,userinterface_total])
        if request_total != 0:
            request_final_list.append([all_reviews[review_line_count],request,request_tags,request_total])
        if general_total != 0:
            general_final_list.append([all_reviews[review_line_count],general,general_tags,general_total])
        review_line_count += 1

    performance_final_list.sort(key=lambda x: x[2])
    for member in performance_final_list:
        print(member)

    compatibility_final_list.sort(key=lambda x: x[2])
    for member in compatibility_final_list:
        print(member)

    userinterface_final_list.sort(key=lambda x: x[2])
    for member in userinterface_final_list:
        print(member)

    request_final_list.sort(key=lambda x: x[2])
    for member in request_final_list:
        print(member)

    general_final_list.sort(key=lambda x: x[2])
    for member in general_final_list:
        print(member)


    all_processed_review.append(performance_final_list)
    all_processed_review.append(compatibility_final_list)
    all_processed_review.append(userinterface_final_list)
    all_processed_review.append(request_final_list)
    all_processed_review.append(general_final_list)

    return  all_processed_review







