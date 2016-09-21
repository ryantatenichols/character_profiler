# -*- coding: utf-8 -*-
classes = {
#    'null' : (''),
#    'ignore' : (' ','\n','\r','\t'),
#    'cc1' : ('易','*'),
#    'cc2' : ('禽','*'),
#    'stopwords' : ('#@'),
#    'delimiters' : ('。'),
#}

    'ignore' : (' ','\n','\r','\t'),

    'delimiters' : ('。'),
    
    #'stopwords' : ('#@','，','、','「','」','：','；','『','』','《','》','，','、','「','」','：','；','『','』','之','不','也','以','而','其','為','曰','者','子','有','於','十','則','無','所','故','三','二','一','是','與','夫','可','五','將','使','何','至','四','矣','自','此','太','謂','如','乃','百','皆','乎','于','在','非','六','諸','必','然','若','及','未','萬','吾','焉','我','復','千','亦','九','七','方','多','西','足','又','高','內','當','去','北','來','氏','外','同','受','反','常','過','后','作','因','雖','里','請','女','右','敢','前','易','求','說','左','起','會','定','通','對','哉','難','稱','屬','宜','聽','終','遠','盡','異','進','初','甚','本','止','興','耳','廣','益','應','還','絕','往','己','固','首','由','共','徒','任'),
        
        'stopwords' : ('#@','，','、','「','」','：','；','『','』','《','》','，','、','「','」','：','；','『','』'),
        
        'stoplisted_di' : ('惠帝','少帝','文帝','景帝','武帝','昭帝','宣帝','元帝','成帝','哀帝','平帝','更始帝','光武帝','章帝','和帝','殤帝','安帝','順帝','沖帝','質帝','桓帝','獻帝','昭烈帝'),
        
        'stoplisted_tian' : ('天下','天子','天地'),
        
        'standalone_di' : ('帝', '$$'),
        
        'standalone_tian' : ('天', '^^'),
        
        'reduced_deity' : ('仙','妖','魅','鬼','神'),
        
        'reduced_gods' : ('天','帝'),
        
        'reduced_punishment' : ('刑','坐','完','尸','廢','懲','拶','枷','法','治','箠','箈','耐','誅','讞','辜','阱','髡'),
        
        'reduced_reward' : ('償','勞','胙','賞','賜','酬'),
        
        'ubc_emotion' : ('安','欲','情','乐','喜','急','忙','恐','惊','爱','怒','恶','苦','怕','欢','感','忧','萧','恨','惧','怨','患','悦','哀','虑','惜','痛','悲','怜','烦','畏','愁','慌','慕','戚','忌','困','悄','悔','嫌','羞','闷','欣','恼','厌','恤','寂','匆','恚','愧','愤','惨','惶','恋','骇','惭','恍','羡','悠','怼','惮','恳','忿','疼','闵','畅','僖','慨','妒','悼','恸','忻','栗','愕','禧','讶','兢','嫉','怅','嗔','歆','憾','懊','怡','娱','瞿','竦','厄','恺','忝','诧','逍','诟','怖','寞','怏','憎','窘','尬','恻','悯','顼','愉','怿','惕','悸','愠','觊','慑','懔','悚','惴','忏','怆','愦','缱','怔','恹'),
        
        'ubc_cognition' : ('知','意','想','思','计','志','觉','记','谋','疑','察','视','略','赏','顾','肯','选','考','算','试','决','识','晓','策','认','判','检','准','智','忘','误','祝','昏','审','惑','择','验','查','惺','悟','迷','辨','阅','痴','拟','伺','呆','搜','诘','测','谟','猜','勘','批','忆','盼','析','猷','译','铨','懂','揆','谛','揣','忖','睬','企','钝','谳'),
        
        'ubc_religion' : ('道','命','宗','礼','圣','仪','灵','祭','寺','丧','佛','祀','祥','占','魂','祠','卜','鼎','禅','祐','坛','奠','祈','菩','佑','魔','飨','卦','祷','衅','魄','俎','偈','咒','祔','刹','醮','氤','傩','迦','禘','筮','瘗','瓒','魃','燔','祜','谶','乩','祧','裟','牺','袈','鬯','祟','禳','俑','妖', '魅', '鬼', '神'),
        # removed from ubc_religion : 天, 帝, 妖, 魅, 鬼, 神, 胙, 法
        # removed from ubc_religion (appear in pun/rew) : 胙, 法
        
        'ubc_morality' : ('正','德','义','真','功','贼','信','忠','罪','善','宜','乱','孝','仁','贤','贵','恩','良','尊','崇','贞','荣','诚','假','奸','恭','惠','邪','夷','勇','凶','坏','蛮','廉','暴','恕','谦','弱','违','谨','佳','慈','豪','贪','淫','贱','慎','优','弊','杰','娇','辉','伪','睿','纯','欺','敦','粗','淳','诈','懿','矗','枉','慧','谅','骄','怠','鄙','诬','毅','哲','乖','颖','骁','咎','侠','伟','僭','孽','虐','懒','恣','俨','孜','谌','忤','婉','歹','侈','陋','谎','侃','懈','慷','愆','戾','诓','惰','悌','亵','忱','獗','婪','慝','窳','悫','谲','龌','愎'),
}