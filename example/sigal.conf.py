title = "Documentary Theme Example"
source = "gallery"
theme = ".."

# Use originals in gallery (default: False). If True, this will bypass all
# processing steps (resize, auto-orient, recompress, and any plugin-specific
# step).
# Originals will be symlinked if orig_link = True, else they will be copied.
# use_orig = True

img_format = "JPEG"
img_size = (3000, 2000)

jpg_options = {
  'quality': 90,
  'optimize': True,
  'progressive': True,
}

make_thumbs = True

_thumb_multiplier = 2
thumb_size = (450 * _thumb_multiplier, 300 * _thumb_multiplier)
thumb_fit = False

plugins = [
  "sigal.plugins.zip_gallery",
  # https://github.com/saimn/sigal/issues/474
  "PIL.PngImagePlugin",
  "PIL.JpegImagePlugin",
]

zip_gallery = "{album.name}.zip"
# zip_media_format = "orig"

albums = {
  "photojournal": {
    "title": "Photojournal demo gallery",
    "description": "<p>This is the description text.</p>",
    "theme": "photojournal",
    "photorowheight": "400px",
  },

  "bookshelf": {
    "title": "Bookshelf demo gallery",
    "description": "<p>This is the description text.</p>",
    "theme": "bookshelf",
  },
}