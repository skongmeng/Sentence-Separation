import jieba
import langconv
import langid

word = [x for x in jieba.tokenize("输入简体,I Love You")][0][0]


class sentence(object):
    def __init__(self):
        self.s = ""
        self.token = []
        self.chinese = []
        self.english = []
        self.other = []
        self.symbol = []
        self.translated = []
        
    def split(self,input_s):
        self.s = input_s
        self.token = jieba.tokenize(self.s)
        for t in self.token:
            if not t[0].isspace():
                if t[0] in ',，"\'‘’“”#@%<>《》{}【】[]。，！!?？' :
                    self.symbol.append(t)
                else:
                    lang = langid.classify(t[0])[0]
                    if lang == "en":
                        self.english.append(t)
                    elif lang == "zh":
                        self.chinese.append(t)
                    else:
                        self.other.append(t)
                    
    def Traditional2Simplified(self,input_s):
        return langconv.Converter('zh-hans').convert(input_s)              
    
    def translate(self):
        if self.english:
            for e in self.english:
                self.translated.append(self.translate_a_word(e))
    
    def translate_a_word(self,e):
        
        #TODO:翻译
        return "翻译文字"

s = sentence()
s.split("哈哈哈 Good Morning")
print(s.english)