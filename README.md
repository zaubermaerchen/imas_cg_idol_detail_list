# imas_cg_idol_detail_list
アイドルマスターシンデレラガールズのアイドルギャラリーページから
該当アイドルの公開されている全カードのJSONデータを抽出します。

## 使用法

	python3 idol_detail_list.py -s セッションID カードハッシュID


## オプション
### -s セッションID, --session_id セッションID
ゲームから発行されたセッションID(sp_mbga_sid_12008305)を指定します。

## サンプル

	$ python idol_detail_list.py -s "session_id" "4270223bf3b0fa1fe9ad07050b397f65" | jq
	[
	  {
	    "data": {
	      "card_name": "[聖夜のｷｾｷ]日高愛",
	      "rarity": "5",
	      "cost": "19",
	      "attribute": "cute",
	      "skill_name": "ALIVE ",
	      "skill_effect": "全ﾀｲﾌﾟのﾌﾛﾝﾄﾒﾝﾊﾞｰ及びﾊﾞｯｸﾒﾝﾊﾞｰ上位2人の攻守 ﾗﾝﾀﾞﾑで大～特大ｱｯﾌﾟ",
	      "grow_idol_flag": "",
	      "default_attack": "4460",
	      "default_defense": "4460",
	      "hash_card_id": "4270223bf3b0fa1fe9ad07050b397f65",
	      "alias_name": "聖夜のｷｾｷ",
	      "real_name": "日高愛"
	    },
	    "profile": {
	      "card_id": "1437201",
	      "card_name": "[聖夜のキセキ]日高愛",
	      "card_kana": "ひだかあい",
	      "card_age": "13",
	      "card_from": "876プロダクション",
	      "card_height": "149",
	      "card_weight": "40",
	      "card_bust": "78",
	      "card_waist": "55",
	      "card_hip": "79",
	      "card_birthday": "6月25日",
	      "card_constellation": "蟹座",
	      "card_blood": "O",
	      "card_arm": "右",
	      "card_hobby": "バーゲンの1点買い、金魚すくい",
	      "card_cv": "戸松遥"
	    },
	    "comments": {
	      "comment": "ﾒｪｪｪﾘｨｨｨ､ｸﾘｽﾏｰｰｰｰｰｽ!!!!! ﾌｪｽ､がんばろｰっっっ､おｰ!! こんな大きな会場､久しぶりだもんね｡思いっきり歌っても､うるさいって言われなさそうだし､めいいっぱい､がんばるよｰ!!",
	      "comments_my_1": "???",
	      "comments_my_2": "???",
	      "comments_my_3": "???",
	      "comments_my_4": "???",
	      "comments_my_max": "???",
	      "comments_work_1": "???",
	      "comments_work_2": "???",
	      "comments_work_3": "???",
	      "comments_work_4": "???",
	      "comments_work_max": "???",
	      "comments_work_love_up": "???",
	      "comments_live": "???",
	      "comments_love_max": "???"
	    },
	    "voice": {
	      "comment": "http://idolmaster.edgesuite.net/idolmaster/sound/1437201/b0af939495bef06ceb59664308fd24fa.mp4",
	      "comments_my_1": null,
	      "comments_my_2": null,
	      "comments_my_3": null,
	      "comments_my_4": null,
	      "comments_my_max": null,
	      "comments_work_1": null,
	      "comments_work_2": null,
	      "comments_work_3": null,
	      "comments_work_4": null,
	      "comments_work_max": null,
	      "comments_work_love_up": null,
	      "comments_live": null,
	      "comments_love_max": null
	    },
	    "event": null,
	    "release": "",
	    "trade_prohibition": {
	      "card_id": "1437201",
	      "card_name": "[聖夜のキセキ]日高愛",
	      "from": "2016/12/09/15:00",
	      "to": "2016/12/19/12:00",
	      "limitless_flag": "0",
	      "is_trade_limit": true
	    },
	    "idol_search_param": "keyword=%E3%81%B2%E3%81%A0%E3%81%8B%E3%81%82%E3%81%84",
	    "archive": {
	      "normal": "0",
	      "premium": "0"
	    },
	    "is_exist_archive": false,
	    "is_max_love": false
	  },
	  {
	    "data": {
	      "card_name": "[聖夜のｷｾｷ]日高愛+",
	      "rarity": "6",
	      "cost": "19",
	      "attribute": "cute",
	      "skill_name": "ALIVE ",
	      "skill_effect": "全ﾀｲﾌﾟのﾌﾛﾝﾄﾒﾝﾊﾞｰ及びﾊﾞｯｸﾒﾝﾊﾞｰ上位2人の攻守 ﾗﾝﾀﾞﾑで特大～極大ｱｯﾌﾟ",
	      "grow_idol_flag": "",
	      "default_attack": "5352",
	      "default_defense": "5352",
	      "hash_card_id": "e39015d925db23fa7c4a5fbfeaf09534",
	      "alias_name": "聖夜のｷｾｷ",
	      "real_name": "日高愛+"
	    },
	    "profile": {
	      "card_id": "1537202",
	      "card_name": "[聖夜のキセキ]日高愛+",
	      "card_kana": "ひだかあい",
	      "card_age": "13",
	      "card_from": "876プロダクション",
	      "card_height": "149",
	      "card_weight": "40",
	      "card_bust": "78",
	      "card_waist": "55",
	      "card_hip": "79",
	      "card_birthday": "6月25日",
	      "card_constellation": "蟹座",
	      "card_blood": "O",
	      "card_arm": "右",
	      "card_hobby": "バーゲンの1点買い、金魚すくい",
	      "card_cv": "戸松遥"
	    },
	    "comments": {
	      "comment": "ずｰっと歌われてきた歌には…たくさんの気持ちがこもってる｡ｸﾘｽﾏｽｿﾝｸﾞにも､他の曲にも｡だから､思いを感じて歌わなきゃ｡これは､あたしの歌｡そして…応援し続けてくれた､みんなの歌!",
	      "comments_my_1": "???",
	      "comments_my_2": "???",
	      "comments_my_3": "???",
	      "comments_my_4": "???",
	      "comments_my_max": "???",
	      "comments_work_1": "???",
	      "comments_work_2": "???",
	      "comments_work_3": "???",
	      "comments_work_4": "???",
	      "comments_work_max": "???",
	      "comments_work_love_up": "???",
	      "comments_live": "???",
	      "comments_love_max": "???"
	    },
	    "voice": {
	      "comment": "http://idolmaster.edgesuite.net/idolmaster/sound/1537202/129bbb79f708362598af6bb399b1fdd4.mp4",
	      "comments_my_1": null,
	      "comments_my_2": null,
	      "comments_my_3": null,
	      "comments_my_4": null,
	      "comments_my_max": null,
	      "comments_work_1": null,
	      "comments_work_2": null,
	      "comments_work_3": null,
	      "comments_work_4": null,
	      "comments_work_max": null,
	      "comments_work_love_up": null,
	      "comments_live": null,
	      "comments_love_max": null
	    },
	    "event": null,
	    "release": "",
	    "trade_prohibition": {
	      "card_id": "1537202",
	      "card_name": "[聖夜のキセキ]日高愛+",
	      "from": "2016/12/09/15:00",
	      "to": "2016/12/19/12:00",
	      "limitless_flag": "0",
	      "is_trade_limit": true
	    },
	    "idol_search_param": "keyword=%E3%81%B2%E3%81%A0%E3%81%8B%E3%81%82%E3%81%84",
	    "archive": {
	      "normal": "0",
	      "premium": "0"
	    },
	    "is_exist_archive": false,
	    "is_max_love": false
	  }
	]