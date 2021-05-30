import requests
from pprint import pprint
from cymruwhois import Client
import socket
import whois
from urllib.parse import urlparse
import dns.resolver
import ssl
import datetime
import os.path


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
        self.length_url = self.get_length(self.url)

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
        self.domain_length = self.get_length(self.domain)

        self.directory_length = self.get_length(self.directory)
        self.count_freq(self.directory)
        self.qty_dot_directory = self.get_freq('.') if self.directory_length > 0 else -1
        self.qty_hyphen_directory = self.get_freq('-') if self.directory_length > 0 else -1
        self.qty_underline_directory = self.get_freq('_') if self.directory_length > 0 else -1
        self.qty_slash_directory = self.get_freq('/') if self.directory_length > 0 else -1
        self.qty_questionmark_directory = self.get_freq('?') if self.directory_length > 0 else -1
        self.qty_equal_directory = self.get_freq('=') if self.directory_length > 0 else -1
        self.qty_at_directory = self.get_freq('@') if self.directory_length > 0 else -1
        self.qty_and_directory = self.get_freq('&') if self.directory_length > 0 else -1
        self.qty_exclamation_directory = self.get_freq('!') if self.directory_length > 0 else -1
        self.qty_space_directory = self.get_freq(' ') if self.directory_length > 0 else -1
        self.qty_tilde_directory = self.get_freq('~') if self.directory_length > 0 else -1
        self.qty_comma_directory = self.get_freq(',') if self.directory_length > 0 else -1
        self.qty_plus_directory = self.get_freq('+') if self.directory_length > 0 else -1
        self.qty_asterisk_directory = self.get_freq('*') if self.directory_length > 0 else -1
        self.qty_hashtag_directory = self.get_freq('#') if self.directory_length > 0 else -1
        self.qty_dollar_directory = self.get_freq('$') if self.directory_length > 0 else -1
        self.qty_percent_directory = self.get_freq('%') if self.directory_length > 0 else -1

        self.count_freq(self.file)
        self.file_length = self.get_length(self.file)
        self.qty_dot_file = self.get_freq('.') if self.file_length > 0 else -1
        self.qty_hyphen_file = self.get_freq('-') if self.file_length > 0 else -1
        self.qty_underline_file = self.get_freq('_') if self.file_length > 0 else -1
        self.qty_slash_file = self.get_freq('/') if self.file_length > 0 else -1
        self.qty_questionmark_file = self.get_freq('?') if self.file_length > 0 else -1
        self.qty_equal_file = self.get_freq('=') if self.file_length > 0 else -1
        self.qty_at_file = self.get_freq('@') if self.file_length > 0 else -1
        self.qty_and_file = self.get_freq('&') if self.file_length > 0 else -1
        self.qty_exclamation_file = self.get_freq('!') if self.file_length > 0 else -1
        self.qty_space_file = self.get_freq(' ') if self.file_length > 0 else -1
        self.qty_tilde_file = self.get_freq('~') if self.file_length > 0 else -1
        self.qty_comma_file = self.get_freq(',') if self.file_length > 0 else -1
        self.qty_plus_file = self.get_freq('+') if self.file_length > 0 else -1
        self.qty_asterisk_file = self.get_freq('*') if self.file_length > 0 else -1
        self.qty_hashtag_file = self.get_freq('#') if self.file_length > 0 else -1
        self.qty_dollar_file = self.get_freq('$') if self.file_length > 0 else -1
        self.qty_percent_file = self.get_freq('%') if self.file_length > 0 else -1

        self.count_freq(self.params)
        self.params_length = self.get_length(self.params)
        self.qty_params = self.get_number_of_params()
        self.qty_dot_params = self.get_freq('.') if self.params_length > 0 else -1
        self.qty_hyphen_params = self.get_freq('-') if self.params_length > 0 else -1
        self.qty_underline_params = self.get_freq('_') if self.params_length > 0 else -1
        self.qty_slash_params = self.get_freq('/') if self.params_length > 0 else -1
        self.qty_questionmark_params = self.get_freq('?') if self.params_length > 0 else -1
        self.qty_equal_params = self.get_freq('=') if self.params_length > 0 else -1
        self.qty_at_params = self.get_freq('@') if self.params_length > 0 else -1
        self.qty_and_params = self.get_freq('&') if self.params_length > 0 else -1
        self.qty_exclamation_params = self.get_freq('!') if self.params_length > 0 else -1
        self.qty_space_params = self.get_freq(' ') if self.params_length > 0 else -1
        self.qty_tilde_params = self.get_freq('~') if self.params_length > 0 else -1
        self.qty_comma_params = self.get_freq(',') if self.params_length > 0 else -1
        self.qty_plus_params = self.get_freq('+') if self.params_length > 0 else -1
        self.qty_asterisk_params = self.get_freq('*') if self.params_length > 0 else -1
        self.qty_hashtag_params = self.get_freq('#') if self.params_length > 0 else -1
        self.qty_dollar_params = self.get_freq('$') if self.params_length > 0 else -1
        self.qty_percent_params = self.get_freq('%') if self.params_length > 0 else -1


        # others
        self.response_obj = requests.get(url, allow_redirects=True)
        self.whois_response = self.get_whois_response()

        self.time_response = self.get_response_time()
        self.asn_ip = self.get_asn_ip()
        self.time_domain_activation = self.get_activation_days()
        self.time_domain_expiration = self.get_expiration_days()
        self.qty_ip_resolved = self.get_ips_resolved()
        self.qty_nameservers = len(self.whois_response['name_servers']) if self.whois_response['name_servers'] else -1
        self.qty_mx_servers = self.get_mx_servers()
        self.tls_ssl_certificate = self.has_valid_certificate()
        self.qty_redirects = len(self.response_obj.history) - 1 if len(self.response_obj.history) > 0 else 0

        self.url_shortened = 1 if len(self.url) < len(self.response_obj.url) else 0

    def get_mx_servers(self):
        mx_count = 0
        try:
            answers = dns.resolver.query(self.domain, 'MX')
            for _ in answers:
                mx_count += 1
        except Exception:
            pass
        return mx_count

    def get_asn_ip(self):
        try:
            c = Client()
            ip = socket.gethostbyname(self.domain)
            return int(c.lookup(ip).asn)
        except Exception:
            return  -1

    def get_ips_resolved(self):
        ip_tuple = socket.gethostbyname_ex(self.domain)
        return len(ip_tuple) - 2

    def get_response_time(self):
        return self.response_obj.elapsed.total_seconds()

    def get_activation_days(self):
        if not self.whois_response['creation_date']:
            return -1
        if isinstance(self.whois_response['creation_date'], list):
            creation_date = self.whois_response['creation_date'][0]
        else:
            creation_date = self.whois_response['creation_date']
        return (datetime.datetime.today() - creation_date).days

    def get_expiration_days(self):
        if not self.whois_response['expiration_date']:
            return -1
        if isinstance(self.whois_response['expiration_date'], list):
            expiration_date = self.whois_response['expiration_date'][0]
        else:
            expiration_date = self.whois_response['expiration_date']
        return (expiration_date - datetime.datetime.today()).days

    def ssl_expiry_datetime(self):
        ssl_dateformat = r'%b %d %H:%M:%S %Y %Z'

        context = ssl.create_default_context()
        context.check_hostname = False

        conn = context.wrap_socket(
            socket.socket(socket.AF_INET),
            server_hostname=self.domain,
        )
        # 5 second timeout
        conn.settimeout(1.0)

        conn.connect((self.domain, 443))
        ssl_info = conn.getpeercert()
        # Python datetime object
        return datetime.datetime.strptime(ssl_info['notAfter'], ssl_dateformat)

    def has_valid_certificate(self):
        try:
            now = datetime.datetime.now()
            cert_expiry_time = self.ssl_expiry_datetime()
            if cert_expiry_time > now:
                return 1
        except Exception:
            pass
        return 0

    def split_url(self):
        parsed_url = urlparse(self.url)
        self.domain = parsed_url.netloc
        split_path = os.path.split(parsed_url.path)
        self.params = parsed_url.query

        if len(split_path) > 0:
            self.directory = split_path[0][1:]

        if len(split_path) > 1:
            self.file = split_path[1]

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

    @staticmethod
    def get_length(input_str):
        return len(input_str)

    def print_features(self):
        di = {}
        for key in self.__dict__.keys():
            if key not in ["count", "whois_response"]:
                di[key] = self.__dict__[key]
        pprint(di)

    def get_number_of_params(self):
        if len(self.params) == 0:
            return 0
        return len(self.params.split('&'))

    def get_whois_response(self):
        try:
            return whois.whois(self.url)
        except Exception:
            return {"expiration_date": None, "creation_date": None, "name_servers": None}