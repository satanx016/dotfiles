# Change the argument to True to still load settings configured via autoconfig.yml
config.load_autoconfig(False)

c.qt.args = ['ignore-gpu-blacklist',
             'disable-gpu-driver-bug-workarounds',
             'enable-native-gpu-memory-buffers',
             'enable-gpu-rasteization',
             'enable-features=VaapiVideoDecoder,VaapiVideoDecodeLinuxGL,VaapiVideoEncoder,UseOzonePlatform'
             'disable-features=UseChromeOSDirectVideoDecoder',
             'canvas-oop-rasterization',
             'enable-zero-copy',
              # 'use-gl=angle',
              # 'use-angle=gl',
             'ozone-platform-hint=wayland',
             'num-raste-threads=4',
             'enable-smooth-scrolling',
             'enable-quic']
c.qt.workarounds.remove_service_workers = True

c.qt.workarounds.disable_accelerated_2d_canvas = 'never'

c.auto_save.session = True

config.set('content.cookies.accept', 'all', 'chrome-devtools://*')

config.set('content.cookies.accept', 'all', 'devtools://*')

config.set('content.headers.accept_language', '', 'https://matchmaker.krunker.io/*')

c.content.headers.user_agent = 'Mozilla/5.0 ({os_info}) AppleWebKit/{webkit_version} (KHTML, like Gecko) {qt_key}/{qt_version} {upstream_browser_key}/{upstream_browser_version} Safari/{webkit_version}'

config.set('content.headers.user_agent', 'Mozilla/5.0 ({os_info}) AppleWebKit/{webkit_version} (KHTML, like Gecko) {upstream_browser_key}/{upstream_browser_version} Safari/{webkit_version}', 'https://web.whatsapp.com/')

config.set('content.headers.user_agent', 'Mozilla/5.0 ({os_info}; rv:90.0) Gecko/20100101 Firefox/90.0', 'https://accounts.google.com/*')

c.content.blocking.enabled = True

c.content.blocking.hosts.lists = ['https://raw.githubusercontent.com/StevenBlack/hosts/master/hosts']

c.content.blocking.method = 'auto'

c.content.blocking.adblock.lists = ['https://easylist.to/easylist/easylist.txt', 'https://easylist.to/easylist/easyprivacy.txt']

c.content.blocking.whitelist = []

config.set('content.images', True, 'chrome-devtools://*')
config.set('content.images', True, 'devtools://*')

c.content.javascript.clipboard = 'access'

config.set('content.javascript.enabled', True, 'chrome-devtools://*')
config.set('content.javascript.enabled', True, 'devtools://*')
config.set('content.javascript.enabled', True, 'chrome://*/*')
config.set('content.javascript.enabled', True, 'qute://*/*')

config.set('content.local_content_can_access_remote_urls', True, 'file:///home/satanx016/.local/share/qutebrowser/userscripts/*')
config.set('content.local_content_can_access_file_urls', False, 'file:///home/satanx016/.local/share/qutebrowser/userscripts/*')

config.set('content.media.audio_capture', True, 'https://www.rev.com')
config.set('content.notifications.enabled', True, 'https://aternos.org')
config.set('content.register_protocol_handler', True, 'https://mail.google.com?extsrc=mailto&url=%25s')

c.editor.command = ['nvim', '-f', '{file}', '-c', 'normal {line}G{column0}l']

c.fileselect.single_file.command = ['foot', '-e', 'ranger', '--choosefile={}']

c.fileselect.multiple_files.command = ['foot', '-e', 'ranger', '--choosefiles={}']

c.fileselect.folder.command = ['foot', '-e', 'ranger', '--choosedir={}']

c.scrolling.smooth = True

c.url.default_page = 'https://alljavi.github.io/tartarus-startpage/'

c.url.open_base_url = True

c.url.searchengines = {'DEFAULT': 'https://google.jp/search?q={}'}

c.url.start_pages = 'https://alljavi.github.io/tartarus-startpage/'

c.colors.messages.warning.fg = 'black'

c.colors.messages.warning.border = '#d47300'

c.colors.webpage.bg = 'black'

c.colors.webpage.preferred_color_scheme = 'dark'

c.colors.webpage.darkmode.enabled = True
c.colors.webpage.darkmode.algorithm = 'lightness-cielab'

c.colors.webpage.darkmode.policy.images = 'never'

c.fonts.default_family = 'Mononoki Nerd Font'

# Bindings for normal mode
config.bind('<Ctrl+Shift+y>', "hint links spawn --detach mpv --ytdl-format='bestvideo[vcodec^=avc1]+bestaudio/best' {hint-url}")
