# Sanallaştırılmış bilgisayar verisi ve kolay web sayfası oluşturucusu
from flask import Flask, render_template, request
from colorama import init
from termcolor import colored
import webbrowser
import flask
from waitress import serve
init()


class Sabe:
    """Sabe web uygulamarını daha kolay ve hızlı şekilde yapabilmek için yazılmıştır"""

    def __init__(self):
        self.app = Flask(__name__)
        self.route_list = []
        self.url_list = []
        self.version = "2.0.1"

    def info(self):
        print("Sabe © Kerem ata\n\nSabe kolay web sitesi oluşturmak için yazılmış bir frameworkdür\nTemelinde flask bulunmaktadır")

    def version(self):
        """return version"""
        return self.version

    def render_website(self, route, url):
        """get file content render content (cannot get css or js file(s))"""
        try:
            import requests
        except:
            print(colored("requests modülü bulunamadı", "red"))
        try:
            url = requests.get(url)

            @self.app.route(route)
            def page():
                return url.text

            self.url_list.append(url)
        except requests.exceptions.MissingSchema:
            #print(colored(f"Geçersiz Url: Bunu mu demek istedinizi? (https://{url})", "red"))

            print(colored(f"Geçersiz Url: Bunu mu demek istediniz? (https://{url})", "red"))

    def url_routes(self):
        """return all websites urls"""
        return(self.url_routes)

    def routes(self):
        """return all routes"""
        return(self.route_list)

    def route(self, route, code):
        """add route for application"""
        self.route_list.append(route)

        @self.app.route(route)
        def page():
            return code

    def error_page_add(self, error_code, code):
        """Add error page for application"""
        if error_code == "404":
            @self.app.errorhandler(404)
            def not_found(e):
                return code
        elif error_code == "500":
            @self.app.errorhandler(500)
            def server_error(e):
                return code
        else:
            print(colored(f"Hata kodu {error_code} bulunamadı", "red"))

    def render_file(self, filename, encoding="utf8"):
        """Render files (default encoding=utf8)"""
        with open(filename, encoding=encoding) as filecontant:
            return filecontant.read()

    def run(self):
        """Run application"""
        self.app.run()

    def __str__(self):
        return "<Sabe>"

        
