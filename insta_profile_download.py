import instaloader
insta = instaloader.Instaloader()
username = input('Enter Username: ')
print(insta.download_profile(username, profile_pic_only=True))
