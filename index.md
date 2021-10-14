<a href="https://github.com/you"><img loading="lazy" width="149" height="149" src="https://github.blog/wp-content/uploads/2008/12/forkme_left_red_aa0000.png?resize=149%2C149" class="attachment-full size-full" alt="Fork me on GitHub" data-recalc-dims="1"></a>
## Sabe Dökümantasyonuna hoşgeldiniz!

Sabe kolayca web server kurmak için yazılmış bir python kütüphanesidir.


### Merhaba Dünya

```py
import sabe
app = sabe.Sabe()
app.route("/", "Merhaba Dünya")
```
**info()**<br>
bilgilendirme metinini görüntüler<br>

**version**<br>
versiyonu döndürür<br>


**render_file(filename, encoding="utf8") tür: String Argümanlar: 2**<br>
dosyanın içini okur ve içerğini döndürür<br>
örnek: `app.route("/", app.render_file("örnek.html")`
<br>

**render_website(url) tür: string Argümanlar: 2**<br>
⚠️Dikkat⚠️ Bu işlem bazı sitelerin lisans haklarına aykırırdır. Olası bir lisans probleminde sorumluluk kabul edilmez<br>
web sitesinin içerğini döndürür<br>
örnek: `app.route("/", app.render_website("example.com"))`<br>

**routes()**<br>
bütün "yolları (routes)" döndürür.<br>

**url_routes()**<br>
Bütün kayıtlı "url" leri döndürür.<br>


**route(route, code) tür: string Argümanlar: 2**<br>
uygulamaya "yol" ekler<br>
örnek: `app.route("/", "<h1>Merhaba Dünya</h1>)`<br>

**error_page_add(error_code, code) tür: string Argümanlar: 2**<br>
uygulamaya oluşan hatalar için (404 vb) klasik hata sayfası yerine özel hata sayfası oluşturur<br>
örnek: `app.error_page_add("404", "<h1>404</h1>)`

**run()**<br>
uygulamayı çalıştırır.<br>
### İletişim

iletişim mail adresim <a href="mailto:zoda@vuhuv.com">zoda@vuhuv.com</a>
