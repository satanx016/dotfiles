config.load_autoconfig(False)

# General
c.editor.command = ['foot', '-c', '.config/foot/footNoPadding.ini', 'nvim', '-f', '{file}', '-c', 'normal {line}G{column0}l']
c.downloads.position = 'bottom'
c.statusbar.show = "in-mode"
c.completion.height = "33%"
c.auto_save.session = True
c.scrolling.smooth = True

# Content
c.content.pdfjs = True
c.content.autoplay = False
c.content.javascript.clipboard = 'access-paste'

# File handling
c.fileselect.handler = 'external'
c.fileselect.single_file.command = ['foot', '-e', 'yazi', '--chooser-file={}']
c.fileselect.multiple_files.command = ['foot', '-e', 'yazi', '--chooser-file={}']
c.fileselect.folder.command = ['foot', '-e', 'yazi', '--cwd-file={}']

# Search engines
c.url.searchengines = {
    "DEFAULT": "https://duckduckgo.com/?q={}",
    "aw": "https://wiki.archlinux.org/?search={}",
    "gg": "https://google.com/search?q={}",
    "gh": "https://github.com/search?q={}",
    "gho": "https://github.com/{}",
    "rd": "https://reddit.com/search/?q={}",
    "rds": "https://reddit.com/r/{}",
    "so": "https://stackoverflow.com/search?q={}",
    "sp": "https://open.spotify.com/search/{}",
    "xx": "https://x.com/search?q={}",
    "ud": "https://urbandictionary.com/define.php?term={}",
    "wk": "https://en.wikipedia.org/wiki/{}",
    "yt": "https://youtube.com/results?search_query={}",
}
# Dark mode
c.colors.webpage.darkmode.enabled = True
c.colors.webpage.preferred_color_scheme = 'dark'
c.colors.webpage.bg = 'black'
c.colors.webpage.darkmode.algorithm = 'lightness-cielab'
c.colors.webpage.darkmode.policy.images = 'never'

# Keybinds
config.bind('<Ctrl+Shift+y>', "hint links spawn --detach mpv {hint-url}")

# Flags & Optimizations
c.qt.args = [
    'enable-features=VaapiVideoDecoder,VaapiVideoDecodeLinuxGL,VaapiVideoEncoder',
    'disable-site-isolation-trials',
    #'enable-unsafe-webgpu',
    #'disable-gpu-driver-bug-workarounds',
    'enable-native-gpu-memory-buffers',
    'enable-gpu-rasterization',
    'enable-zero-copy',
    'enable-smooth-scrolling',
    'enable-quic'
]
c.qt.workarounds.disable_accelerated_2d_canvas = 'never'
