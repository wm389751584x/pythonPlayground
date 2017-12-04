def greet_user(names):
    for name in names:
        msg = "Hello, " + name.title() + "!"
        print(msg)


usernames = ['rice', 'wang']
greet_user(usernames)
