config.load_autoconfig(False)

c.qt.args = ['enable-unsafe-webgpu', 'disable-gpu-driver-bug-workarounds', 'enable-native-gpu-memory-buffers', 'enable-gpu-rasterization', 'enable-features=RawDraw,VaapiVideoDecoder,VaapiVideoDecodeLinuxGL,VaapiVideoEncoder', 'enable-zero-copy', 'ozone-platform-hint=wayland', 'enable-smooth-scrolling', 'enable-quic']
c.qt.workarounds.disable_accelerated_2d_canvas = 'never'

c.auto_save.session = True
c.scrolling.smooth = True
c.content.javascript.clipboard = 'access-paste'

c.editor.command = ['foot', '-c', '.config/foot/footNoPadding.ini', 'nvim', '-f', '{file}', '-c', 'normal {line}G{column0}l']
c.fileselect.single_file.command = ['foot', '-c', '-e', 'ranger', '--choosefile={}']
c.fileselect.multiple_files.command = ['foot', '-c', '-e', 'ranger', '--choosefiles={}']
c.fileselect.folder.command = ['foot', '-c', '-e', 'ranger', '--choosedir={}']


c.url.default_page = 'https://alljavi.github.io/tartarus-startpage/'
c.url.open_base_url = True
c.url.searchengines = {'DEFAULT': 'https://google.jp/search?q={}'}
c.url.start_pages = 'https://alljavi.github.io/tartarus-startpage/'

c.colors.webpage.bg = 'black'
c.colors.webpage.preferred_color_scheme = 'dark'
c.colors.webpage.darkmode.enabled = True
c.colors.webpage.darkmode.algorithm = 'lightness-cielab'
c.colors.webpage.darkmode.policy.images = 'never'

config.bind('<Ctrl+Shift+y>', "hint links spawn --detach mpv --ytdl-format='bestvideo[vcodec^=avc1]+bestaudio/best' {hint-url}")
