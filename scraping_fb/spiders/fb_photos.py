# from urllib.parse import urljoin
# import scrapy
# from scrapy.selector import Selector
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.chrome.options import Options
# from shutil import which
# from time import sleep

# # from six import text_type

# # chrome_options = Options()
# # chrome_options.add_argument("--headless")
# # chrome_path = which("chromedriver.exe")

# cookie = "cookie: sb=a75iYNhZ7wizl44PGndgDKZY; _fbp=fb.1.1617786963671.1059209162; locale=vi_VN; datr=JhTsYAw_B4pb6R0baDcv6KhG; c_user=100022337169390; spin=r.1004100728_b.trunk_t.1626084398_s.1_v.2_; m_pixel_ratio=1; x-referer=eyJyIjoiL3N0b3J5LnBocD9zdG9yeV9mYmlkPTQ1NzgzNDUxMDg4NTExODYmaWQ9NDU0ODk0MjE0OTUzNTk4IiwiaCI6Ii9zdG9yeS5waHA%2Fc3RvcnlfZmJpZD00NTc4MzQ1MTA4ODUxMTg2JmlkPTQ1NDg5NDIxNDk1MzU5OCIsInMiOiJtIn0%3D; presence=C%7B%22t3%22%3A%5B%7B%22i%22%3A%22p.1059845080701224%22%7D%2C%7B%22i%22%3A%22g.2106848579392852%22%7D%2C%7B%22i%22%3A%22u.100035747986272%22%7D%2C%7B%22i%22%3A%22u.100004754438942%22%7D%2C%7B%22i%22%3A%22u.100009511834873%22%7D%2C%7B%22i%22%3A%22g.1715374488573804%22%7D%5D%2C%22utc3%22%3A1626158880723%2C%22lm3%22%3A%22p.1059845080701224%22%2C%22v%22%3A1%7D; xs=9%3Aj8BcS3jepaDEyA%3A2%3A1626084396%3A-1%3A6382%3A%3AAcXe1G6pcTqaQEfq2jvN5NqEOAYdvdZV00JaHh6IMEE; fr=1B0LSSUJEVcsNZR9M.AWXVltwKaw32UCHnlTSKhzNpxHY.Bg7TjS.eb.AAA.0.0.Bg7TjS.AWWZgJxViho; wd=774x657"


# class MfbSpider(scrapy.Spider):
#     name = 'mfb'
#     allowed_domains = ['m.facebook.com']

#     # for p in list_post:z
#     start_urls = ['https://m.facebook.com/ksclosetvn/']

#     def __init__(self):
#         chrome_options = Options()
#         chrome_options.add_argument("--headless")

#         chrome_path = which("chromedriver.exe")
#         self.driver = webdriver.Chrome(executable_path=chrome_path)

#     # def start_requests(self):
#     #     # list_post = [279230610653262, 299324851977171]
#     #     # for p in list_post:
#     #     #     # post = p[0]

#     #     return scrapy.Request(url=link_url, callback=self.parse_post)

#     def parse(self, response):
#         self.driver.get("https://m.facebook.com/")

#         def loginFacebookByCookie(cookie):
#             script = 'javascript:void(function(){ function setCookie(t) { var list = t.split("; "); console.log(list); for (var i = list.length - 1; i >= 0; i--) { var cname = list[i].split("=")[0]; var cvalue = list[i].split("=")[1]; var d = new Date(); d.setTime(d.getTime() + (7*24*60*60*1000)); var expires = ";domain=.facebook.com;expires="+ d.toUTCString(); document.cookie = cname + "=" + cvalue + "; " + expires; } } function hex2a(hex) { var str = ""; for (var i = 0; i < hex.length; i += 2) { var v = parseInt(hex.substr(i, 2), 16); if (v) str += String.fromCharCode(v); } return str; } setCookie("' + cookie + '"); location.href = "https://m.facebook.com/"; })();'
#             self.driver.execute_script(script)
#             sleep(5)

#         loginFacebookByCookie(cookie)
#         # list_post = [4565811536771210, 4578345108851186, 1857795267716723]
#         # for p in list_post:
#         #     link_post = 'https://m.facebook.com/story.php?story_fbid={post_id}&id={page_id}'
#         #     link_url = link_post.format(post_id=p, page_id=1059845080701224)
#         list_post = [4565811536771210]
#         for p in list_post:
#             # REACTION
#             link_post = 'https://m.facebook.com/ksclosetvn/photos/pcb.4565811536771210/4565807740104923/?type=3&source=48'
#             link_url = link_post.format(post_id=p, page_id=1059845080701224)
#             sleep(5)
#             self.driver.get(link_url)
#             count_post = 0

#             # hidden_comment = ""
#             while True:
#                 try:
#                     load_comments = self.driver.find_element_by_xpath(
#                         "//div[@class='async_elem']/a")
#                 except:
#                     print("last comment")
#                     break
#                 count_post += 1
#                 print(count_post)

#                 load_comments.click()
#                 sleep(3)
#                 # print("test =" + str(test))
#             while True:
#                 try:
#                     view_more_reply = self.driver.find_element_by_xpath(
#                         "//div[@class='_2b1l']/a")
#                 except:
#                     print("last comment")
#                     break
#                 count_post += 1
#                 print(count_post)

#                 view_more_reply.click()
#                 sleep(1)
#             while True:
#                 try:
#                     reply_not_from_shop = self.driver.find_element_by_xpath(
#                         "//div[@class='_2b1h async_elem']/a")
#                 except:
#                     print("last comment")
#                     break
#                 count_post += 1
#                 print(count_post)

#                 reply_not_from_shop.click()
#                 sleep(1)

#             resp = Selector(text=self.driver.page_source)
#             comments_id_xpath = "//div[@class='_333v _45kb']//div[@data-sigil='comment-body']/@data-commentid"
#             comments_id = resp.xpath(comments_id_xpath).getall()

#             links_xpath = "//div[@class='_333v _45kb']//div[@class='_2b05']/a/@href"
#             # print("links = " + links_xpath)
#             links_profile = resp.xpath(links_xpath).getall()
#             # print(links_profile)

#             names_xpath = "//div[@class='_333v _45kb']//div[@class='_2b05']/a/text()"
#             # print("names = " + names_xpath)
#             names = resp.xpath(names_xpath).getall()
#             # print(names)

#             comments_xpath = "//div[@class='_333v _45kb']//div[@data-sigil='comment-body']"
#             # print("comments = "+comments_xpath)
#             comments = resp.xpath(comments_xpath).getall()

#             for comment_id, link, name, comment in zip(comments_id, links_profile, names, comments):
#                 yield {
#                     "comment_id": comment_id,
#                     "post_id": p,
#                     "link_profile": "https://www.facebook.com"+str(link),
#                     "name": name,
#                     "comment": {
#                         "tag_link": Selector(text=comment).xpath("//a/@href").get(),
#                         "tag_text": Selector(text=comment).xpath("//a/text()").get(),
#                         "text": Selector(text=comment).xpath("//text()").get()
#                     }
#                 }

#         sleep(10)
#         self.driver.close()
