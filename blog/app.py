blogs = dict() #blog_name: Blog Object
MENU_PROMPT = 'Enter "c" to crreate the blog, "l" to list blogs, "r" to read one, "p" to create a post and "q" to quit. '

def menu():
    """
    Show the user the available blogs
    Let the user make the choice
    Do something with that choice
    Eventually exit
    """
    print_blogs()
    selection = input(MENU_PROMPT)



def print_blogs():
    """
    Print the available blogs
    """
    print('blogs')

    for key,value in blogs.items():
        print(f'{value}')
