# requests and urllib library imported
import urllib

import requests

# import termcolor
from termcolor import colored

# For Sentiment Analysis  we import the library TextBlob
from textblob import TextBlob

# to  implement Sentiment Analysis using the TextBlob library
from textblob.sentiments import NaiveBayesAnalyzer

# import json
from wordcloud import WordCloud, STOPWORDS

# import matplotlib
import matplotlib.pyplot as plt

# import clarifai
from clarifai.rest import ClarifaiApp


# Access Token
APP_ACCESS_TOKEN = "1136457803.d18d4d0.190888b83160419fba78fda58aa88c7c"

# Token Owner : ananyagupta.main
# Sandbox users : ['princechauhan3133','ysyuvraj079','cmayankdogra', 'srishtichauhan1196', 'Pl.Instabot']

#  Base URL common for all the Instagram API endpoints
BASE_URL = "https://api.instagram.com/v1/"

#  function to get data of a user
def self_info():
    request_url = (BASE_URL + "users/self/?access_token=%s") % (APP_ACCESS_TOKEN)
    print "GET request url : %s" % (request_url)
    user_info = requests.get(request_url).json()

# function to get the number of followers, posts and people we follow from the data received
    if user_info["meta"]["code"] == 200:
        if len(user_info["data"]):
            print "Username: %s" % (user_info["data"]["username"])
            print "Full Name: %s" % (user_info["data"]["full_name"])
            print "Profile picture: %s" % (user_info["data"]["profile_picture"])
            print "Post: %s" % (user_info["data"]["counts"]["media"])
            print "No. of followers: %s" % (user_info["data"]["counts"]["followed_by"])
            print "No. of people you are following: %s" % (user_info["data"]["counts"]["follows"])
            print "No. of posts: %s" % (user_info["data"]["counts"]["media"])
        else:
            print "User does not exist!"
    else:
        print "INVALID REQUEST!!"
        print "Please check the request"

#  function that returns the user ID of the user
def get_user_id(insta_username):
    request_url = (BASE_URL + "users/search?q=%s&access_token=%s") % (insta_username, APP_ACCESS_TOKEN)
    print "GET request url : %s" % (request_url)
    user_info = requests.get(request_url).json()

# To check if the user we searched for exists or not
    if user_info["meta"]["code"] == 200:
        if len(user_info["data"]):
            return user_info["data"][0]["id"]
        else:
            return None
    else:
        print "INVALID REQUEST!!Please try again"
        exit()

# function that  returns the information of the user
def get_user_info(insta_username):
    user_id = get_user_id(insta_username)
    if user_id == None:
        print "User doesnt' exist!!!"
        exit()
    request_url = (BASE_URL + "users/%s?access_token=%s") % (user_id, APP_ACCESS_TOKEN)
    print "GET request url : %s" % (request_url)
    user_info = requests.get(request_url).json()

# fetching the number of followers, the number of people user follows, and the number of posts
    if user_info["meta"]["code"] == 200:
        if len(user_info["data"]):
            print "Username: %s" % (user_info["data"]["username"])
            print "Full Name: %s" % (user_info["data"]["full_name"])
            print "Profile picture: %s" % (user_info["data"]["profile_picture"])
            print "Post: %s" % (user_info["data"]['counts']["media"])
            print "No. of followers: %s" % (user_info["data"]["counts"]["followed_by"])
            print "No. of people you are following: %s" % (user_info["data"]["counts"]["follows"])
            print "No. of posts: %s" % (user_info["data"]["counts"]["media"])
        else:
            print "There is no data for this particular user!!!"
    else:
        print "INVALID REQUEST!!!Please try again"

 #  function that returns the image that we have recently posted on Instagram
def get_own_post():
            request_url = (BASE_URL + "users/self/media/recent/?access_token=%s") % (APP_ACCESS_TOKEN)
            print "GET request url : %s" % (request_url)
            own_media = requests.get(request_url).json()

# check for the status code of the request
            if own_media["meta"]["code"] == 200:
                if len(own_media["data"]):

 # accessing  the image id
                    image_name = own_media["data"][0]["id"] + ".jpeg"
                    image_url = own_media["data"][0]["images"]["standard_resolution"]["url"]
                    urllib.urlretrieve(image_url, image_name)

# Downloading our own post
                    print "Your image has been downloaded!"
                else:
                    print "Post does not exist!"
            else:
                print "Status code other than 200 received!"

# function that  returns the ID of the most recent post of the user
def get_user_post(insta_username):

# function to get the corresponding user ID of the user
            user_id = get_user_id(insta_username)
            if user_id == None:
                print "User does not exist!"
                exit()
            request_url = (BASE_URL + "users/%s/media/recent/?access_token=%s") % (user_id, APP_ACCESS_TOKEN)
            print "GET request url : %s "% (request_url)
            user_media = requests.get(request_url).json()

            if user_media["meta"]["code"] == 200:
                if len(user_media["data"]):
                    image_name = user_media["data"][0]["id"] + ".jpeg"
                    image_url = user_media["data"][0]["images"]["standard_resolution"]["url"]
                    urllib.urlretrieve(image_url, image_name)

# Downloading another user's post
                    print "Your image has been downloaded!"
                else:
                    print "Post does not exist!"
            else:
                print "Status code other than 200 received!"



#  function that returns the video that we have recently posted on Instagram
def get_own_video():
    request_url = (BASE_URL + "users/self/media/recent/?access_token=%s") % (APP_ACCESS_TOKEN)
    print "GET request url : %s" % (request_url)
    own_media = requests.get(request_url).json()

    # check for the status code of the request
    if own_media["meta"]["code"] == 200:
        if len(own_media["data"]):

            # accessing  the image id
            video_name = own_media["data"][0]["id"] + ".mp4"
            video_url = own_media["data"][0]["videos"]["standard_resolution"]["url"]
            urllib.urlretrieve(video_url, video_name)

            # Downloading our own post
            print "Your video has been downloaded!"
        else:
            print "Post does not exist!"
    else:
        print "Status code other than 200 received!"


#  function that returns the video that user have recently posted on Instagram
def get_user_video(insta_username):
    # function to get the corresponding user ID of the user
    user_id = get_user_id(insta_username)
    if user_id == None:
        print "User does not exist!"
        exit()
    request_url = (BASE_URL + "users/%s/media/recent/?access_token=%s") % (user_id, APP_ACCESS_TOKEN)
    print "GET request url : %s " % (request_url)
    user_media = requests.get(request_url).json()

    if user_media["meta"]["code"] == 200:
        if len(user_media["data"]):
            video_name = user_media["data"][0]["id"] + ".mp4"
            video_url = user_media["data"][0]["videos"]["standard_resolution"]["url"]
            urllib.urlretrieve(video_url, video_name)

            # Downloading another user's post
            print "Your video has been downloaded!"
        else:
            print "Post does not exist!"
    else:
        print "Status code other than 200 received!"

def get_post_id(insta_username):
    user_id = get_user_id(insta_username)
    if user_id == None:
        print 'User does not exist!'
        exit()
    request_url = (BASE_URL + 'users/%s/media/recent/?access_token=%s') % (user_id, APP_ACCESS_TOKEN)
    print 'GET request url : %s' % (request_url)
    user_media = requests.get(request_url).json()

    if user_media["meta"]["code"] == 200:
        if len(user_media["data"]):
            return user_media["data"][0]["id"]
        else:
            print "There is no recent post of the user!"
            exit()
    else:
        print "Status code other than 200 received! "
        exit()


#  function that likes the most recent post of that user
def like_a_post(insta_username):

# function to get the ID of the post to be liked
    media_id = get_post_id(insta_username)
    request_url = (BASE_URL + 'media/%s/likes') % (media_id)
    payload = {"access_token": APP_ACCESS_TOKEN}
    print 'POST request url : %s' % (request_url)
    post_a_like = requests.post(request_url, payload).json()
    if post_a_like["meta"]["code"] == 200:
        print "Your like was successful!"
    else:
        print "Your like was unsuccessful. Please try again!!"

# function to get list of the users who have liked the post
def get_like_list(insta_username):
  mid = get_post_id(insta_username)
  request_url = (BASE_URL + 'media/%s/likes?access_token=%s') % (mid, APP_ACCESS_TOKEN)
  likes_lst = requests.get(request_url).json()
  print likes_lst


# function that makes a new comment on the most recent post of the user
def post_a_comment(insta_username):

# function to get ID of the post to which we want to make a new comment
    media_id = get_post_id(insta_username)
    comment_text = raw_input("Your comment: ")
    payload = {"access_token": APP_ACCESS_TOKEN, "text" : comment_text}
    request_url = (BASE_URL + 'media/%s/comments') % (media_id)
    print 'POST request url : %s' % (request_url)

    make_comment = requests.post(request_url, payload).json()

    if make_comment['meta']['code'] == 200:
        print "Your comment was successfully added to the post!"
    else:
        print "Unable to add comment.Please try again!"

# function to get list of comments on the recent post of the user
def get_comment_list(insta_username):
  media_id = get_post_id(insta_username)
  request_url = (BASE_URL + 'media/%s/comments?access_token=%s') % (media_id, APP_ACCESS_TOKEN)
  comment_list = requests.get(request_url).json()

  if comment_list['meta']['code'] == 200:
    if len(comment_list['data']):
      for i in range(0, len(comment_list['data'])):
        print comment_list['data'][i]['text']
    else:
      print "There are no recent post of the user!!"
      exit()
  else:
    print "Incorrect choice!!"
    exit()

# function that deletes all negative comments from an instagram post using NLP
def delete_negative_comment(insta_username):
    media_id = get_post_id(insta_username)
    request_url = (BASE_URL + 'media/%s/comments/?access_token=%s') % (media_id, APP_ACCESS_TOKEN)
    print 'GET request url : %s' % (request_url)
    comment_info = requests.get(request_url).json()

    if comment_info['meta']['code'] == 200:
        if len(comment_info['data']):
            #Here's a naive implementation of how to delete the negative comments :)
            for x in range(0, len(comment_info['data'])):
                comment_id = comment_info['data'][x]['id']
                comment_text = comment_info['data'][x]['text']
                blob = TextBlob(comment_text, analyzer=NaiveBayesAnalyzer())
                if (blob.sentiment.p_neg > blob.sentiment.p_pos):
                    print 'Negative comment : %s' % (comment_text)
                    delete_url = (BASE_URL + 'media/%s/comments/%s/?access_token=%s') % (media_id, comment_id, APP_ACCESS_TOKEN)
                    print 'DELETE request url : %s' % (delete_url)
                    delete_info = requests.delete(delete_url).json()

                    if delete_info['meta']['code'] == 200:
                        print "Your comment was successfully deleted!\n"
                    else:
                        print "Unable to delete comment!Please try again"
                else:
                    print "Positive comment : %s\n" % (comment_text)
        else:
            print "There are no existing comments on the post!!"
    else:
        print "INVALID choice!!"


ar = []
my_dictionary = {
    'imageurl': None,
    'words': ''

}
user_lis = ['princechauhan3133', 'ysyuvraj079', 'srishtichauhan1196','Pl.Instabot']

#function to show the subtrend of a wedding and plot through wordcloud
#objective to show subtrend of any activities or event and plot through word cloud
#defining clarifaiApp with generated key
app = ClarifaiApp(api_key='b40b2d24a82b4cab89ec2ec4af04874a')

# to get the general model
model = app.models.get('weddings-v1.0')
for user in user_lis:
 def get_users_post(user):
        user_id = get_user_id(user)
        if user_id == None:
            print 'User does not exist!'
            exit()
        request_url = (BASE_URL + 'users/%s/media/recent/?access_token=%s') % (user_id, APP_ACCESS_TOKEN)
        print 'GET request url : %s' % (request_url)
        user_media = requests.get(request_url).json()

        if user_media['meta']['code'] == 200:
            if len(user_media['data']):
                image_name = user_media['data'][0]['id'] + '.jpeg'
                image_url = user_media['data'][0]['images']['standard_resolution']['url']
                model = app.models.get('travel-v1.0')
                response = model.predict_by_url(url=image_url)

# data fetched through concepts and stored in response
                for x in response['outputs'][0]['data']['concepts']:

# print name stored in value
                    print x['name'], x['value']

# if value of x greater than .7
                    if x['value'] > .7:

# string show the value of x in name
                        strr = x['name']

# using temp variable to fetch words stored in dictionary
                        temp = my_dictionary['words']
                        temp = temp + ' ' + str(strr)
                        my_dictionary['words'] = temp

# string stored in a dictionary as a words
                String = my_dictionary['words']
                print
                wordcloud = WordCloud(stopwords=STOPWORDS, background_color='white', width=1200, height=1000).generate(
                    String)
                plt.imshow(wordcloud)
                plt.axis('off')
                plt.show()
                urllib.urlretrieve(image_url, image_name)
            else:
                print "error"

        else:
            print "error"


 def start_bot():
    while True:
        print '\n'
        print "Hey! Welcome all to MyInstaBot!"
        print "Menu options:"
        print "1.Get your own details\n"
        print "2.Get details of a user by username\n"
        print "3.Get your own recent post\n"
        print "4.Get the recent post of a user by username\n"
        print "5.Get your own recent video\n"
        print "6.Get the recent video of a user by username\n"
        print "7.Like the recent post of a user\n"
        print "8.Get like list\n"
        print "9.Make a comment on the recent post of a user\n"
        print "10.Get list comment on recent post\n"
        print "11.Delete negative comments from the recent post of a user\n"
        print "12.Show Subtrends of wedding\n"
        print "13.Exit"

        choice=raw_input(colored("Enter you choice: ",'green'))
        if choice=="1":
          self_info()
        elif choice=="2":
            insta_username = raw_input(colored("Enter the username of the user: ",'red'))
            get_user_info(insta_username)
        elif choice == "3":
            get_own_post()
        elif choice == "4":
            insta_username = raw_input(colored("Enter the username of the user: ",'grey'))
            get_user_post(insta_username)
        elif choice == "5":
            get_own_video()
        elif choice == "6":
            insta_username = raw_input(colored("Enter the username of the user: ",'grey'))
            get_user_video(insta_username)
        elif choice == "7":
            insta_username = raw_input(colored("Enter the username of the user: ",'yellow'))
            like_a_post(insta_username)
        elif choice == "8":
            insta_username = raw_input(colored("Enter username of the user: ",'magenta'))
            get_like_list(insta_username)
        elif choice == "9":
            insta_username = raw_input(colored("Enter the username of the user: ",'grey'))
            post_a_comment(insta_username)
        elif choice == "10":
            insta_username = raw_input(colored("Enter the username of the user: ",'red'))
            get_comment_list(insta_username)
        elif choice == "11":
            insta_username = raw_input(colored("Enter the username of the user: ",'magenta'))
            delete_negative_comment(insta_username)
        elif choice=="12":
            exit()
        else:
            print "Incorrect choice"
start_bot()