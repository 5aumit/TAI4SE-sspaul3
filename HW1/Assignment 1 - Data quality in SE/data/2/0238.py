import reddit
import tts
import sys
import praw
import os

#TODO: CENSOR CURSE WORDS,tag images that have curse words in them. strip punctuation from comment replies mp3
#TODO: pay for ads :thinking: buy views?
#TODO: sort by top upvotes
#todo: remove the formatting stuff
#todo: redo ducking
#todo quick script to get high upvote replies
#todo: remove hyperlinks

POST_ID = sys.argv[1]
NUM_POSTS = int(sys.argv[2])

reddit_object = praw.Reddit(
    client_id="aAhfCgWHCGOylw",
    client_secret="FLrVvWquolZc4cnKaEhULqzfUYsxQQ",
    user_agent='reddit_to_vid')


print(f"NOW PROCESSING POST ID: {POST_ID}")
comments_from_post,post_title = reddit.get_top_comments_from_id(reddit_object,POST_ID,NUM_POSTS)
tts.comment_to_mp3(post_title,'./quota.txt','titles',0,randomize=True)
n = 1
for comment in comments_from_post:
    tts.comment_to_mp3(comment,"./quota.txt",POST_ID,n,randomize=True)
    n+=1
tts.comment_to_mp3("Oh, you made it to the end? You're a ducking beast! Lets make a deal: Hit like and subscribe and I will provide more humanoid content. Goodbye!","./quota.txt",'duck',1,randomize=True)

