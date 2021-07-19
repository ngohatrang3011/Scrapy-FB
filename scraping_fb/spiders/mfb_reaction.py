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

# cookie = "cookie: sb=a75iYNhZ7wizl44PGndgDKZY; _fbp=fb.1.1617786963671.1059209162; locale=vi_VN; datr=Gp3uYIVzw3OzZlSHnc2sVMJO; c_user=100022337169390; wd=1349x657; spin=r.1004114193_b.trunk_t.1626362078_s.1_v.2_; presence=C%7B%22t3%22%3A%5B%7B%22i%22%3A%22u.100012249136842%22%7D%2C%7B%22i%22%3A%22u.100005453856197%22%7D%5D%2C%22utc3%22%3A1626417408813%2C%22lm3%22%3A%22u.100012249136842%22%2C%22v%22%3A1%7D; xs=21%3A52dFhnqzMvAabA%3A2%3A1626256369%3A-1%3A6382%3A%3AAcUb80NTZZOuLBLRiJaDmmyjm8UfFl64YkjdGfYVwuU; fr=12OmUIypE3gw3LJUh.AWVUe_1tvAOZNVTm4Ub5rmq0V0o.Bg8TGR.2t.GDx.0.0.Bg8TGR."


# class MfbReactionSpider(scrapy.Spider):
#     name = 'mfb_reaction'
#     allowed_domains = ['m.facebook.com']

#     # for p in list_post:z
#     start_urls = ['https://m.facebook.com/AbbieOh.Vietnam']

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
#         list_post = [1261420020967676,
#  1258767734566238,
#  1258485707927774,
#  1255462011563477,
#  1254143481695330,
#  1253462168430128,
#  1251553038621041,
#  1251550731954605,
#  1250748905368121,
#  1250694378706907,
#  1249456088830736,
#  1247567395686272,
#  1245614292548249,
#  1244965192613159,
#  1237396526703359,
#  1235853743524304,
#  1234652376977774,
#  1231122497330762,
#  1230295480746797,
#  1229800677462944,
#  1229198167523195,
#  1228575194252159,
#  1227961690980176,
#  1227312514378427,
#  1226470797795932,
#  1225892234520455,
#  1225267684582910,
#  1224603477982664,
#  1224026114707067,
#  1222797974829881,
#  1222135098229502,
#  1221579874951691,
#  1220252591751086,
#  1219630831813262,
#  1218998425209836,
#  1218447868598225,
#  1218338175275861,
#  1217837511992594,
#  1217111862065159,
#  1215226975586981,
#  1214739925635686,
#  1214639855645693,
#  1214102179032794,
#  1213496735760005,
#  1212168105892868,
#  1211494192626926,
#  1211481959294816,
#  1210856899357322,
#  1210246856084993,
#  1210248982751447,
#  1209130899529922,
#  1208470212929324,
#  1207910942985251,
#  1207349116374767,
#  1206679003108445,
#  1205985536511125,
#  1205304833245862,
#  1204677813308564,
#  1204026070040405,
#  1203556600087352,
#  1202831180159894,
#  1202176543558691,
#  1201607500282262,
#  1200893810353631,
#  1200342463742099,
#  1199674570475555,
#  1198943120548700,
#  1198357940607218,
#  1197696847339994,
#  1197100917399587,
#  1196582264118119,
#  1195790587530620,
#  1195238257585853,
#  1194541814322164,
#  1193848254391520,
#  1193160481126964,
#  1192531304523215,
#  1191904221252590,
#  1191184464657899,
#  1190781498031529,
#  1189891401453872,
#  1189267418182937,
#  1188621284914217,
#  1188026064973739,
#  1187375141705498,
#  1186839898425689,
#  1186173401825672,
#  1185292265247119,
#  1184706888638990,
#  1183903658719313,
#  1183181248791554,
#  1182463692196643,
#  1181859535590392,
#  1180460425730303,
#  1179807305795615,
#  1179360119173667,
#  1178482039261475,
#  1177885959321083,
#  1176765156099830,
#  1175857476190598,
#  1175842489525430,
#  1175331226243223,
#  1174538902989122,
#  1174538189655860,
#  1173844729725206,
#  1174536709656008,
#  1173288079780871,
#  1172159563227056,
#  1172050953237917,
#  1171093256667020,
#  1170757846700561,
#  1170722620037417,
#  1168966293546383,
#  1164794870630192,
#  1168548070254872,
#  1164787737297572,
#  1163296580780021,
#  1162747960834883,
#  1162662694176743,
#  1162080857568260,
#  1160187874424225,
#  1159472684495744,
#  1158894917886854,
#  1158426014600411,
#  1157791237997222,
#  1157009654742047,
#  1157007588075587,
#  1156438844799128,
#  1156424164800596,
#  1155614944881518,
#  1155092681600411,
#  1154434361666243,
#  1154418545001158,
#  1154414968334849,
#  1153879511721728,
#  1153129648463381,
#  1152534268522919,
#  1151822021927477,
#  1151358895307123,
#  1150108862098793,
#  1150106978765648,
#  1149534078822938,
#  1149417612167918,
#  1148728102236869,
#  1148725262237153,
#  1148714722238207,
#  1148573395585673,
#  1147972732312406,
#  1147970568979289,
#  1147365615706451,
#  1147289155714097,
#  1146502429126103,
#  1146498449126501,
#  1146262359150110,
#  1145932205849792,
#  1145342159242130,
#  1145112492598430,
#  1144726732637006,
#  1143920492717630,
#  1143365216106491,
#  1142672692842410,
#  1141852056257807,
#  1141084803001199,
#  1141078933001786,
#  1140535169722829,
#  1137549426688070,
#  1139590093150670,
#  1137547330021613,
#  1137543870021959,
#  1137553483354331]
#         for p in list_post:
#             # REACTION
#             link_post = 'https://m.facebook.com/story.php?story_fbid={post_id}&id={page_id}'
#             link_url = link_post.format(post_id=p, page_id=454894214953598)
#             self.driver.get(link_url)
#             sleep(5)
#             try:
#                 reaction_page = self.driver.find_element_by_xpath("//div[@class='_45kb ufi']/div[@class='_52jh _5ton _45m7']/a")
#                 reaction_page.click()
#                 sleep(5)
#                 # self.driver.get(link_reaction_url)
#                 count_reaction = 0
#                 while True:
#                     try:
#                         load_reactions = self.driver.find_element_by_xpath(
#                             "//div[@id='reaction_profile_pager']/a")
#                     except:
#                         print("last reaction")
#                         break
#                     count_reaction += 1
#                     print(count_reaction)

#                     load_reactions.click()
#                     sleep(5)
#                 resp_reaction = Selector(text=self.driver.page_source)
#                 print(resp_reaction)
#                 links_reaction_xpath = "//div[@class='_4mn c']/a/@href"
#                 # print("links = " + links_xpath)
#                 links_profile_reaction = resp_reaction.xpath(
#                     links_reaction_xpath).getall()
#                 # print(links_profile)

#                 names_reaction_xpath = "//div[@class='_4mn c']/a//strong/text()"
#                 # print("names = " + names_xpath)
#                 names_reaction = resp_reaction.xpath(names_reaction_xpath).getall()
#                 # self.driver.execute_script(
#                 #     "window.scrollTo(0, document.body.scrollHeight);")
#                 # sleep(1)
#             except:
#                 pass
#             for link, name in zip(links_profile_reaction, names_reaction):
#                 yield {
#                     "post_id": p,
#                     "link_profile": "https://www.facebook.com"+str(link),
#                     "name": name
#                 }

#             # self.driver.execute_script(
#             #         "window.scrollTo(500, document.body.scrollHeight);")
#             # sleep(5)

#         sleep(2)
#         self.driver.close()
