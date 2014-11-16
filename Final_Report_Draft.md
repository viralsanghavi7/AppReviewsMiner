#Mobile Application Reviews Mining
-----
##Introduction

With increasing competition in mobile marketplace, developers are working on getting their application better and serve it's users. They can improve on their apps by using the wide source of information they get in terms of user reviews about their application. But main problem for developers is to filter out helpful & relevant reviews from the large pool of user reviews. With careful analysis of each review, we can output the most constructive and helpful reviews to aid developer in improving the quality of their product. This project will help them in working on the different characteristics of their application based on whatever feedback is given by user for their application.

##Problem of Mobile Developers and our solution

Every application in mobile application store gets hundreds of reviews. Some of them are really good praising the application. But some of them are low rated reviews which signifies any improvements needed in this application or any suggestions from the user that they would like to have improved. Sometimes developer may encounter with very short and irrelevant reviews. As the number of reviews increases, it becomes difficult for developer to sort out the most helpful reviews from this large corpus. Their main task is to filter out the most helpful and informative reviews and categorize them according to different areas of improvements like performance, stability, compatibility with multiple devices, user interface etc. Objective of this application is to assist the mobile app developers in categorizing the reviews into different areas of improvements. This will expedite the process of getting informative feedbacks from application users and to work on quality improvement of their application.

##How it works?
Every android application developer gets their review data in csv (comma separated value) format from google. If you are an android mobile developer then you can get your review data by following the steps give at following link.
- [Get the reviews data from play store for your android app]

Our project is a web application which allows the developer to upload their csv file on the site.
![Home](https://github.ncsu.edu/CSC510-Fall2014/Technical-AppReviews/raw/master/MobileAppReviews/ReviewMiner/static/Images/HomePage.jpg)

Then we have defined various criteria for mobile applications such as Performance, User Interface, Compatibility, Request by User, General improvements. When you click on `upload` button on the home page, it will show you the reviews which are most helpful partitioned as per the criteria. 
![Output](https://github.ncsu.edu/CSC510-Fall2014/Technical-AppReviews/raw/master/MobileAppReviews/ReviewMiner/static/Images/Working.gif)



This application will parse each review to perform natural language processing on each of the review text and it tries to find out the whether the review is related to performance, compatibility or any other criteria.

>For example, If a review says `‘It is unplayable game. Hanging on my Google Nexus.’` This type of review is helpful for mobile developer. It will allow developer to understand what the problem is and decide upon the appropriate action to take to improve. Like in this review, user is mentioning that the application is not compatible with his/her cell Google Nexus. Our application will categorize this review in the category of Performance and Compatibility based on the text of review and natural language processing on that text. 

For detailed understanding of the application working please refer following video: 
[![Home](https://github.ncsu.edu/CSC510-Fall2014/Technical-AppReviews/raw/master/MobileAppReviews/ReviewMiner/static/Images/HomePage.jpg)](http://youtu.be/o0jNeUcssU0)

##Features

* This application allows developer to put **filter on the rating of reviews**. Suppose developer just want to consider reviews which got the rating below 3 or below 2. Then our application will give the option to select such filter and then we will parse only those reviews which are below rating 3 or 2 based on whatever the user has selected.
* This application also allows user to see the **reviews by criteria**. Suppose, the developer just want to see reviews which are related to compatibility of the application, then he can select the compatibility tabs on the side to choose reviews related to compatibility. Developer can click on ‘All Reviews’ to select the reviews which falls in all the criteria.
* This application also displays the **statistics in graphical form** based on how these reviews are categorized. This will help developers to focus on particular area of improvement for their application.

##Technologies and architecture behind it
No doubt that we got to learn lot of new technologies and implement them. 
* Our application is developed completely in *[Python]*. Since Python is very flexible, easy to use and very powerful language, we decided to try our hands on this language through this project.
* It uses *[Python Natural Language Toolkit] (NLTK)* to perform the natural language processing of the review text. Python NLTK has rich set functionality and documentation available, which allows the text parsing in easy and effective manner.
* Web application is developed in *[Django framework]* for Python which is very again useful and easy to manage framework.
* We are using **strategy architecture pattern** behind this code logic. It basically identifies various improvement areas and applies respective strategy to parse the review text for that particular improvement area.
* We are using *[bootstrap]* framework to display the web page. 


##Limitations and Future scope
* Currently this application works only for the CSVs given in the prescribed format as mentioned above. In future, we can try to accommodate the reviews in the CSV which might be in different formats.
* Support for the mobile marketplace can be increased from Google play store to Apple App store or windows application store etc.
* This application just provides support for processing of reviews which are written in English language. Python NLTK also provides support for other languages as well and we can incorporate them in subsequent releases.
* The list of criteria based on which reviews are parsed is currently fixed.  In future scope, we can allow user to participate in defining the criteria with which he wants to detect reviews related to particular area of improvement.
* Currently filtered reviews are just shown to user. In future we can have status for each filtered review. For example when user is working on particular review, he should be able to mark it as ‘In Progress’. And further when user is done with working, user should be able to mark that review as ‘fixed’. So that it won’t show up in the list again.
* We can provide the option of extracting the output which we are getting on the web application and should allow the user to save the results so as to refer the output again when offline.

##References
Along with our professor [Dr. Christopher J Parnin], We would like to thank all the resources from where we got this inspiration to work on such a useful project.
* [Why People Hate Your App — Making Sense of User Feedback in a Mobile App Store]
KDD’13, August 11–14, 2013, Chicago, Illinois, USA
* [AR-Miner: Mining Informative Reviews for Developers from Mobile App Marketplace]
ICSE ’14, May 31-June 7, 2014, Hyderabad, India

[Get the reviews data from play store for your android app]:(https://support.google.com/googleplay/android-developer/answer/138230?hl=en)
[Python]:(https://www.python.org/)
[Python Natural Language Toolkit]:(http://www.nltk.org/)
[Django framework]:(https://www.djangoproject.com/)
[bootstrap]:(http://getbootstrap.com/)
[Dr. Christopher J Parnin]:(http://www.chrisparnin.me/)
[Why People Hate Your App — Making Sense of User Feedback in a Mobile App Store]:(http://www.cs.cmu.edu/~leili/pubs/fu-kdd2013-wiscom.pdf)
[AR-Miner: Mining Informative Reviews for Developers from Mobile App Marketplace]:(http://www.cais.ntu.edu.sg/~nchen1/AR-Miner/icse14-preprint.pdf)
