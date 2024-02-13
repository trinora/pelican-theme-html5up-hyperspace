AUTHOR = 'Trinora Software, Ltd.'
SITENAME = 'Example Site'
SITEURL = ""

PATH = "content"
TIMEZONE = 'America/Edmonton'
DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ("Pelican", "https://getpelican.com/"),
    ("Python.org", "https://www.python.org/"),
    ("Jinja2", "https://palletsprojects.com/p/jinja/"),
    ("You can modify those links in your config file", "#"),
)

# Social widget
SOCIAL = (
    ("You can add links in your config file", "#"),
    ("Another social link", "#"),
)

DEFAULT_PAGINATION = 5
# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

BIND = "0.0.0.0"


# The following values are set for the purposes of this example site.

SITESUBTITLE = "This website demonstrates a custom theme for Pelican"
THEME = '..'
AUTHORS_SAVE_AS = 'authors.html'
CATEGORIES_SAVE_AS = 'categories.html'
TAGS_SAVE_AS = 'tags.html'
PAGINATED_TEMPLATES = {
    'index': 1,      # set to 1 so that only the "template info" article appears
    'tag': None, 'category': None, 'author': None
}