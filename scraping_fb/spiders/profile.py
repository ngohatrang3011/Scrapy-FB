from logging import info
import re
from urllib.parse import urljoin
import scrapy
from scrapy.selector import Selector
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from shutil import which
from time import sleep
from datetime import datetime

now = datetime.now()

timestamp = datetime.timestamp(now)
dt_object = datetime.fromtimestamp(timestamp)
dt_object = dt_object.strftime("%b %d %Y %H:%M:%S")

cookie = "cookie: sb=a75iYNhZ7wizl44PGndgDKZY; _fbp=fb.1.1617786963671.1059209162; locale=vi_VN; datr=Gp3uYIVzw3OzZlSHnc2sVMJO; c_user=100022337169390; wd=1349x657; spin=r.1004123825_b.trunk_t.1626616735_s.1_v.2_; xs=21%3A52dFhnqzMvAabA%3A2%3A1626256369%3A-1%3A6382%3A%3AAcWzZEOkpEsphg1_vmhGU9N7npXHGTtpznDOO8k8qtQ; fr=1BPF3sATcd4ybmVgW.AWWU-SfHVzficHs-xf8sPqGawlg.Bg9NbF.2t.AAA.0.0.Bg9NbF.AWXYjd7N4ZE; presence=C%7B%22t3%22%3A%5B%7B%22i%22%3A%22u.100004754438942%22%7D%5D%2C%22utc3%22%3A1626660201744%2C%22lm3%22%3A%22u.100004754438942%22%2C%22v%22%3A1%7D"

class MfbSpider(scrapy.Spider):
    name = 'mfb_profile'
    allowed_domains = ['m.facebook.com']

    # for p in list_post:z
    start_urls = ['https://m.facebook.com/']

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
            sleep(3)

        loginFacebookByCookie(cookie)
        profile = ['sharkbi']
        for p in profile:
            link_profile = 'https://m.facebook.com/{profile}/about'
            link_url = link_profile.format(profile=p)
            self.driver.get(link_url)
            sleep(10)

            self.driver.execute_script(
                "window.scrollTo(0, document.body.scrollHeight);")
            
            sleep(10)
           )
            resp = Selector(text=self.driver.page_source)
           
            about_xpath = "//div[contains(@class,'_4jbs')]"
            about = resp.xpath(about_xpath).get()


            # work
            try:
                works_info = []
                works = Selector(text=about).xpath(
                    "//div[@id='work']//div[@class='_2pir c']").getall()
                for work in works:
                    work = {
                        "link_title": "https://www.facebook.com" + str(Selector(text=work).xpath("//span/a/@href").get()) if Selector(text=work).xpath("//span/a/@href").get() else "None",
                        "title": Selector(text=work).xpath("//span/a/text()").get() if Selector(text=work).xpath("//span/a/text()").get() else "None",
                        "type": Selector(text=work).xpath("//span[@class='_52jc _52ja']/text()").get() if Selector(text=work).xpath("//span[@class='_52jc _52ja']/text()").get() else "None",
                        "time_period": Selector(text=work).xpath("//span[@class='_52jc _52j9']/text()").get() if Selector(text=work).xpath("//span[@class='_52jc _52j9']/text()").get() else "None",
                        "description": Selector(text=work).xpath("//span[@class='_52jc _52jb']/span/text()").get() if Selector(text=work).xpath("//span[@class='_52jc _52jb']/span/text()").get() else "None",
                    }
                    works_copy = work.copy()
                    works_info.append(works_copy)
            except:
                works = "None"

            # education
            try:
                edu_info = []
                educations = Selector(text=about).xpath(
                    "//div[@id='education']//div[@class='_2pir c']").getall()
                # print(education)
                for edu in educations:
                    dict_edu = {
                        "link_title": "https://www.facebook.com" + str(Selector(text=edu).xpath("//span/a/@href").get()) if Selector(text=edu).xpath("//span/a/@href").get() else "None",
                        "title": Selector(text=edu).xpath("//span/text()").get() if Selector(text=edu).xpath("//span/text()").get() else Selector(text=edu).xpath("//span/a/text()").get(),
                        "type": Selector(text=edu).xpath("//span[@class='_52jc _52ja']/text()").get() if Selector(text=edu).xpath("//span[@class='_52jc _52ja']/text()").get() else "None",
                        "time_period": Selector(text=edu).xpath("//span[@class='_52jc _52j9']/text()").get() if Selector(text=edu).xpath("//span[@class='_52jc _52j9']/text()").get() else "None",
                        "description": Selector(text=edu).xpath("//span[@class='_52jc _52jb']/span/text()").get() if Selector(text=edu).xpath("//span[@class='_52jc _52jb']/span/text()").get() else "None",
                    }
                    edu_copy = dict_edu.copy()
                    edu_info.append(edu_copy)
            except:
                educations = "None"

            # living
            try:
                livings = []
                living = Selector(text=about).xpath(
                    "//div[@id='living']//div[@class='_2swz _2lcw']").getall()
                for live in living:
                    dict_living = {
                        "title": Selector(text=live).xpath("//h4/text()").get() if Selector(text=live).xpath("//h4/text()").get() else "None",
                        "type": Selector(text=live).xpath("//h4[@class='_52jc _52ja _52jg']/text()").get() if Selector(text=live).xpath("//h4[@class='_52jc _52ja _52jg']/text()").get() else "None"
                    }
                    living_copy = dict_living.copy()
                    livings.append(living_copy)
            except:
                living = "None"

            # contact-info
            try:
                contact = []
                contact_infos = Selector(text=about).xpath(
                    "//div[@id='contact-info']//div[@class='_5cds _2lcw _5cdu']").getall()
                for contact_info in contact_infos:
                    dict_contact_info = {
                        "title": Selector(text=contact_info).xpath("//span[@class='_52jd _52ja _52jg']/text()").get() if Selector(text=contact_info).xpath("//span[@class='_52jd _52ja _52jg']/text()").get() else "None",
                        "type": Selector(text=contact_info).xpath("//div[@class='_5cdv r']/text()").get() if Selector(text=contact_info).xpath("//div[@class='_5cdv r']/text()").get() else "None"
                    }
                    contact_copy = dict_contact_info.copy()
                    contact.append(contact_copy)
            except:
                contact_infos = "None"

            # basic-info
            try:
                basics_info = []
                basic_infos = Selector(text=about).xpath(
                    "//div[@id='basic-info']//div[@class='_5cds _2lcw _5cdu']").getall()
                for basic_info in basic_infos:
                    dict_basic_info = {
                        "title": Selector(text=basic_info).xpath("//span[@class='_52jd _52ja _52jg']/text()").get() if Selector(text=basic_info).xpath("//span[@class='_52jd _52ja _52jg']/text()").get() else "None",
                        "type": Selector(text=basic_info).xpath("//div[@class='_5cdv r']/text()").get() if Selector(text=basic_info).xpath("//div[@class='_5cdv r']/text()").get() else "None"
                    }
                    basic_copy = dict_basic_info.copy()
                    basics_info.append(basic_copy)
            except:
                basic_infos = "None"

            # nicknames
            try:
                nickname_list = []
                nicknames = Selector(text=about).xpath(
                    "//div[@id='nicknames']//div[@class='_55x2 _5ji7']").getall()
                for nickname in nicknames:
                    dict_nickname = {
                        "title": Selector(text=nickname).xpath("//span[@class='_52jd _52ja _52jg']/text()").get() if Selector(text=nickname).xpath("//span[@class='_52jd _52ja _52jg']/text()").get() else "None",
                        "type": Selector(text=nickname).xpath("//div[@class='_5cdv r']/text()").get() if Selector(text=nickname).xpath("//div[@class='_5cdv r']/text()").get() else "None"
                    }
                    nickname_copy = dict_nickname.copy()
                    nickname_list.append(nickname_copy)
            except:
                nicknames = "None"

            # relationship
            try:
                relationship_list = []
                relationships = Selector(text=about).xpath(
                    "//div[@id='relationship']//div[@class='_55x2 _5ji7']").getall()
                for relationship in relationships:
                    if Selector(text=relationship).xpath("//div[@class='_52ja _5cds _5cdt']/text()").get():
                        dict_relationship = {
                            "title": Selector(text=relationship).xpath("//div[@class='_52ja _5cds _5cdt']/text()").get()

                        }
                    elif Selector(text=relationship).xpath("//div[@class='_4g34']").get():
                        dict_relationship = {
                            "title": Selector(text=relationship).xpath("//h3[@class='_52ja _52jg']/text()").get() if Selector(text=relationship).xpath("//h3[@class='_52ja _52jg']/text()").get() else "None",
                            "partner": Selector(text=relationship).xpath("//span[@class='_52jb']/text()").get() if Selector(text=relationship).xpath("//span[@class='_52jb']/text()").get() else "None",
                            "partner_profile": "https://www.facebook.com" + str(Selector(text=relationship).xpath("//h3/a/@href").get()) if Selector(text=relationship).xpath("//h3/a/@href").get() else "None"
                        }
                    rela_copy = dict_relationship.copy()
                    relationship_list.append(rela_copy)
            except:
                relationships = "None"

            # family
            try:
                member_list = []
                members = Selector(text=about).xpath(
                    "//div[@id='family']//div[@class='_5r7k _2lcw']").getall()
                for member in members:
                    dict_member = {
                        "name": Selector(text=member).xpath("//span[@class='_52jb']/text()").get() if Selector(text=member).xpath("//span[@class='_52jb']/text()").get() else "None",
                        "title": Selector(text=member).xpath("//h3[@class='_52ja _52jg']/text()").get() if Selector(text=member).xpath("//h3[@class='_52ja _52jg']/text()").get() else "None",
                        "member_profile": "https://www.facebook.com" + str(Selector(text=member).xpath("//h3/a/@href").get()) if Selector(text=member).xpath("//h3/a/@href").get() else "None"
                    }
                    member_copy = dict_member.copy()
                    member_list.append(member_copy)
            except:
                members = "None"

            # quote
            try:
                quote_list = []
                quotes = Selector(text=about).xpath(
                    "//div[@id='quote']//div[@class='_55x2 _5ji7']").getall()
                for quote in quotes:
                    dict_quote = {
                        "content": Selector(text=quote).xpath("//div[@class='_5cds _2lcw _5cdt']/text()").get() if Selector(text=quote).xpath("//div[@class='_5cds _2lcw _5cdt']/text()").get() else "None"}
                    quote_copy = dict_quote.copy()
                    quote_list.append(quote_copy)
            except:
                quotes = "None"

            # bio
            try:
                bio_list = []
                bios = Selector(text=about).xpath(
                    "//div[@id='bio']//div[@class='_55x2 _5ji7']").getall()
                for bio in bios:
                    dict_bio = {
                        "content": Selector(text=bio).xpath("//div[@class='_5cds _2lcw _5cdt']/text()").get() if Selector(text=bio).xpath("//div[@class='_5cds _2lcw _5cdt']/text()").get() else "None"}
                    bio_copy = dict_bio.copy()
                    bio_list.append(bio_copy)
            except:
                bios = "None"

            yield {
                "id": p,
                "works": works_info,
                "educations": edu_info,
                "livings": livings,
                "contact_info": contact,
                "basic_info": basics_info,
                "nicknames": nickname_list,
                "relationships": relationship_list,
                "family_members": member_list,
                "quotes": quote_list,
                "bio": bio_list,
                "crawl_date": dt_object
            }
            sleep(10)

        sleep(3)
        self.driver.close()
