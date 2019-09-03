

def str2cookie(st):
    if cookie[0:6] =='cookie':
        st = st[8:]
    c2s= st.split(';')
    dct= dict()
    for cs in c2s:
        kv=cs.strip().split('=') 
        print(cs,kv)  
        dct[kv[0]]=kv[1]

    return dct
cookie='cookie: l_n_c=1; _xsrf=c6c4e2e3b4af4cc7384c9af60cccb6a0; n_c=1; d_c0="AHClW7TZSw-PTmxejFyGN6ggtOz941zFCuY=|1555568272"; _zap=79fd394e-0e23-42ef-b38e-582c67f6131a; z_c0="2|1:0|10:1555568559|4:z_c0|92:Mi4xQ2RseEFBQUFBQUFBY0tWYnRObExEeVlBQUFCZ0FsVk5yMldsWFFDSVF1LVJHUEJqS1pETmwwV2tQbC1DNW1oZUdB|bb0532822c003ff65b32302426d9aac01b1534d41e29d745c9c5c2ddf0d5949e"; _xsrf=9W0HX4qil3rcNzPWzeslbdHtboqV3HNs; __utma=51854390.478959437.1561706276.1561706276.1561706276.1; __utmc=51854390; __utmz=51854390.1561706276.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmv=51854390.100-1|2=registration_date=20140809=1^3=entry_date=20140809=1; tst=r; tgw_l7_route=66cb16bc7f45da64562a077714739c11; q_c1=13eac2b1a07d4b47a89ce2f37badc6a9|1567503563000|1555568263000'
print(cookie)
dct = str2cookie(cookie)
print(dct)
cookie2 = 'bid=XZDtANxJUjY; douban-fav-remind=1; __utmc=30149280; __yadk_uid=O7AQLTnnS0G6q8jvSTOfgggoxxlsv9bJ; trc_cookie_storage=taboola%2520global%253Auser-id%3D1485977d-ae01-4b3b-9396-7bc208206aec-tuct3b6aab6; ll="118281"; push_noty_num=0; push_doumail_num=0; __utmv=30149280.10030; _pk_ref.100001.8cb4=%5B%22%22%2C%22%22%2C1567503691%2C%22https%3A%2F%2Fcn.bing.com%2F%22%5D; _pk_ses.100001.8cb4=*; __utma=30149280.2011835486.1562924812.1567496036.1567503697.5; __utmz=30149280.1567503697.5.4.utmcsr=cn.bing.com|utmccn=(referral)|utmcmd=referral|utmcct=/; _pk_id.100001.8cb4=558f2fab2bb26ffa.1562924810.5.1567504681.1567496102.; __utmt=1; __utmb=30149280.2.10.1567503697; dbcl2="100305619:YqT5QAr3FfU"'
dct2 = str2cookie(cookie2)
print(dct2)