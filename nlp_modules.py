import MeCab
import mojimoji
import numpy as np


#MeCabでtextの形態素解析
#一旦はneologedの辞書で解析
tagger = MeCab.Tagger("-d /usr/lib/x86_64-linux-gnu/mecab/dic/mecab-ipadic-neologd")
tagger.parse("")

def text_to_word(text, stopword_pass="./stopwords/Japanese.txt"):
    """
    Tokenize texts with MeCab neologd
    
    Parameters
    ----------
    text: str
        text to tokenize
    stopword_pass: str
        path of stopwords
        
    Returns
    -------
    basic_words_list: str
        tokenized and basic text
    
    """
    
    #stopwordのリスト作成
    stopword_list =[]
    with open(stopword_pass, "r") as file:
        lines = file.readlines()
            
        stopword_list = [stopword for stopword in lines if stopword.strip()]
    
    #mojimojiで全角数字、英字を半角に統一。大文字もすべて小文字に統一する
    text = mojimoji.zen_to_han(text, kana=False).lower()
    #解析
    parse_text = tagger.parse(text)
    
    #ここから解析したものの原型などを取り出して抽出していく
    basic_words_list = []
    
    #各単語の解析結果ごとにsplitしていく
    split_parse_text = parse_text.split("\n")
    
    for parse_word in split_parse_text:
        #\tで区切り、表層と品詞の情報に分ける
        split_parse_word = parse_word.split("\t")
        surface_word = split_parse_word[0]
        
        #最終行はEOSのため、終了させる
        if surface_word =="EOS":
            break
        else:
            #品詞が動詞、形容詞の場合、原形を格納
            morph_info = split_parse_word[1]
            morphs = morph_info.split(",")
            #品詞情報
            morph = morphs[0]
            #原型
            #原型は品詞情報の後ろから3番目
            basic = morphs[-3]
            
            if morph == "記号":
                continue
            elif morph in("動詞", "形容詞") and basic not in stopword_list:
                basic_words_list.append(basic)
                    
            elif morph =='名詞' and basic not in stopword_list:
                basic_words_list.append(basic)
        
    #最終的にまとめたものを半角スペースでjoinし、リストで返す
    basic_words_list = " ".join(basic_words_list)
    return basic_words_list