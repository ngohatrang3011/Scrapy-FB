# from urllib.parse import urljoin
# from scrapy.selector import Selector
# import scrapy
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.chrome.options import Options
# from shutil import which
# import time

# # chrome_options = Options()
# # chrome_options.add_argument("--headless")
# # chrome_path = which("chromedriver.exe")

# cookie = "cookie: sb=a75iYNhZ7wizl44PGndgDKZY; datr=bb5iYKZG6zyZGnysnk1X4Eby; _fbp=fb.1.1617786963671.1059209162; locale=vi_VN; wd=1366x657; c_user=100022337169390; spin=r.1004089850_b.trunk_t.1625736718_s.1_v.2_; presence=C%7B%22t3%22%3A%5B%7B%22i%22%3A%22u.100012249136842%22%7D%5D%2C%22utc3%22%3A1625817020233%2C%22lm3%22%3A%22u.100012249136842%22%2C%22v%22%3A1%7D; xs=21%3A7dKdx3nG0nomew%3A2%3A1625736717%3A-1%3A6382%3A%3AAcWXWp7WQluLA6Nt4DaSl6zYglb_DJNJTHQ25gnx-hw; fr=1BQyIklz1out9taV2.AWX0-rz35qExtJpYUpd50BAV-xY.Bg6Asw.G6.GDo.0.0.Bg6Asw."


# class FbPostSpider(scrapy.Spider):
#     name = 'fb_post'
#     allowed_domains = ['m.facebook.com']
#     # list_post = [1258485707927774]
#     # for p in list_post:
#     start_urls = ['https://m.facebook.com/abbieoh.hanoi/posts/279230610653262']

#     def __init__(self):
#         chrome_options = Options()
#         chrome_options.add_argument("--headless")

#         chrome_path = which("chromedriver.exe")
#         self.driver = webdriver.Chrome(executable_path=chrome_path)

#     def parse(self, response):
#         self.driver.get("https://m.facebook.com/")

#         def loginFacebookByCookie(cookie):
#             script = 'javascript:void(function(){ function setCookie(t) { var list = t.split("; "); console.log(list); for (var i = list.length - 1; i >= 0; i--) { var cname = list[i].split("=")[0]; var cvalue = list[i].split("=")[1]; var d = new Date(); d.setTime(d.getTime() + (7*24*60*60*1000)); var expires = ";domain=.facebook.com;expires="+ d.toUTCString(); document.cookie = cname + "=" + cvalue + "; " + expires; } } function hex2a(hex) { var str = ""; for (var i = 0; i < hex.length; i += 2) { var v = parseInt(hex.substr(i, 2), 16); if (v) str += String.fromCharCode(v); } return str; } setCookie("' + cookie + '"); location.href = "https://www.facebook.com/"; })();'
#             self.driver.execute_script(script)

#         loginFacebookByCookie(cookie)

#         link_post = 'https://m.facebook.com/abbieoh.hanoi/posts/279230610653262'

#         # for p in list_post:
#         self.driver.get(link_post)

#         # self.fr

#         # search_input = self.driver.find_element_by_xpath("(//div[@class='oajrlxb2 g5ia77u1 qu0x051f esr5mh6w e9989ue4 r7d6kgcz rq0escxv nhd2j8a9 nc684nl6 p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso i1ao9s8h esuyzwwr f1sip0of lzcic4wl l9j0dhe7 abiwlrkh p8dawk7l'])[1]")
#         # search_input.click()
#         # all_comment = self.driver.find_element_by_xpath("(//div[@class='oajrlxb2 g5ia77u1 qu0x051f esr5mh6w e9989ue4 r7d6kgcz rq0escxv nhd2j8a9 j83agx80 p7hjln8o kvgmc6g5 oi9244e8 oygrvhab h676nmdw pybr56ya dflh9lhu f10w8fjw scb9dxdr i1ao9s8h esuyzwwr f1sip0of lzcic4wl l9j0dhe7 abiwlrkh p8dawk7l bp9cbjyn dwo3fsh8 btwxx1t3 pfnyh3mw du4w35lb'])[3]")
#         # all_comment.click()
#         # time.sleep(5)
#         self.driver.execute_script(
#             "window.scrollTo(500, document.body.scrollHeight);")
#         time.sleep(5)

#         resp = Selector(text=self.driver.page_source)
#         # # # print(resp)
#         links_profile = resp.xpath("//div[@class='_2b05']/a/@href").getall()
#         names = resp.xpath(
#             "//div[@class='_2b05']/a/text()").getall()
#         comments = resp.xpath(
#             "//div[@data-sigil='comment-body']/text()").getall()

#         for link, name, comment in zip(links_profile, names, comments):
#             yield {
#                 "link": link,
#                 "name": name,
#                 "comment": comment
#             }

#         time.sleep(10)
#         self.driver.close()

#         # list_post = [1258485707927774, 1245614292548249, 1258485707927774]
#         # for p in range(len(list_post)):
#         #     yield scrapy.Request(url=urljoin(response.url, list_post[p] ), callback=self.parse)

#         # email_input = self.driver.find_element_by_xpath("(//input[@name='email'])[1]")
#         # email_input.send_keys("phanvandung2904@gmail.com")
#         # time.sleep(3)
#         # pass_input = self.driver.find_element_by_xpath("(//input[@name='pass'])[1]")
#         # time.sleep(3)
#         # pass_input.send_keys("Td19962000@")
#         # # login = driver.find_element_by_xpath("//input[@data-testid='royal_login_button']")
#         # pass_input.send_keys(Keys.ENTER)
#         # time.sleep(10)
#         # self.html = self.driver.page_source
#         # links = response.xpath("*//a[@class='oajrlxb2 gs1a9yip g5ia77u1 mtkw9kbi tlpljxtp qensuy8j ppp5ayq2 goun2846 ccm00jje s44p3ltw mk2mc5f4 rt8b4zig n8ej3o3l agehan2d sk4xxmp2 rq0escxv nhd2j8a9 q9uorilb mg4g778l btwxx1t3 pfnyh3mw p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x tgvbjcpo hpfvmrgz jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso l9j0dhe7 i1ao9s8h esuyzwwr f1sip0of du4w35lb lzcic4wl abiwlrkh p8dawk7l']")
#         # print(links)
#         # more_comment = response.xpath("/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[4]/div[2]/div[1]/div[2]/div/div/div/div/div/div/div/div[1]/div/div[2]/div/div[5]/div/div/div[2]/div[4]/div[1]/div[2]/span/span")
#         # if more_comment:
#         #     more_comment.click()
