Hyperspace by HTML5 UP
----------------------
Originally developed by [HTML5 UP](https://html5up.net/hyperspace). Ported to Pelican by [Trinora Software, Ltd.](https://trinora.software). Licensed under the under the Creative Commons Attribution 3.0 license. Please keep all attribution notices in place.

## Theme Features

### Home Page Sections
Any page can be added as a section to the homepage. These sections will appear underneath the articles (if enabled, see `THEME_HOMEPAGE_INCL_ARTICLES`) and before the footer. Add the following metadata for the applicable pages:

* HomePage_Sort: Numeric (actually a string, but intended to be a numeric) value giving the sort order of the section on the page. This only takes effect if more than one page is included as a homepage section.

* HomePage_Style: Class name for CSS styling. See `main.css` rules for `style?` classes. E.g., `style1`, `style1-alt`, `style2`, etc.

### Page Sort in Navigation Menu
Add the key `Menu_Sort` to your page metadata to control the sort order of the page in the navigation menu. This only takes effect if `THEME_MENU_ONLY_MENUITEMS` is False and `DISPLAY_PAGES_ON_MENU` is True and more than one page appears in the menu.

### Article Image
Add the key `Cover` to your article metadata with an image filename as value to have this image appear in article listings as a thumbnail and as a fullscreen background image in the article itself.	

## Theme-specific Settings
The following are settings that alter the behaviour of this theme. These values should be set in your `pelicanconf.py` file.

### THEME_HIDE_ATTRIBUTION
*Boolean, default False*

If set to True, will hide the attribution notice in the footer. Please ensure you meet the licensing requirements as specified in the README.md file before setting this to True!

### THEME_MENU_ONLY_MENUITEMS
*Boolean, default False*

If set to True, will only show links in the `MENUITEMS` configuration setting in the website navigation menu, and will disregard `DISPLAY_PAGES_ON_MENU` and `DISPLAY_CATEGORIES_ON_MENU` settings. If set to False, Pelican's standard menu behaviour will be used.

### THEME_HOMEPAGE_INTRO_PAGE
*Page slug, default unset*

If set to a page slug, the contents of the specified page will be rendered in the intro section on the homepage, overriding the default intro. If unset, set to a blank string, or the page slug is not found, the default intro section will be used. The default intro section shows the site name, site subtitle, and a link to scroll the homepage to the articles section.

### THEME_HOMEPAGE_INCL_ARTICLES
*Boolean, default True*

If set to True, articles will be shown on the homepage. Set to False to not show articles on the homepage.

### THEME_HOMEPAGE_ARTICLES_PAGINATION
*String, default unset*

When articles are shown on the homepage (i.e., `THEME_HOMEPAGE_INCL_ARTICLES` set True) and pagination is required, if this is set to "pagination", the pagination controls will be displayed on the homepage. Any other string will be interpreted as the destination of a "View more articles" link. If unset, pagination will not be shown on the homepage.

### THEME_FOOTER_PAGE
*Page slug, default unset*

If set to a page slug, the contents of the specified page will be rendered in the footer, overriding the default footer. If unset, set to a blank string, or the page slug is not found, the default footer will be used. The default footer shows the `LINKS` and `SOCIAL` link lists.

## Removing Attribution
The Creative Commons Attribution 3.0 license requires that all attribution notices are left in place. The original author has a commercial license offering that allows the attribution notice to be removed. Please see [Pixelarity](https://pixelarity.com/) by the original author and purchase a subscription. Once a commercial license has been purchased, attribution can be removed with the setting `THEME_HIDE_ATTRIBUTION` to True.

## TODO

1. Add support for author images and biographies? 
2. Need to implement `period_archives.html` template.
3. Inline CSS styles to be cleaned up.
4. Some other ugly CSS styles to be prettified.
5. Add a feature to alter theme color scheme from settings?
6. Some of the article listing pages (tags, at least, probably others) need a better layout. 

## Original Readme (from HTML5 UP)
> So I've had the wireframe for this particular design kicking around for some time, but with all
the other interesting (and in some cases, semi-secret) projects I've been working on it took me
a little while to get to actually designing and coding it. Fortunately, things have eased up
enough for me to finaly get around to it, so I'm happy to introduce Hyperspace: a fun, blocky,
one-page design with a lot of color, a bit of animation, and an additional "generic" page template
(because hey, even one-page sites usually need an interior page or two). Hope you dig it :)
>
>Demo images* courtesy of Unsplash, a radtastic collection of CC0 (public domain) images
you can use for pretty much whatever.
>
>(* = not included)
>
>AJ
>aj@lkn.io | @ajlkn


### Credits

    Original HTML Template:
        AJ (aj@lkn.io | @ajlkn)
        https://html5up.net/hyperspace

	Demo Images:
		Unsplash (unsplash.com)

	Icons:
		Font Awesome (fontawesome.io)

	Other:
		jQuery (jquery.com)
		Scrollex (github.com/ajlkn/jquery.scrollex)
		Responsive Tools (github.com/ajlkn/responsive-tools)