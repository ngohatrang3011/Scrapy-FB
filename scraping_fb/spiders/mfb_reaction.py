from urllib.parse import urljoin
import scrapy
from scrapy.selector import Selector
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from shutil import which
from time import sleep

cookie = "cookie: sb=a75iYNhZ7wizl44PGndgDKZY; _fbp=fb.1.1617786963671.1059209162; locale=vi_VN; datr=Gp3uYIVzw3OzZlSHnc2sVMJO; c_user=100022337169390; wd=1349x657; spin=r.1004114193_b.trunk_t.1626362078_s.1_v.2_; presence=C%7B%22t3%22%3A%5B%7B%22i%22%3A%22u.100012249136842%22%7D%2C%7B%22i%22%3A%22u.100005453856197%22%7D%5D%2C%22utc3%22%3A1626417408813%2C%22lm3%22%3A%22u.100012249136842%22%2C%22v%22%3A1%7D; xs=21%3A52dFhnqzMvAabA%3A2%3A1626256369%3A-1%3A6382%3A%3AAcUb80NTZZOuLBLRiJaDmmyjm8UfFl64YkjdGfYVwuU; fr=12OmUIypE3gw3LJUh.AWVUe_1tvAOZNVTm4Ub5rmq0V0o.Bg8TGR.2t.GDx.0.0.Bg8TGR."


class MfbReactionSpider(scrapy.Spider):
    name = 'mfb_reaction'
    allowed_domains = ['m.facebook.com']

    # for p in list_post:z
    start_urls = ['https://m.facebook.com/AbbieOh.Vietnam']

    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")

        chrome_path = which("chromedriver.exe")
        self.driver = webdriver.Chrome(executable_path=chrome_path)

    def parse(self, response):
        self.driver.get("https://m.facebook.com/")

        def loginFacebookByCookie(cookie):
            script = 'javascript:void(function(){ function setCookie(t) { var list = t.split("; "); console.log(list); for (var i = list.length - 1; i >= 0; i--) { var cname = list[i].split("=")[0]; var cvalue = list[i].split("=")[1]; var d = new Date(); d.setTime(d.getTime() + (7*24*60*60*1000)); var expires = ";domain=.facebook.com;expires="+ d.toUTCString(); document.cookie = cname + "=" + cvalue + "; " + expires; } } function hex2a(hex) { var str = ""; for (var i = 0; i < hex.length; i += 2) { var v = parseInt(hex.substr(i, 2), 16); if (v) str += String.fromCharCode(v); } return str; } setCookie("' + cookie + '"); location.href = "https://m.facebook.com/"; })();'
            self.driver.execute_script(script)
            sleep(5)

        loginFacebookByCookie(cookie)
        list_post = [1261420020967676]
        for p in list_post:
            # REACTION
            link_post = 'https://m.facebook.com/story.php?story_fbid={post_id}&id={page_id}'
            link_url = link_post.format(post_id=p, page_id=454894214953598)
            self.driver.get(link_url)
            sleep(5)
            try:
                reaction_page = self.driver.find_element_by_xpath("//div[@class='_45kb ufi']/div[@class='_52jh _5ton _45m7']/a")
                reaction_page.click()
                sleep(5)
                count_reaction = 0
                while True:
                    try:
                        load_reactions = self.driver.find_element_by_xpath(
                            "//div[@id='reaction_profile_pager']/a")
                    except:
                        print("last reaction")
                        break
                    count_reaction += 1
                    print(count_reaction)

                    load_reactions.click()
                    sleep(5)
                resp_reaction = Selector(text=self.driver.page_source)
                print(resp_reaction)
                links_reaction_xpath = "//div[@class='_4mn c']/a/@href"
                links_profile_reaction = resp_reaction.xpath(
                    links_reaction_xpath).getall()

                names_reaction_xpath = "//div[@class='_4mn c']/a//strong/text()"
                names_reaction = resp_reaction.xpath(names_reaction_xpath).getall()
            except:
                pass
            for link, name in zip(links_profile_reaction, names_reaction):
                yield {
                    "post_id": p,
                    "link_profile": "https://www.facebook.com"+str(link),
                    "name": name
                }

        sleep(2)
        self.driver.close()
