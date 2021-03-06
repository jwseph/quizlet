# /*/ coding: utf-8 /*/

import re


key1 = {

  'あ': 'a',    'い': 'i',    'う': 'u',    'え': 'e',    'お': 'o',
  'か': 'ka',   'き': 'ki',   'く': 'ku',   'け': 'ke',   'こ': 'ko',
  'が': 'ga',   'ぎ': 'gi',   'ぐ': 'gu',   'げ': 'ge',   'ご': 'go',
  'さ': 'sa',   'し': 'shi',  'す': 'su',   'せ': 'se',   'そ': 'so',
  'ざ': 'za',   'じ': 'ji',   'ず': 'zu',   'ぜ': 'ze',   'ぞ': 'zo',
  'た': 'ta',   'ち': 'chi',  'つ': 'tsu',  'て': 'te',   'と': 'to',
  'だ': 'da',   'ぢ': 'ji',   'づ': 'zu',   'で': 'de',   'ど': 'do',
  'な': 'na',   'に': 'ni',   'ぬ': 'nu',   'ね': 'ne',   'の': 'no',
  'は': 'ha',   'ひ': 'hi',   'ふ': 'fu',   'へ': 'he',   'ほ': 'ho',
  'ば': 'ba',   'び': 'bi',   'ぶ': 'bu',   'べ': 'be',   'ぼ': 'bo',
  'ぱ': 'pa',   'ぴ': 'pi',   'ぷ': 'pu',   'ぺ': 'pe',   'ぽ': 'po',
  'ま': 'ma',   'み': 'mi',   'む': 'mu',   'め': 'me',   'も': 'mo',
  'や': 'ya',   '　': ' ',    'ゆ': 'yu',   '𛀁': 'ye',   'よ': 'yo',
  'ら': 'ra',   'り': 'ri',   'る': 'ru',   'れ': 're',   'ろ': 'ro',
  'わ': 'wa',   'ゐ': 'wi',   '〜': '~',    'ゑ': 'we',   'を': 'wo',
  'ん': "n'",   'ゟ': 'yoro', '。': '.',    '，': ',',     '、': ',',
  '！': '!',    '？': '?',    '：': ':',    '（': '(',    '）': ')',

  'ゃ': '~ya',               'ゅ': '~yu',               'ょ': '~yo'

}


key2 = {

  'a': 'ā',
  'i': 'ī',
  'u': 'ū',
  'e': 'ē',
  'o': 'ō'

}


key1_reverse = {

  'a':   'あ',    'i':   'い',    'u':   'う',    'e':   'え',    'o':   'お',
  'ka':  'か',    'ki':  'き',    'ku':  'く',    'ke':  'け',    'ko':  'こ',
  'ga':  'が',    'gi':  'ぎ',    'gu':  'ぐ',    'ge':  'げ',    'go':  'ご',
  'sa':  'さ',    'shi': 'し',    'su':  'す',    'se':  'せ',    'so':  'そ',
  'za':  'ざ',    'ji':  'じ',    'zu':  'ず',    'ze':  'ぜ',    'zo':  'ぞ',
  'ta':  'た',    'chi': 'ち',    'tsu': 'つ',    'te':  'て',    'to':  'と',
  'da':  'だ',    'dzi': 'ぢ',    'dzu': 'づ',    'de':  'で',    'do':  'ど',
  'na':  'な',    'ni':  'に',    'nu':  'ぬ',    'ne':  'ね',    'no':  'の',
  'ha':  'は',    'hi':  'ひ',    'fu':  'ふ',    'he':  'へ',    'ho':  'ほ',
  'ba':  'ば',    'bi':  'び',    'bu':  'ぶ',    'be':  'べ',    'bo':  'ぼ',
  'pa':  'ぱ',    'pi':  'ぴ',    'pu':  'ぷ',    'pe':  'ぺ',    'po':  'ぽ',
  'ma':  'ま',    'mi':  'み',    'mu':  'む',    'me':  'め',    'mo':  'も',
  'ya':  'や',    ':':   '：',    'yu':  'ゆ',    'ye':  '𛀁',    'yo':  'よ',
  'ra':  'ら',    'ri':  'り',    'ru':  'る',    're':  'れ',    'ro':  'ろ',
  'wa':  'わ',    'wi':  'ゐ',    '~':   '〜',    'we':  'ゑ',    'wo':  'を',
  "n'":  'ん',    'yoro':'ゟ',    '.':   '。',    ',':   '，',
  '!':   '！',    '?':   '？',    '(':   '（',    ')':   '）',
  'n':   'ん',    'hu':  'ふ',    's':   'す',

  'kya':  'きゃ',    'kyu':  'きゅ',    'kyo':  'きょ',
  'gya':  'ぎゃ',    'gyu':  'ぎゅ',    'gyo':  'ぎょ',
  'sha':  'しゃ',    'shu':  'しゅ',    'sho':  'しょ',
  'ja':   'じゃ',    'ju':   'じゅ',    'jo':   'じょ',
  'cha':  'ちゃ',    'chu':  'ちゅ',    'cho':  'ちょ',
  'dzya': 'ぢゃ',    'dzyu': 'ぢゅ',    'dzyo': 'ぢょ',
  'nya':  'にゃ',    'nyu':  'にゅ',    'nyo':  'にょ',
  'hya':  'ひゃ',    'hyu':  'ひゅ',    'hyo':  'ひょ',
  'bya':  'びゃ',    'byu':  'びゅ',    'byo':  'びょ',
  'pya':  'ぴゃ',    'pyu':  'ぴゅ',    'pyo':  'ぴょ',
  'mya':  'みゃ',    'myu':  'みゅ',    'myo':  'みょ',
  'rya':  'りゃ',    'ryu':  'りゅ',    'ryo':  'りょ',

}


key2_reverse = {

  'ā': 'aa',
  'ī': 'ii',
  'ū': 'uu',
  'ē': 'ee',
  'ō': 'ou'

}


def hiragana_to_romaji(hiragana):

  return re.sub(r"'(?=[^aiueoy]|$)", '', re.sub('(a[aー])|(i[iー])|(u[uー])|(e[eー])|(o[uoー])|(っ[kstcp])', lambda x: (lambda c: key2.get(c[0], c[1]*2))(x.group()), re.sub('((?<=j)|(?<=sh|ch))i~y|i~', '', ''.join(key1.get(_, _) for _ in hiragana))))


def romaji_to_hiragana(string):

  return re.sub(r"([kgsztdnhfbpmyrwj]?y?|ch|sh)[aiueo]|tsu|[ns]('|(?=[^aiueoy]|$))|[ ~\.,!\?:\(\)]", lambda x: (lambda c: key1_reverse.get(c, c))(x.group()), re.sub(r'([kstcp])(?=\1)|([āīūēō])', lambda x: key2_reverse.get(x.group(), 'っ'), string.lower()))

# おはよう ございます ohayō gozaimasu
# おっちょこちょい occhokochoi
# あたたかくなかった atatakakunakatta

if __name__ == '__main__':

  while True: print(romaji_to_hiragana(input()))
