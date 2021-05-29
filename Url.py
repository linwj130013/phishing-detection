import requests

class Url:
    def __init__(self, url=""):
        self.url = url
        self.count = dict()

        # separation of url
        self.domain = ""
        self.directory = ""
        self.file = ""
        self.params = ""

        self.split_url()

        # 101 attributes
        self.count_freq(self.url)
        self.qty_dot_url = self.get_freq('.')
        self.qty_hyphen_url = self.get_freq('-')
        self.qty_underline_url = self.get_freq('_')
        self.qty_slash_url = self.get_freq('/')
        self.qty_questionmark_url = self.get_freq('?')
        self.qty_equal_url = self.get_freq('=')
        self.qty_at_url = self.get_freq('@')
        self.qty_and_url = self.get_freq('&')
        self.qty_exclamation_url = self.get_freq('!')
        self.qty_space_url = self.get_freq(' ')
        self.qty_tilde_url = self.get_freq('~')
        self.qty_comma_url = self.get_freq(',')
        self.qty_plus_url = self.get_freq('+')
        self.qty_asterisk_url = self.get_freq('*')
        self.qty_hashtag_url = self.get_freq('#')
        self.qty_dollar_url = self.get_freq('$')
        self.qty_percent_url = self.get_freq('%')
        self.qty_tld_url = 0
        self.length_url = 0

        self.count_freq(self.domain)
        self.qty_dot_domain = self.get_freq('.')
        self.qty_hyphen_domain = self.get_freq('-')
        self.qty_underline_domain = self.get_freq('_')
        self.qty_slash_domain = self.get_freq('/')
        self.qty_questionmark_domain = self.get_freq('?')
        self.qty_equal_domain = self.get_freq('=')
        self.qty_at_domain = self.get_freq('@')
        self.qty_and_domain = self.get_freq('&')
        self.qty_exclamation_domain = self.get_freq('!')
        self.qty_space_domain = self.get_freq(' ')
        self.qty_tilde_domain = self.get_freq('~')
        self.qty_comma_domain = self.get_freq(',')
        self.qty_plus_domain = self.get_freq('+')
        self.qty_asterisk_domain = self.get_freq('*')
        self.qty_hashtag_domain = self.get_freq('#')
        self.qty_dollar_domain = self.get_freq('$')
        self.qty_percent_domain = self.get_freq('%')
        self.qty_vowels_domain = 0
        self.domain_length = 0
        self.domain_in_ip = 0
        self.server_client_domain = 0

        self.count_freq(self.directory)
        self.qty_dot_directory = self.get_freq('.')
        self.qty_hyphen_directory = self.get_freq('-')
        self.qty_underline_directory = self.get_freq('_')
        self.qty_slash_directory = self.get_freq('/')
        self.qty_questionmark_directory = self.get_freq('?')
        self.qty_equal_directory = self.get_freq('=')
        self.qty_at_directory = self.get_freq('@')
        self.qty_and_directory = self.get_freq('&')
        self.qty_exclamation_directory = self.get_freq('!')
        self.qty_space_directory = self.get_freq(' ')
        self.qty_tilde_directory = self.get_freq('~')
        self.qty_comma_directory = self.get_freq(',')
        self.qty_plus_directory = self.get_freq('+')
        self.qty_asterisk_directory = self.get_freq('*')
        self.qty_hashtag_directory = self.get_freq('#')
        self.qty_dollar_directory = self.get_freq('$')
        self.qty_percent_directory = self.get_freq('%')
        self.directory_length = 0

        self.count_freq(self.file)
        self.qty_dot_file = self.get_freq('.')
        self.qty_hyphen_file = self.get_freq('-')
        self.qty_underline_file = self.get_freq('_')
        self.qty_slash_file = self.get_freq('/')
        self.qty_questionmark_file = self.get_freq('?')
        self.qty_equal_file = self.get_freq('=')
        self.qty_at_file = self.get_freq('@')
        self.qty_and_file = self.get_freq('&')
        self.qty_exclamation_file = self.get_freq('!')
        self.qty_space_file = self.get_freq(' ')
        self.qty_tilde_file = self.get_freq('~')
        self.qty_comma_file = self.get_freq(',')
        self.qty_plus_file = self.get_freq('+')
        self.qty_asterisk_file = self.get_freq('*')
        self.qty_hashtag_file = self.get_freq('#')
        self.qty_dollar_file = self.get_freq('$')
        self.qty_percent_file = self.get_freq('%')
        self.file_length = 0

        self.count_freq(self.params)
        self.qty_dot_params = self.get_freq('.')
        self.qty_hyphen_params = self.get_freq('-')
        self.qty_underline_params = self.get_freq('_')
        self.qty_slash_params = self.get_freq('/')
        self.qty_questionmark_params = self.get_freq('?')
        self.qty_equal_params = self.get_freq('=')
        self.qty_at_params = self.get_freq('@')
        self.qty_and_params = self.get_freq('&')
        self.qty_exclamation_params = self.get_freq('!')
        self.qty_space_params = self.get_freq(' ')
        self.qty_tilde_params = self.get_freq('~')
        self.qty_comma_params = self.get_freq(',')
        self.qty_plus_params = self.get_freq('+')
        self.qty_asterisk_params = self.get_freq('*')
        self.qty_hashtag_params = self.get_freq('#')
        self.qty_dollar_params = self.get_freq('$')
        self.qty_percent_params = self.get_freq('%')
        self.params_length = 0
        self.tld_present_params = 0
        self.qty_params = 0

        # others
        self.email_in_url = 0
        self.time_response = self.get_resp_time(self.url)
        self.domain_spf = 0
        self.asn_ip = 0
        self.time_domain_activation = 0
        self.time_domain_expiration = 0
        self.qty_ip_resolved = 0
        self.qty_nameservers = 0
        self.qty_mx_servers = 0
        self.ttl_hostname = 0
        self.tls_ssl_certificate = 0
        self.qty_redirects = 0
        self.url_google_index = 0
        self.domain_google_index = 0
        self.url_shortened = 0

    def split_url(self):
        self.domain = self.url.split('/')[2]
        self.directory = self.url.split('/')[3]
        self.file = self.url.split('/')[4].split('?')[0]
        self.params = self.url.split('?')[-1]

    def count_freq(self, url):
        for i in url:
            if i in self.count:
                self.count[i] += 1
            else:
                self.count[i] = 1

    def get_freq(self, symbol):
        if symbol in self.count:
            return self.count[symbol]
        else:
            return 0
    
    def get_resp_time(self, url):
        respTime = requests.get(url)
        return respTime.elapsed.microseconds/1000/1000

url = "https://domain.com/dir/index.php?q=example"
Url(url)
