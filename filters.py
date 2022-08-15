def get_setting(album, name, default_value, settings):
  return album.meta.get(name, settings.get(name, [default_value]))[0]

def theme_name(album):
  return album.meta.get("theme", "bookshelf")

def static_url(url, album):
  """
  This takes an album and attempts to get a linkable url to a static file.
  """

  url = f"static/{url}"

  # album.name == "." implies this is a root album.
  # since sigal doesn't support walking up the album tree, this theme only supports a single level of nested albums.
  if album.name != ".":
    url = f"../{url}"

  return url

