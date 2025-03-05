import re

class ImportPatterns:
    def __init__(self):
        self.patterns = {
            # CDN Providers
            'cdnjs': re.compile(r'cdnjs\.cloudflare\.com/ajax/libs/([^/]+)/([\d\.]+)/'),
            'jsdelivr': re.compile(r'cdn\.jsdelivr\.net/npm/([^@]+)@([\d\.]+)/'),
            'googleapis': re.compile(r'ajax\.googleapis\.com/ajax/libs/([^/]+)/([\d\.]+)/'),
            'unpkg': re.compile(r'unpkg\.com/([^@]+)@([\d\.]+)/'),
            'bootstrapcdn': re.compile(r'maxcdn\.bootstrapcdn\.com/bootstrap/([\d\.]+)/'),
            'stackpath': re.compile(r'stackpath\.bootstrapcdn\.com/bootstrap/([\d\.]+)/js/bootstrap\.min\.js'),
            'fontawesome': re.compile(r'cdn\.fontawesome\.com/([\d\.]+)/'),
            'bowercdn': re.compile(r'bowercdn\.net/libs/([^/]+)/([\d\.]+)/'),
            'googlefont': re.compile(r'fonts\.googleapis\.com/css\?family=([^&]+)&'),
            'cdnjs-jquery': re.compile(r'cdnjs\.cloudflare\.com/ajax/libs/jquery/([\d\.]+)/'),

            # Package Managers (e.g., npm, yarn)
            'npm': re.compile(r'node_modules/([^/]+)/([^/]+)/'),
            'yarn': re.compile(r'yarnpkg\.com/package/([^/]+)/([\d\.]+)/'),

            # Static File Paths
            'local': re.compile(r'([^/]+)-([\d\.]+)\.min\.js'),
            'local_folder': re.compile(r'/(?:js|libs|assets)/([^/]+)/([\d\.]+)/[^/]+\.min\.js'),
            'local_cdn': re.compile(r'\/(js|libs|assets)\/([^/]+)\/([\d\.]+)\/'),

            # JavaScript CDN Services
            'cdnjs_compressed': re.compile(r'cdnjs\.cloudflare\.com/ajax/libs/([^/]+)-([\d\.]+)-min\.js'),
            'jsdelivr_compressed': re.compile(r'cdn\.jsdelivr\.net/npm/([^@]+)@([\d\.]+)-min\.js'),

            # Popular JavaScript Libraries
            'jquery': re.compile(r'(https?:\/\/.*?jquery.*?\/)([\d\.]+)\/(jquery(?:\.min)?\.js)'),
            'react': re.compile(r'(https?:\/\/.*?react.*?\/)([\d\.]+)\/(react(?:\.min)?\.js)'),
            'vue': re.compile(r'(https?:\/\/.*?vue.*?\/)([\d\.]+)\/(vue(?:\.min)?\.js)'),
            'angular': re.compile(r'(https?:\/\/.*?angular.*?\/)([\d\.]+)\/(angular(?:\.min)?\.js)'),
            'lodash': re.compile(r'(https?:\/\/.*?lodash.*?\/)([\d\.]+)\/(lodash(?:\.min)?\.js)'),
            'momentjs': re.compile(r'(https?:\/\/.*?moment.*?\/)([\d\.]+)\/(moment(?:\.min)?\.js)'),

            # Custom CDN or Hosting
            'my_cdn': re.compile(r'customcdn\.com/libs/([^/]+)/([\d\.]+)/'),
            'custom_host': re.compile(r'https:\/\/(?:www\.)?mywebsite\.com\/static\/([^/]+)\/([\d\.]+)\/'),

            # Other File Path Variations
            'version_in_url': re.compile(r'\/([^\/]+)\/v([\d\.]+)\/'),
            'hash_in_url': re.compile(r'\/([^\/]+)\/([\da-f]+)\/'),
            'query_param_version': re.compile(r'\/([^\/]+)\/\?version=([\d\.]+)'),

            # File URL Patterns (Various formats)
            'file_path_with_version': re.compile(r'\/([^\/]+)-([\d\.]+)\.js'),
            'minified_with_version': re.compile(r'\/([^\/]+)-([\d\.]+)\.min\.js'),
            'unminified_with_version': re.compile(r'\/([^\/]+)-([\d\.]+)\.js$'),

            # Other known CDN providers (specific libraries)
            'cdnjs_react': re.compile(r'cdnjs\.cloudflare\.com/ajax/libs/react/([\d\.]+)/'),
            'cdnjs_vue': re.compile(r'cdnjs\.cloudflare\.com/ajax/libs/vue/([\d\.]+)/'),
            'cdnjs_angular': re.compile(r'cdnjs\.cloudflare\.com/ajax/libs/angular/([\d\.]+)/'),
            'cdnjs_moment': re.compile(r'cdnjs\.cloudflare\.com/ajax/libs/moment/([\d\.]+)/'),

            # Unknown CDN Patterns (generic)
            'generic_cdn': re.compile(r'https:\/\/.*?\/([^/]+)/([^/]+)\/([\d\.]+)/'),
        }

    def add_pattern(self, name, pattern):
        self.patterns[name] = re.compile(pattern)

    def get_patterns(self):
        return self.patterns