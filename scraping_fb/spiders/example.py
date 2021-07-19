# from time import sleep
# import scrapy
# from scrapy.selector import Selector
# from scrapy_selenium import SeleniumRequest
# from shutil import which
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options

# from selenium.webdriver.common.keys import Keys

# chrome_options = Options()
# chrome_options.add_argument("--headless")
# chrome_path = which("chromedriver.exe")


# cookie = "Cookie: sb=GpfVYAzVVVJymx1bhn-5bSnN; datr=GpfVYMivvJYU3WEg_8qkzDpk; _fbp=fb.1.1625481791766.879578012; wd=1848x949; locale=en_US; c_user=100004898083962; spin=r.1004093971_b.trunk_t.1625796230_s.1_v.2_; usida=%7B%22ver%22%3A1%2C%22id%22%3A%22Aqvyhhnd1heba%22%2C%22time%22%3A1625797851%7D; xs=22%3AusrOQXJ5ONweWQ%3A2%3A1625796228%3A-1%3A6300%3A%3AAcUGKLSFpFaWTI8ZumN10YNLyI6z571MPTVe-RiBWA; fr=1xlmlCTkSwvsjF24Q.AWXE-doYSEXLEnE0yEnBZjzCmv0.Bg57Th.Rb.AAA.0.0.Bg57Th.AWWW15-1e98"


# class ExampleSpider(scrapy.Spider):
#     name = 'example'

#     def __init__(self):
#         self.html_file = open("text2.html", 'w')

#     def start_requests(self):
#         def loginFacebookByCookie(cookie):
#             script = 'javascript:void(function(){ function setCookie(t) { var list = t.split("; "); console.log(list); for (var i = list.length - 1; i >= 0; i--) { var cname = list[i].split("=")[0]; var cvalue = list[i].split("=")[1]; var d = new Date(); d.setTime(d.getTime() + (7*24*60*60*1000)); var expires = ";domain=.facebook.com;expires="+ d.toUTCString(); document.cookie = cname + "=" + cvalue + "; " + expires; } } function hex2a(hex) { var str = ""; for (var i = 0; i < hex.length; i += 2) { var v = parseInt(hex.substr(i, 2), 16); if (v) str += String.fromCharCode(v); } return str; } setCookie("' + cookie + '"); location.href = "https://www.facebook.com/"; })();'
#             self.driver.execute_script(script)

#         loginFacebookByCookie(cookie)
        
#         yield SeleniumRequest(
#             url="https://www.facebook.com/",
#             wait_time=3,
#             screenshot=True,
#             callback=self.parse,
#             dont_filter=True
#         )

#     def parse(self, response):
#         driver = response.meta['driver']

#         # email_input = driver.find_element_by_xpath(
#         #     "(//input[@name='email'])[1]")
#         # email_input.send_keys("phanvandung2904@gmail.com")
#         # pass_input = driver.find_element_by_xpath("(//input[@name='pass'])[1]")
#         # pass_input.send_keys("Td19962000@")
#         # # login = driver.find_element_by_xpath("//input[@data-testid='royal_login_button']")
#         # pass_input.send_keys(Keys.ENTER)
#         # sleep(10)
#         # driver.execute_script("window.scrollTo(500, document.body.scrollHeight);")
#         # sleep(5)

#         self.html = driver.page_source
#         resp = Selector(text=self.html)
#         links = resp.xpath("(//div[@class='j83agx80 cbu4d94t'])[1]//a[@class='oajrlxb2 gs1a9yip g5ia77u1 mtkw9kbi tlpljxtp qensuy8j ppp5ayq2 goun2846 ccm00jje s44p3ltw mk2mc5f4 rt8b4zig n8ej3o3l agehan2d sk4xxmp2 rq0escxv nhd2j8a9 q9uorilb mg4g778l btwxx1t3 pfnyh3mw p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x tgvbjcpo hpfvmrgz jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso l9j0dhe7 i1ao9s8h esuyzwwr f1sip0of du4w35lb lzcic4wl abiwlrkh p8dawk7l']/@href").getall()
#         names = resp.xpath("(//div[@class='j83agx80 cbu4d94t'])[1]//span[@class='pq6dq46d']/span/text()").getall()
#         comments = resp.xpath("(//div[@class='j83agx80 cbu4d94t'])[1]//div[@class='ecm0bbzt e5nlhep0 a8c37x1j']/span/div/div/text()").getall()

#         for link, name, comment in zip(links, names, comments):
#             yield {
#                 "link": link.split("?")[0],
#                 "name": name,
#                 "comment": comment
#             }

#         self.html_file.write(driver.page_source)
#         driver.close()
