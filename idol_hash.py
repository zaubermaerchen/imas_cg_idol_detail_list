# -*- coding: utf-8 -*-
import argparse

IDOL_HASH = {
    "島村卯月": "0dabb79ff64691111a0abae2ffed01ce",
    "中野有香": "46c53f722dfaa05a4f4d36b7821a686a",
    "水本ゆかり": "5a32b53f2943c5c7b76b18c0e098f400",
    "福山舞": "9e4c72332c4881ae0bdc40ed2ec88c89",
    "椎名法子": "2c27422ff05ee7bb687d23d68b8e5437",
    "今井加奈": "ed6aeeec0997ee6943d1791c228c1ec7",
    "持田亜里沙": "bb74192d2815e42c51cbf484f0e7c57b",
    "三村かな子": "9934868123e14bccac84dfb85f7ecd8a",
    "奥山沙織": "2bc8b92d3444429e10e29e7fd056aaab",
    "間中美里": "729dbe34998bc4505ec54c4a91d6274c",
    "小日向美穂": "bef9093335fbcbe9e92a41d2d68a206d",
    "緒方智絵里": "e0ac4f8b1faf39c137d2bef65559b5f5",
    "五十嵐響子": "fb3b173c49703071b4dbdd5ed424640c",
    "柳瀬美由紀": "64b53f490afd702be31de96b5ae28e36",
    "櫻井桃華": "1cefdef7df7c14eca803910b67e61dfc",
    "江上椿": "1b52629f3463de549e9e776fb9be9c73",
    "長富蓮実": "4d2e995945e069c1c219d6c6b45edfce",
    "横山千佳": "33e0fe9d3980f8fcc0146acf93b1527c",
    "関裕美": "a62ddac0bbdf7507192e5ed73698a4be",
    "池袋晶葉": "bd75cdaf7d77b14fca1d6f6c65dc88da",
    "太田優": "54ae8e0c640c6a7b14cb72b9395ea0fd",
    "棟方愛海": "668df5f627110fb638fed98ab6f0efdb",
    "藤本里奈": "d2e5c0c476cfc344fce7fe03c8c9a4fb",
    "大原みちる": "6b068f0f0e900fe2dd9026fc45e69c73",
    "遊佐こずえ": "45e99d9c3367c228d33f71058dd2f738",
    "大沼くるみ": "28789186bef61a4dcdd8eff8ef59fe7f",
    "一ノ瀬志希": "dad249d2193e48fede1efb6b86ce152f",
    "前川みく": "eb2571c3f125aa3fcadb1468b6a4dbee",
    "赤西瑛梨華": "2cd48b54401ff3ef8a81a753318705a9",
    "松原早耶": "510b48227148c9164ac281f46083d2c5",
    "相原雪乃": "fe1ec011929547cd07d17bfa91432bd3",
    "宮本フレデリカ": "1593bfefaa649ce28d0b586bbcee2c81",
    "小早川紗枝": "3d5441d51a3d93214ed9798cdb5b0fe1",
    "西園寺琴歌": "20867159bc2a902527f5dc0efa76d68b",
    "双葉杏": "f6db9a4a1e364bf7da838ed3dce77f97",
    "楊菲菲": "0b9a4389717199d57e7001d411c67791",
    "桃井あずき": "4efc876705241a31f7ecf57ae3dc8ef4",
    "涼宮星花": "e25bfc4f11de8a6ae9c2039c90c21348",
    "月宮雅": "7c175ee387814c3af476068126e9a693",
    "兵藤レナ": "fc97ba28d3a4f9ba0863b15761df3403",
    "道明寺歌鈴": "6c298af445eea9e1b73482704eec4924",
    "高槻やよい": "73221b45dc3a76f73b08bb8854191273",
    "菊地真": "7c3cc9c1c697ecc6b62dc2d5a835f534",
    "我那覇響": "f8f4c3be1b401f47318d440f2bcf9bec",
    "柳清良": "0b94e4097c16bce2c2579da0914234c5",
    "天海春香": "85d13609464513894fdecb0baad54c2a",
    "井村雪菜": "e45c0c3027d05bf557aae92dadc353b8",
    "日下部若葉": "98daacfc83511eb95974e557aaf84caf",
    "榊原里美": "0a2cb7263e4bab320935782c987b0ed1",
    "輿水幸子": "c3100ee880e230589036b29a80d7dce3",
    "安斎都": "a5a7e280731764ee1d3df5391bd87d43",
    "浅野風香": "fa074d5e6fd70b950c77ecb6d0156075",
    "大西由里子": "380a7a645fe50c52773fd2fceb026002",
    "安部菜々": "edd3438bd612a333a76edaea0ff73fe7",
    "工藤忍": "1a31c15fa7189284f9df6258d5382de2",
    "栗原ネネ": "9d98993861fb0959c1f26b591db03133",
    "古賀小春": "f9947ff6fc9c5c580c0f6382c56cccbf",
    "クラリス": "15bf1c0a280683642827f5f4ef6463fa",
    "佐久間まゆ": "34b22a25affabfd3160d7d70488f7e0d",
    "村松さくら": "cca70f56774507cb696b0e85846a8786",
    "丹羽仁美": "3fed05567d232be4af746b2de681d024",
    "原田美世": "2e36224b97dfdd2701e9803ee789f47d",
    "白菊ほたる": "131e22dcecbfcd1842e42ba64311950f",
    "早坂美玲": "bad5f37bdb10a4526a1783e377e160ff",
    "有浦柑奈": "6a5d8d6eb2f6d9d734794f521447d592",
    "乙倉悠貴": "5d22c46f3d70b063510b1afdb41faca1",
    "日高愛": "4270223bf3b0fa1fe9ad07050b397f65",
    "渋谷凛": "8f88bb5ffa40b4935ef04257ba4ba0d1",
    "黒川千秋": "4035fd883093767b28d2a539d774e094",
    "松本沙理奈": "a30783d170b758c118fd545eec28dfa9",
    "桐野アヤ": "f8edf47fb60a0d249bb979d68211b8be",
    "高橋礼子": "0a608619d8933f94dbf234b16a738cc4",
    "相川千夏": "24db8e0436418b7e45715d6330a49056",
    "川島瑞樹": "40a601df9bea01621e36d1ab686f16e3",
    "神谷奈緒": "4c54b931268517a3746f98911166b113",
    "上条春菜": "67f718dfb03e338ba76c322b1970258e",
    "荒木比奈": "15b30810c788f120586bc0916134b1da",
    "東郷あい": "74aa09925c2e9f3dfa27f9d6c9043737",
    "多田李衣菜": "914e2e1efbc1f05e987772cc5c925722",
    "水木聖來": "abc8481a5c280fa3b9f0e214880ee10d",
    "佐々木千枝": "f0c2444b0d413beed830240f57990e26",
    "三船美優": "c89d54609371818e71836d519b3d404f",
    "服部瞳子": "35b09bc982525959986d255eba92f6bf",
    "木場真奈美": "046cd353c0361020d544e2946f024908",
    "藤原肇": "50f53b8bae68c432456604aa421dfce9",
    "新田美波": "2bada7af6dfab066132d050923a513eb",
    "水野翠": "b72a61e46933108a7e0ecbcd37bcc461",
    "古澤頼子": "a93f91d99fbc2f134011e4fdf38e49bb",
    "橘ありす": "4712d374c30554718ed4dcafc5edfd1c",
    "鷺沢文香": "cf0f5af872286b4401c644ad570b1401",
    "八神マキノ": "3ae96bc5997dd574e80cdcac87d694c2",
    "ライラ": "3fd787fa963d607b8b8a5686e59f5b29",
    "浅利七海": "fbd7e64d96b438e45db27f0392b08a06",
    "ヘレン": "7213b5c8bf9bcf2661deeed916c04839",
    "松永涼": "259ea6a1a4bfe54feafe3adea84e09fc",
    "小室千奈美": "052c63f721faba1ce3c0ee0b14c45bb4",
    "高峯のあ": "fa2dec52d070ce84f31fe991bd02a9f4",
    "高垣楓": "1f62eb063030ed5083b0e7826245d3af",
    "神崎蘭子": "b7999fc204ef28323b6b656f66d46c42",
    "伊集院惠": "cdd97d8779d5ae35b16aa32bf8172e9f",
    "柊志乃": "e8a68de320c6b9d699b376a3893c9eeb",
    "北条加蓮": "d3e95e1ca3c7b346535ad23e8619ec7e",
    "ケイト": "583f455902cb4a78514d6eae2037e178",
    "瀬名詩織": "fff13e1315d12b403dc3d4e0d29f55eb",
    "綾瀬穂乃香": "86972ac887ef7cdbd493b5c04cdfd8ae",
    "佐城雪美": "ea5f708af5590fa7d0ae03018ef7c4fd",
    "如月千早": "6266f471377bc1698b58ddd4638ead09",
    "三浦あずさ": "70716895c47fcf16e1441bb913c05bb8",
    "秋月律子": "30a17a9dccef3c222df1abb5ffcd7a01",
    "四条貴音": "ecc6dd0013d9d3d8ae24947d77a78192",
    "篠原礼": "0279e0bfe3a06fed6d20b88fea031a7a",
    "和久井留美": "b73e3bd3f986371ca390c06539f30f2e",
    "吉岡沙紀": "0f37976821af0722871ecf50938c7ddf",
    "梅木音葉": "8b7fce105c3d588ac3f32396be6d63a9",
    "白坂小梅": "5fe1faaee0a52e41f24eea585a682df5",
    "岸部彩華": "c73b4dc40685bc50d331c9f32d1b91fb",
    "氏家むつみ": "9cdd818a009f19eab8c73cc845175ee6",
    "西川保奈美": "1458f727e92427dcc643e35e6e09eb2e",
    "成宮由愛": "b9c6ac643c09462bf81ce0377506d23c",
    "藤居朋": "ada1f3044f16789d41715c19836867d2",
    "塩見周子": "e44e7611282f6c57fea4ab3fc18d6519",
    "脇山珠美": "e679dff816d61f7dde0816dd34799270",
    "岡崎泰葉": "b57af23a2c131cc8b45dd49a20f76df0",
    "速水奏": "e50a31a7e529103da461ae20d1da2140",
    "大石泉": "26a9c568028c41a7a3d8b6877284ab46",
    "松尾千鶴": "5868502dd8fba8f476fdbc8db146dbb8",
    "森久保乃々": "5e2ce56ce241f77692f5ba6723149452",
    "アナスタシア": "a0104e1ecbb0a22937e3465955d57a8e",
    "大和亜季": "bdd75aa4670e84394fa074885329d353",
    "結城晴": "dfa875a32faa00241a4fbe09310f9c7f",
    "望月聖": "45979186701f234bab59226a89c062aa",
    "二宮飛鳥": "4631474fd525ac81e51808b0bface6a2",
    "桐生つかさ": "dc80aeb410e6c893f6af62cc1ffe68f3",
    "鷹富士茄子": "d7dec3c58513c892ae28ce692f1d9c06",
    "水谷絵理": "addeb97fac43f59ea040b91102e7a6fd",
    "本田未央": "3a15a87af190354ae89fca368b35b69e",
    "高森藍子": "25ea7fdd66fc6bd8e7209a4c0d2ba00c",
    "並木芽衣子": "dd7b4d4e1769b447ee6fc98e317fb666",
    "龍崎薫": "6bd01496d9b00da9563c7e92b6a40257",
    "木村夏樹": "0534bded8c74fa792bde6f3c5692c187",
    "松山久美子": "7674301daa6c75a7321b726f9571ead2",
    "斉藤洋子": "a264ec914168a4e0fa2be2774b4213f5",
    "沢田麻理菜": "52a617fd8f60c1aec0b3d22d3cb1c944",
    "矢口美羽": "d7eb1b97b7cc5d256ceb95118ffae977",
    "赤城みりあ": "6ef2cd5ef498c7caaea87f7d89340110",
    "愛野渚": "63fd3fcbc361ec10820d32bf513be16e",
    "真鍋いつき": "b209c422b7346f1d4d69feda95318a5f",
    "大槻唯": "1515860fd22175a20c99d8007cf8faae",
    "姫川友紀": "70e2c81b06c8865ca2b615df8ee4ff93",
    "喜多見柚": "76e94c283b186a3461922f4ec21881ea",
    "上田鈴帆": "d20b8ca340a2b6ee42797c966f3a79b3",
    "海老原菜帆": "f11481993da76a38d7f289c35cae41f5",
    "及川雫": "66fbc3ffdc1d467d4656be4e6a806c8d",
    "小関麗奈": "95dfef96c030c77201ff9ed0faa2077f",
    "衛藤美紗希": "ce41501e26f10c602104c8ea99058fac",
    "メアリー・コクラン": "886e0e6ddf996f029d572480ab02dd81",
    "星輝子": "f07c10e7c7e68491371b5c0b6fcbf1a6",
    "片桐早苗": "b87dd23cc34603944cd75e87db7435d8",
    "堀裕子": "c55d799ec6a7189b86c2c61309ff705e",
    "西島櫂": "90e1a482a68770c0117ff910db7209c2",
    "的場梨沙": "d95254e127a889746034022f82cb5798",
    "財前時子": "d1aa3bc716ff2f22ebf41c1fe9b83266",
    "依田芳乃": "ddf7d3e8d751523496c1bb75a1aa2124",
    "相葉夕美": "af64f16df0293b28f4bd8fd8e213b98a",
    "野々村そら": "bb90dd3425c2e096e9b48a928e734b8b",
    "浜川愛結奈": "7fa02e42c440b57785448072345ef8e0",
    "若林智香": "bf61ef00c0f50870767799b93134aed8",
    "城ヶ崎美嘉": "73eea87bdec62f29de318e50e84f021d",
    "城ヶ崎莉嘉": "959bc006631151106b824edd21901161",
    "仙崎恵磨": "9ffc7c24c1e76bcb922e7b8c1b40fd66",
    "日野茜": "2ba9aa6bf49a8d75a1cf6ae3a131de74",
    "諸星きらり": "e36b10a6274efaa7836e5b54f9a47ffa",
    "十時愛梨": "2af54b80c9be9ffde43904089069d877",
    "ナターリア": "f382a774439acb0a89167e8d2923b630",
    "相馬夏美": "df8b4a9675f16bdc8379a8e5f59a20ad",
    "槙原志保": "631512ff6dcc396969055e90d1430a6d",
    "萩原雪歩": "e01a1807c67d2fc57825c3acbb06bb0f",
    "双海亜美": "c161cb226474f58f3393e3d6aabfc9b2",
    "双海真美": "421870a18b78ade223c811fe38edf51e",
    "星井美希": "0fd395f1fae53b17c20854465439ca1d",
    "向井拓海": "20f58f004dad13ba670869c921dc32b9",
    "水瀬伊織": "5d06736b102de0b7c12dc2ff98d00eec",
    "市原仁奈": "461c0f642b5623fcd0df84af1de98fc7",
    "杉坂海": "6edab62ef4c1db15158c13d522310985",
    "喜多日菜子": "35ed8cc4e33cec53aea016cb9e2f0f22",
    "北川真尋": "ded225525d77bc5e164da6ec41d0342e",
    "小松伊吹": "981843c62010419ba465420262c9550f",
    "三好紗南": "74a5d336821a3ccbb0e27083910eb4a2",
    "キャシー・グラハム": "b3484b86731fa47b0a59f2d1fb3af249",
    "難波笑美": "462788ef215a343a2f7ea3cdf5a79fd3",
    "浜口あやめ": "ca56d3f1c3dfddc86c3e2d5c12c12747",
    "村上巴": "52a9739a10a91ce69139bb28d742e99e",
    "土屋亜子": "84775bd2804d19b99d77eddeaa86a02c",
    "首藤葵": "43868973b8854862d7c02d14e3c03740",
    "冴島清美": "697e19df704f2ef4b9aca8fb57aa39d2",
    "南条光": "8e9bb5d91c1612e5a4962aed94f45a78",
    "佐藤心": "d9a0ec5b2f49514b8f6fdbc2b3771f44",
    "イヴ・サンタクロース": "f8c5c2664ca76f4aa84b267300290d54",
    "秋月涼": "74bfb36578411126f56d04baeb48212d",
    "トレーナー": "a398078875ab4c504e9a1bf8881f1611",
    "ルーキートレーナー": "9d8f7ddf9814571ec92baa652f20ead5",
    "ベテラントレーナー": "b0fca5a125b526c755eeec59253e3bb3",
    "マスタートレーナー": "24d5423d9fe8deb825e29b8a516d39de",
}

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("name", help="target idol name")
    args = parser.parse_args()

    print(IDOL_HASH.get(args.name, ""))