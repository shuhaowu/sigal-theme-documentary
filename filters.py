import markdown

def get_setting(album, name, default_value, settings):
  # Attempt to find a global default
  value = settings.get(name, [default_value])[0]

  # Attempt to find a per-album default, by in the albums variable as specified in sigal.conf.py
  # This overrides the global default.
  global_album_settings = settings.get("albums", {}).get(album.name, {})
  value = global_album_settings.get(name, value)

  # Finally, look in index.md for each album, which overrides all of the above.
  return album.meta.get(name, value)

def album_meta(album, name, settings):
  return settings.get("albums", {}).get(album.name, {}).get(name)

def to_markdown(s):
  return markdown.markdown(s)

def previous_link(album, settings):
  keys = list(settings.get("albums", {}).keys())
  idx = keys.index(album.name)
  if idx == 0:
    return "&#8592; Previous album"

  return '<a href="../{}">&#8592; Previous album</a>'.format(keys[idx - 1])

def next_link(album, settings):
  keys = list(settings.get("albums", {}).keys())
  idx = keys.index(album.name)
  if idx >= len(settings.get("albums", {})) - 1:
    return "Next album &#8594;"

  return '<a href="../{}">Next album &#8594;</a>'.format(keys[idx + 1])

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
