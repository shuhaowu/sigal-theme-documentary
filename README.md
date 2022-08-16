Documentary sigal theme
=======================

A [sigal](https://sigal.saimon.org/) theme based on [pure.css](https://purecss.io/) and [lightGallery](https://www.lightgalleryjs.com/). It supports multiple galleries, each with different subthemes. Currently, there are two subthemes to choose from:

- `bookshelf` for a grid of photos
- `photojournal` for rows of photos on the left and text to the right

See [a demo here](https://shuhaowu.github.io/sigal-theme-documentary/).

Custom configurations
---------------------

Contrary to how sigal normally specifies metadata for albums, this theme expects there to be an `albums` variable in `sigal.conf.py` in the following format:

```python
albums = {
  # album name must match the folder name
  "album_name": {
    "title": "Title",
    "description": "<p>This is the description html.</p>",

    # Could be photojournal or bookshelf
    "theme": "bookshelf",

    # The height of the photocard <img>, which are the grid of photos in bookshelf
    # subtheme and the album index page (album_list.html)
    "photocardheight": "250px",

    # The object-fit setting for the photocard <img>
    # See https://developer.mozilla.org/en-US/docs/Web/CSS/object-fit
    "photocardfit": "cover",

    # The height of the photorow <img>, which are the rows of photo and text
    # in the photojournal subtheme.
    "photorowheight": "400px",

    # The object-fit setting for the photorow <img>
    # See https://developer.mozilla.org/en-US/docs/Web/CSS/object-fit
    "photorowfit": "cover",

    # The grid setting for a small screen. See purecss for details
    # https://purecss.io/grids/
    "photocardsmfrac": "1-2"

    # The grid setting for a small screen. See purecss for details
    # https://purecss.io/grids/
    "photocardmdfrac": "1-3"

    # The grid setting for a small screen. See purecss for details
    # https://purecss.io/grids/
    "photocardlgfrac": "1-4"
  },
  }
}
```

The reason this is needed is because of https://github.com/saimn/sigal/issues/478. Once you put the album information in one place, you might as well put it all in the same place (which frankly I almost like better than the index.md).

Limitations
-----------

- The theme doesn't support author attribute.
- Only supports 1 sublevel of albums. Nested albums are not supported!

Hacks
-----

This theme abuses sigal in the following ways:

- Instead of using `index.md` to specify the album title, metadata, and description, the theme expects the album information to be available in a variable called `albums` in the `sigal.conf.py` file.
- Settings are inherited, through hacks. This is done via a Jinja2 filter, which then requires the `album` and `settings` object to be passed to it in weird and hacky ways.
