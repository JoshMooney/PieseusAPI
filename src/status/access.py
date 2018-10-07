import requests


class Access(object):
    def __init__(self, ip=None, port=None, endpoint=None):
        self._ip = ip
        self._port = port
        self._endpoint = endpoint

    def url(self):
        url = "http://"
        if not self._ip:
            return
        else:
            url += self._ip

        if self._port:
            url += ":%s" % (self._port)
        if self._endpoint:
            url += self._endpoint
        return url


class MicroserviceAccess(object):
    def __init__(self, name):
        self._service_name = name
        self._default_msg = "%s microservice is %s via %s @%s"

    def check_all(self, local=None, external=None, domain=None):
        msg = {}
        if local:
            msg['local'] = self.local(local)
        if external:
            msg['external'] = self.external(external)
        if domain:
            msg['domain'] = self.domain(domain)
        return msg

    def local(self, access):
        url = access.url()
        response_msg = { "name": self._service_name, "status": "False"}
        try:
            curl_local = requests.get(url)
            if (curl_local.status_code is 200):
                response_msg['status'] = 'True'
        except Exception as err:
            print(err)

        response_msg['value'] = url
        response_msg['msg'] = self._create_resposne_message(name=self._service_name,
                                                            status=response_msg['status'],
                                                            type="Local IP Address",
                                                            url=url)
        return response_msg

    def external(self, access):
        url = access.url()
        response_msg = {"name": self._service_name, "status": "False"}
        try:
            curl_extern = requests.get(access.url())
            if (curl_extern.status_code is 200):
                response_msg['status'] = 'True'
        except Exception as err:
            print(err)

        response_msg['value'] = url
        response_msg['msg'] = self._create_resposne_message(name=self._service_name,
                                                            status=response_msg['status'],
                                                            type="External IP Address",
                                                            url=access.url())
        return response_msg

    def domain(self, access):
        url = access.url()
        response_msg = {"name": self._service_name, "status": "False"}
        try:
            curl_domain = requests.get('http://www.Theseus.tk/jblog')
            if (curl_domain.status_code is 200):
                response_msg['status'] = 'True'
        except Exception as err:
            print(err)

        response_msg['value'] = url
        response_msg['msg'] = self._create_resposne_message(name=self._service_name,
                                                            status=response_msg['status'],
                                                            type="Domain Name",
                                                            url=url)
        return response_msg

    def _create_resposne_message(self, name, status, type, url):
        if status == 'True':
            status = "accessible"
        else:
            status = "not accessible"

        return self._default_msg % (name, status, type, url)