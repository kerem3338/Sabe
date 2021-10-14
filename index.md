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
Some Markdown text with <span style="color:blue">some *blue* text</span>.
web sitesinin içerğini döndürür<br>
### İletişim

iletişim mail adresim <a href="mailto:zoda@vuhuv.com">zoda@vuhuv.com</a>
