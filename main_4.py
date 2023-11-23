#!/usr/bin/python3
import sys
import requests
from lxml import html
import re

states = [('b0bdbdc7-fc0d-4615-8621-a3d7601e46cb', 'aamxvvqets', []), 
('cdfe9a43-1110-4bf2-90f3-e252f74d3c14', 'afskqpspym', [('fc0972bd-48ba-48be-a0a3-288171dc26ce', 'dilyyvladn'), 
('9b50e29d-2651-42a9-8198-e6d412e00a6a', 'ivxbsviara'), 
('ac38dcd7-571c-4d17-9a44-ec7fefd5e8a0', 'mjqagsgmkm'), 
('c2cc30e6-4ef1-4a20-b3a6-d25f25f363da', 'qwntonxxsn')]), 
('00e12696-0279-4a42-a0e7-bffab4040bf3', 'aitimzybmh', [('8e3b53a5-f8f6-4317-9696-8ed21d08a036', 'dwdxeohafa'), 
('a76f69c6-3668-4343-b305-a246fbd7ddad', 'gouoyllque'), 
('1a1fce0a-92d0-4d1c-a294-c9b1efc3ba15', 'izjhshgugh'), 
('e0d0f3ee-c7f3-401d-957e-2f9792731812', 'zimjvbgjih')]), 
('057e99db-d762-4177-88fe-352025dfb52b', 'apwpixbilb', [('70b68d72-6fe4-4b7f-93d6-c15c3c60084f', 'btzxgfmvdr'), 
('e9af8231-7d84-418f-9455-4b8fe61b57e2', 'vpbglwsuqj')]), 
('4765ba4b-6613-4032-91d9-327086cb48c8', 'bdjlkknlpk', [('d2240ad3-00a4-4f19-a28b-3fb3f56b73a5', 'dunjgpnlae'), 
('1b5f8cf2-250f-48f9-8a2f-ed77dcc3f4b4', 'efubpvvppt'), 
('4bf3bab5-b70d-48b9-81a4-1fc06a22038f', 'fliwcirkgy'), 
('e38c25d3-f6d9-4ab5-b6c8-7f99dabc124a', 'fvqdbnxjpr'), 
('9ac45fd9-5f40-4687-b33e-7a9a59ba04d3', 'uuutylincg'), 
('888e540c-2c5d-4e6e-994d-70533b971f3d', 'uxzvlwqfmy')]), 
('a7f5b29b-f14d-4d5d-b27b-1454bd6a3a66', 'bxahplbltz', [('4783ea41-d8c0-4feb-bf6b-a7ea3ef64fe0', 'ckhhxtuwvk'), 
('a33a66a2-4ea1-4e35-b865-108fa1d60f38', 'emvlergwxl'), 
('dd4d8b5e-552f-4306-9d20-73d8b3ef6cdd', 'kwrxhmuoeb'), 
('6d857716-80c2-4840-a213-545d245cc292', 'liautvhned'), 
('5c08ae2c-0231-47b0-a4d9-3b4f8785d5ef', 'lywyavvydg'), 
('d2325d60-d192-4d52-8c91-f45fcad85f12', 'psmrzeorhj'), 
('496245b9-21ef-47fd-8542-f2f23d345fc9', 'sypsvqvstr'), 
('2006a655-eaac-4b55-a5ab-c2e2c980b3d8', 'yuutfdpudz')]), 
('2c91cb5c-7f3f-473c-8ab6-7824024ea203', 'byhpsrtzar', [('43e9a17b-380c-4829-8b72-02b370746025', 'ofgsrjmymy'), 
('52b821ae-fa0d-4183-8f90-c988a9e5fafc', 'pppgipmqks')]), 
('f9387f00-5d0b-4ff3-9ccb-4169eab21e0d', 'cvebxqmjib', [('6b7348d2-017e-4b9d-9d15-4fde6499fd20', 'cuudvjgueq'), 
('90f50129-8638-4f37-b3de-8967d1e47259', 'ifpvatsnxe'), 
('f8b579c0-87f2-4d8f-9bf4-aa52dc4ce705', 'jfubmzmckj'), 
('50132368-7228-4ced-bee1-4f0ce4ecfaf5', 'ncxycamfrw'), 
('cc6b5e66-5beb-41b2-a41e-c34708927803', 'trkmcvqvul'), 
('7b06363b-2227-42e6-a8ab-5632da52ea36', 'yrnrdxpqin')]), 
('82ca508c-753a-443d-b73e-1097aa8923e5', 'cwjoieiryf', [('6d077352-f7d3-442c-84b5-8c4303b2753f', 'aydqkpoplt'), 
('402985e9-1ae6-48fd-9aae-02e9a37fe726', 'gagkglvwvq'), 
('6f632e79-0854-44ef-8670-83cd77814272', 'mwtuytsesk'), 
('aa9ece61-4d27-4505-9355-312f7fcaf193', 'qprfzwplrm'), 
('a7d2b58c-e7c1-45e5-b469-30a0021151f0', 'rqqneosqus'), 
('ce9559f3-4613-443b-a2e4-73ec67917c68', 'vesrqpbprh'), 
('1a133cf7-3a56-48a9-82db-5fdc9108d438', 'ziylcfzins'), 
('42fff70f-3d66-4c54-96e2-0c2b160aeaae', 'zqjiguxgqi')]), 
('b570c78a-7c9a-4961-9270-48e40f3f6707', 'czkwrlkgzn', [('fbef2c43-82c9-4342-a13b-57e9c4fb54ce', 'bnzogcedjd'), 
('18727d5b-5348-477e-a192-2f0e9d211676', 'bybqaemjgi'), 
('2d669197-3f21-4d9c-b4b8-634080b4912e', 'oomimmaqkv'), 
('ed0aa11b-353c-44eb-bef5-2761d9707896', 'yabpxhayiu')]), 
('fd98ca69-2fca-4a32-b8da-180646f28697', 'dioalwscdp', [('a9404933-507e-41fc-bf87-115122ed6c09', 'qeczfkruvn'), 
('f70628d3-8c3c-44e3-8dad-f3258bccb075', 'rnswzpfbqy')]), 
('6e80edc7-ab42-48cd-bcba-735ac533850f', 'drzbaypbld', [('0cfd48f6-5323-4b42-b708-14d4a3c3bf84', 'iouoyutulk'), 
('8cbc5e0c-d651-4199-9427-9072accf349a', 'kyyzoyxuam'), 
('6fe2bd0d-e16e-495e-ab51-585c11c82d4b', 'laojfrvvnc'), 
('b8f16f9d-5a94-4bee-b7ac-362608e951b3', 'qckruoogoq'), 
('ca21c834-781f-4041-8232-1c2b6e53fd33', 'rfedprrsmi'), 
('e43f8004-792d-4ef0-8add-14b796319fdb', 'xpoorddtbc')]), 
('405faed4-c586-4425-abed-dda2b19045aa', 'duiymwegya', [('9764d486-5566-4904-94c5-25beffcb8b15', 'hnriiagyht'), 
('af89e258-635d-4a49-8323-94215975881e', 'jfcjhddjie'), 
('014adcf7-1af8-477a-82eb-6554772b63de', 'ljpoarxmwx'), 
('3497634d-5f73-4318-80f4-5dfa732a4fd3', 'mojztmgpzb'), 
('bbc1319b-0659-473e-aebc-9a3ad560208d', 'oujvuzeiuv'), 
('6cb28e46-83f1-4b9d-bbcf-ab103e7ead7d', 'prvzgrnryn')]), 
('0b6016ef-d85c-4dff-9b28-4ed4034be886', 'ekdgfwicnq', [('dbcc8db9-b039-4eef-801f-eb4385da005b', 'coygioboej'), 
('44016927-64ea-4f79-acf3-c230377e8137', 'fxyjmelwvr'), 
('2322e003-043d-44fd-af86-f6b18ac3f935', 'rsfmtpuwhm'), 
('dd3c8c2f-f40d-41fb-bf3f-0e328d6fd6a7', 'waibmvajed'), 
('659a284e-91e8-44c4-99f1-a5105546a527', 'xtlszrobir'), 
('682ff11d-fdaa-4ae4-8e96-685b0ba3ccee', 'yjjwohavzr')]), 
('8144f801-eeee-4238-be47-2e66a0a3de5b', 'exnqcpxfle', []), 
('3c009aaf-a468-40aa-a8cb-347d9f2f71d3', 'fauhbqplei', [('2cfb3107-dfc1-439b-8619-5bcf8e27fcc5', 'gkxxhcjadq'), 
('f841280b-3f7d-4b1b-9f98-6021ac0076ec', 'iphfnwwaxc'), 
('68bd9213-a823-4cfa-82a8-f9a8e659abaf', 'pljxudiqku'), 
('32f6a573-828a-417c-834a-f2c8f5c222fc', 'vhgglfzlrs')]), 
('e2249ae9-6b70-4328-bdca-e6c3130866fc', 'finffleetp', [('323f7174-da10-4b76-95ca-1dc6cd5559eb', 'aftrjeyhbf'), 
('251f13a6-ced7-4b38-959b-aba90a062cf0', 'cgrpaqznik'), 
('f463f79a-5512-4800-bac7-d50113f97702', 'dzrdblfacd'), 
('b451d9ec-af7a-4838-b966-63e1b22fcab2', 'gyehkvnqsb'), 
('9e8df396-0288-4481-86c1-f06504fddb10', 'qazwxnekes'), 
('e6598304-ace7-4a30-8fde-019114732981', 'shyreuupdv'), 
('d2d3d437-287f-4d19-8b30-121d45f9b086', 'tcskjcdtgy'), 
('ace06ee9-4fc1-45de-a33c-4cacc97f305b', 'ywypinthyi')]), 
('ed6373a0-79e2-4120-8f27-824a78ba87b2', 'fuyoubgwvn', [('cbcac04c-95c4-4a25-b2e8-f022f7872a6b', 'khjrumolzs'), 
('3592eca6-a3ef-4b0d-b59d-b78dfffc6736', 'razteceeyh')]), 
('a94b8ce2-472a-4fac-9229-e769bf76e91a', 'fxnnlhilwe', []), 
('7d26b473-b874-456d-adc5-4b540850855c', 'fzpnoytxno', []), 
('6503af3c-bce3-432a-a556-a04c0ff737f9', 'gdqvlgbydn', [('7dc4cc3a-baf1-49a8-8a84-4dc46cd68422', 'aftjgierra'), 
('2509e870-08df-4947-bfe2-bafe1c432b62', 'apivokrwhh'), 
('22c6eae2-67a7-432b-8909-0664fce1df73', 'jgqysalezb'), 
('d3da4cca-5644-40e2-863a-c44b891bfd91', 'luwpybusyh'), 
('2408647a-da29-40c3-9087-cf20a5a01f79', 'qhihksjjun'), 
('a8afb57e-8804-45c7-84e3-e01eb0574935', 'seglcufrry'), 
('c54af043-4806-449e-8564-0dac72328b02', 'xkqdnfjhup'), 
('d656d84f-4100-41c0-b34f-1b368a0eea43', 'zttnqhbkbk')]), 
('63719833-9a24-4f88-9f7a-265eaddf923d', 'gjnzisgevj', [('df950d1d-9f45-4c86-8000-5a108e5a31ba', 'bhthtupdla'), 
('e3ba7c27-8adc-4141-802a-a8d8e658410f', 'jysjmkxjnt'), 
('67c6ce83-cffb-44e0-a071-fb02985cc207', 'kablnqkmxp'), 
('fefe3186-f9d5-458f-ae0c-c3e596e9d5f0', 'ljapvnzbjm'), 
('5c616941-b84c-4769-b407-9def824ff227', 'qrchtqnnav'), 
('78e3429e-72ac-45bf-9190-a7c0b2e544c7', 'rqbofxihmq'), 
('347dc5c3-751d-4aad-ba34-c8b9f0db0011', 'ydqqufsxxh'), 
('69e81b6a-78dd-4df8-a75e-56144b04b0c4', 'ytrjliehos')]), 
('7f1b2535-a295-4689-a25a-295764b3d8dc', 'goglfcxfkv', [('298d8c4b-4bcb-4fb2-ad7b-931ebb4fc2bd', 'asfuzkyyyf'), 
('fb3dcd89-b39e-4413-8ef7-97e86ee792d3', 'jyovyjtign'), 
('52108594-6759-41dd-ab6c-e52632d299ee', 'legargvcov'), 
('236af15c-e73e-4a2b-b396-93a707486092', 'uudaqpqayu')]), 
('7bfe62cd-68b0-4bf4-a4b2-b6b52d443150', 'gzabtqyvvy', [('57666b67-92d0-462d-b6b4-09c47cd94f8c', 'ghbcbvcfqm'), 
('759e1770-ebc1-4ec0-aac7-d94371932ce2', 'lyyeksnmfy'), 
('2a30639d-c34e-4d18-b5d5-339ac7fbb6db', 'rfppenmqqt'), 
('29579aa6-b5e7-4ccf-8612-e8a124af4156', 'uoxsuocplp')]), 
('aeb1cc7d-eff9-4531-9f4b-9ba3f3e50e01', 'hkyclzsbny', []), 
('494cf067-5f53-4921-a7e5-d48becab7ae2', 'hmitukdeki', []), 
('5acc8a61-9f82-4f1d-be13-2ba26900a043', 'hpkgejnodn', [('71da1806-9c45-4d83-b9ec-565239f64e56', 'fxhyedfeam'), 
('652a1772-4350-4ea9-ae19-5cde25edfaba', 'mfwkkwrhmr'), 
('d1bfa26c-5f8a-43bc-bd1b-4dfa3030d929', 'twwxarxxjx'), 
('5c5916df-d75b-47cc-8d18-f8d5861e3b5c', 'ufjcvojhgr')]), 
('8d4b246f-83a7-4c3b-9ef7-2a274f051ae7', 'hveaaltrvf', [('2d9a821c-6186-4912-ae2f-efebf4b510ef', 'klwkzaxmbl'), 
('48751abe-f41e-482e-956e-ba5fe5cf1f04', 'qqusmhtepi')]), 
('cb9bd874-2530-47ee-9357-1a4ed09f6f7d', 'invkiqkbiu', [('745b0f42-2387-4b8b-bffb-8ba307699639', 'nmrqipkxja'), 
('6913ddc5-79c5-45c9-803d-68ec6b0cdc75', 'uqprliajuy')]), 
('a70a6d09-dc06-4ad6-832f-17496ed4203e', 'jeggqolhyp', [('43f5dd9a-52ee-4383-9f23-14bd835eff41', 'btxrkyzaje'), 
('2bc6eac7-5b86-4e70-9d80-00bdec3725ad', 'qdztticros'), 
('0e50a81a-2101-4d7f-bed2-50f11cdfaac1', 'srvxkfolbd'), 
('60773260-97ab-4dc0-9511-4e00d87995c3', 'urblbiveit'), 
('8ba6a818-c9ee-4406-99dd-19509fb5a9d0', 'uwgtmwfgya'), 
('46d790d8-8da8-453f-b512-406804083b23', 'vpsuzuikam')]), 
('4e537c6d-62bf-4aa2-9ec0-5bf933540ba7', 'jwlgqsufvd', [('72b7a882-5e33-471c-ba56-aa1169d89edc', 'embrensmmc'), 
('8d338927-0d16-469e-ae52-1421d9ccfaea', 'euqvgjhlaq'), 
('4bfe9fe9-5363-4e66-ba29-03bbf127b3dc', 'hoecsnxnqy'), 
('3a4bd776-1501-43d6-9430-a74b9cf21f14', 'ilocrqrbyd'), 
('4e6ff3f3-da1e-4406-b310-f13598ace4b9', 'mycvxtumso'), 
('be1d16b3-575b-431d-a097-9be74b8470d9', 'ofcvkhuowh'), 
('4712b0c5-31a7-4198-812e-f8f5a7a2fae4', 'thoenqsdiu'), 
('ed0abade-6a4a-4f5f-bf0c-2c00e34aa843', 'uucsgdgweq')]), 
('c218d6e6-74fe-40a9-a602-9384af8d797b', 'kiykwpdehi', [('1de3c0f5-ee5f-48ac-b2e3-ef9cf20eba29', 'dftgpiakvl'), 
('101f6f0f-6867-49c3-ab56-3103065bb244', 'fpmcvpgghh'), 
('5c5e087a-cfea-4228-8595-456b69e345ef', 'hntpfkarzz'), 
('10eb8e06-4d4e-44ad-849f-fe9275ece3fb', 'hrnwhhnusn'), 
('2f0532b5-0667-436f-8c3d-3f61bce75834', 'lijzcvcemd'), 
('f0f967b5-f603-495e-84d4-c74205b8463d', 'oflbmicvzl'), 
('9edc6c75-3b54-495d-85d7-778a06e6f03a', 'tnzijxqrio'), 
('1f506910-bed0-450e-af6f-084718ff0e3c', 'zqrouazhkx')]), 
('7cef7e15-d378-4eaf-bf76-7b1a36fdc64f', 'kjvlrwlpsl', [('acd382a4-22cb-433a-b617-16ad4e05de38', 'fcbdvhrsvp'), 
('06d29374-6596-40f9-943e-02e9f9045d10', 'gqzuiqztef'), 
('bfd74568-878d-4d6d-b13a-1ed23800517c', 'renckfhmkj'), 
('e967fa85-5b65-4d6e-8e1f-3e94808983e4', 'tlihsvxhci')]), 
('6dd4b10d-6d91-4eb4-9508-e2d07b8e955d', 'kthrvrvgxu', [('abb8bc7d-74a9-4b92-aefb-d16cef21291b', 'kdmdjjotan'), 
('38baacb4-dffa-4769-8113-19379b564cb5', 'lpobpapaxi'), 
('221924da-2f4a-4faa-83f2-5c99901c2134', 'tglgiitjbp'), 
('d9ff9fc1-02ee-483e-a20b-d7e9a0132af1', 'zcecvholec')]), 
('b60edd4f-87cc-4109-a1a0-8761582fb398', 'kyopgfeifn', [('0f7313e6-2b3e-4ab3-ab75-bf7716d9e3e3', 'sgscapomez'), 
('65e486f0-5e97-45fa-842a-b96a5996a602', 'spomwzvvha'), 
('37d5becd-6efe-445d-b1a3-c6770e719322', 'wkfiwqhcns'), 
('5681bcd4-c0ac-4cca-a3ba-e055580a9de6', 'xfwsuunmob')]), 
('740f04e2-eb02-4c44-bf15-f5769686c868', 'ladqqfjczh', [('8bedea71-e46d-4616-a2b5-30758173be0b', 'eioguyrlpv'), 
('763c3841-9b9e-42f5-b112-65c72114112b', 'fbnvasihny'), 
('77135157-41f8-4ef9-a170-766be528edc1', 'henvknghqm'), 
('df4d2c7e-b09c-4718-861d-f8da4112576b', 'oytbkptzbm'), 
('5ed1a966-b512-48c8-9fc8-c9b255959bb6', 'rsjgpmzgmn'), 
('6fb387c3-bdee-4c08-b664-6773e2a68539', 'sjijjonmmj')]), 
('d8fd3e11-e2f9-47ab-a84d-2b950d894a25', 'lilkacqorl', [('1ee96b78-a0bb-46da-a14c-58364b96b424', 'eooljwtalw'), 
('5348219d-469a-438a-a08b-4a94e3ea4fe7', 'kzdsxyzlda')]), 
('b474b61b-5f14-4046-894b-3413abe076ec', 'lrcmnmnxpt', []), 
('7232cb92-6e6b-4d06-b600-a1f811e22f44', 'mbdktfwzok', [('d615d972-69a6-4bc3-8228-d19667a495f6', 'dzaiclnupl'), 
('2f26d236-7ab6-4cf6-90ce-c6f429933fe5', 'nlifafbjhi'), 
('6e61d808-a893-45e1-aafc-af1d6a131e30', 'rgwexycopc'), 
('67a1b999-1e42-4c81-8821-f7120e44d015', 'wddhyajouj')]), 
('d2632656-57b6-45da-8c1b-be600d0e7948', 'mgdbtfxrqs', [('63453869-aa28-4bce-a0e7-31746d1eba0c', 'ezabgjdffa'), 
('ad1c8654-8490-4c38-8fbc-aa67bbcb95bf', 'iwvuxywlkf'), 
('7b09ca46-e72e-4e3c-a94c-aa9d48b9bd66', 'jjogwuxekv'), 
('b336be3c-2d3f-463a-9271-3b494bbb33de', 'ndbubhhple'), 
('87b8be12-b481-443b-aa2c-2a4bbf2394a7', 'wvsewryori'), 
('cffb137f-622d-45bf-8aac-da110d9695b1', 'xtxdociewl'), 
('5a8b5544-5b37-41f4-8257-23ff609f8bb7', 'ycsiblkgmz'), 
('20225145-8139-451a-a9b7-58064cf812e7', 'zqqwagmcpv')]), 
('397fbae9-e68e-4c38-b127-7e0167e9f216', 'mllgyosiwf', [('5dba9964-16ea-4200-af0d-cfdabac6dfe0', 'avxlkvefma'), 
('26092345-9d2f-4ac1-bbd6-a2840338479d', 'kvobscojst'), 
('5d8feada-a894-45d7-8c91-6f2992adcc0f', 'lhhhkvytzw'), 
('0819ffa4-9190-4270-9280-325a516b61a6', 'xscxkzgshp')]), 
('9041aec0-da0f-43d7-a1f6-035a88743145', 'mttfhnleky', [('edd8b258-d726-4641-bc5d-4da6a696a89a', 'kivbnytvmf'), 
('9ececc2b-361e-4579-9c57-65cad8614821', 'kjqqnqpmpp'), 
('c74d879a-8f06-4593-a5ce-dc4a16e20c6c', 'oteaplytqw'), 
('711fa0bb-eb8f-4711-833c-b94722609437', 'qvnperaszg')]), 
('e2624137-b6d8-4aa6-8f7a-0f0bf8ffa8de', 'mwinihtrhn', [('08e67900-7855-4ad7-ba68-547cf8ff73b1', 'sefgrahuyd'), 
('bb9db24b-be1e-42a6-868f-d25d909a435e', 'xzebhqcxlu')]), 
('03c5fc4c-73f3-4b10-9c45-6a1442cf535b', 'mxyvnigwgz', []), 
('a9d0e012-4906-49ec-8030-de441a60c74d', 'ngnskgkuoz', []), 
('0c96fe36-f0be-42a7-991d-4af3d93d540f', 'ngsvxxourc', [('c687243f-15a5-4af4-a1dd-2600732f10f9', 'akfsmencvf'), 
('f9eaad03-810b-4200-b855-5a57333e943f', 'enoczmjtpm'), 
('ad6e3afa-fb33-4a03-bfa1-ba8b98455085', 'tijygygdyd'), 
('15a09d7c-095b-4dcc-8028-18e840fd5761', 'tjdvjbiizt')]), 
('6c7a1c86-6f0e-4917-99b0-2cd08e6de754', 'nilnhafmke', [('694fbbe3-669a-4611-a931-b5106c6de1d4', 'gmraycbwgo'), 
('9b71e1ea-9a59-4a01-abbc-5876a8506905', 'jclyvahwwu'), 
('0788891c-b9f3-45e2-a235-d2717781ff74', 'jgsichronr'), 
('cad82d95-61b4-488b-ab69-9d036e43812c', 'jrqctorpci'), 
('97a4fce8-82a3-4a89-936b-acc9c84de189', 'qngsvvosgf'), 
('548a9ac2-b331-46e0-8f89-b089c7426589', 'wjbkinbmxr'), 
('51ed43e6-761e-4643-95bb-2310afc5143e', 'xmltjrmhco'), 
('dbb98501-9dd6-4a68-9d45-d5ba3b0398b8', 'xzkrtsmgil')]), 
('6ae58b65-6cbd-4b36-baa8-fe72089d500f', 'niqubdorny', [('e6318631-507b-4665-b983-bc95a29ac8af', 'hsepmatsgv'), 
('1c3489bd-0511-4b2d-bf4e-de034816db6a', 'memihreytz'), 
('59a30645-6fd0-4c1a-95ef-b1a6a9203d97', 'ojzckrrwfd'), 
('c57a8dcd-d3ab-458d-94f8-1ce8630f39bb', 'qdjuctddgw'), 
('a31b3ad9-5bf7-43b8-a300-30222b9ac927', 'qyyegtcjxn'), 
('8ccef836-9609-4536-8cac-476e85b12ee7', 'syfynunlho'), 
('8bb5ef50-212d-4721-b130-43626863bda6', 'uvsifuwese'), 
('385de026-2eaf-4eea-b2e8-1aba8327910b', 'vzvgzeiutb')]), 
('aa147970-a2fa-4d0c-97cb-eadab73d2e92', 'nitokefzhm', [('c313ae36-9bca-4cf5-ac30-00159b7d0ff6', 'itktqrmkvq'), 
('deece32f-7e7b-4ac1-9ea6-a46f5c9f13b4', 'kyzdotwaxp')]), 
('8a52df7b-64cc-4c23-baac-ab298e0610e8', 'nnmyfxmqrb', [('5b165b5d-a606-44ff-9e0e-8520e6778fb1', 'aatrhaoxvt'), 
('529f6fe7-d34f-41f4-beea-3440b9d227f7', 'bvdzazyqdr')]), 
('6d240113-3ab5-43d2-ab63-71de26cac555', 'nogyknwqxd', [('821c29eb-e2f9-4cc6-bada-6b15ead139f0', 'alkdqqgolx'), 
('a0e51e20-f156-48c6-acc3-4a8e7ed4b49a', 'gdnekickta'), 
('af06d303-988f-4f4f-a6c9-61e88b887ead', 'igeqygkplf'), 
('2e27702f-a1b7-497a-b8c7-d4f9a4aa253a', 'qiopdmsdbb'), 
('c1320dc4-7337-42d4-a06e-e12a1aae646f', 'uutctfjvfe'), 
('f30b5f0e-c04b-4fc3-bdc3-2bf0dfe68eca', 'uuzccimawo')]), 
('311bc4b4-79fd-480f-9797-247a6d1c8a14', 'nxktqfqkgo', []), 
('7929109a-2fef-465d-a856-8fce66e865e3', 'oghgbrtbce', []), 
('4dda5a9a-14c7-4ef6-9653-5d7bfc59e282', 'ooycnrzdan', [('b1eb7f06-6a14-4aff-868e-8b670a714d28', 'cypykpfsfk'), 
('1e99dad5-6106-4154-a3fa-9a8517849274', 'ktfletigmp')]), 
('5664bd58-d39b-475e-90ad-dd0bcba17a47', 'orebcippbi', [('91488ca8-5425-47d6-8f07-fb61fb7b3c2d', 'bgbohzdbof'), 
('f43420b4-4edd-4ce5-aa1c-72c2c07c1e27', 'iijpkcmpoi'), 
('55a96c70-d051-405c-9243-0d8a55cf24b5', 'jhkhjyiued'), 
('62430737-3cf8-4482-b6f0-c7b338603f04', 'mahbebvrud'), 
('d2d92a76-edf6-4393-b1f9-12b8d7d7e479', 'mbbdtzaqcz'), 
('b83b852a-94f8-40c2-819b-d98e5b791868', 'tvjsckszin'), 
('76efe0c9-1972-483c-aa60-b4d288ebdd26', 'vrlaforawe'), 
('211be82e-85eb-45d0-9fab-2354cbbf03ad', 'zgyfmzcjly')]), 
('847b7811-68c9-454e-9a16-6047d79e57df', 'ousuyzrstp', [('5a4f4cab-c4f8-4214-b5dc-bdcda01c6441', 'ixeucfrklm'), 
('99eacbc8-1d98-41fe-9662-1b93f9557406', 'lqxqaunbsy'), 
('b57123c2-2852-48f3-88f3-3d871ed96b27', 'xcwkioclic'), 
('7f2b39f6-7f7b-4bf0-8522-fb4c2baa45aa', 'ydstaqtvrq'), 
('35156b3c-dc98-4b61-9ec0-901ffd53d307', 'zrvyaxuzbu'), 
('74d91c02-c30d-4a59-b6c2-b59ba7da7f9e', 'zywpqtiusn')]), 
('4e64f6f0-1cf2-4ebd-87ff-c191e2e6f8f3', 'ozvgiowofp', []), 
('4f463bd6-67bb-4a42-bd81-4932dcad5333', 'padfczcsnl', [('bc0c51f8-a167-4f2c-8f4c-499043787691', 'cxpxpnzbrc'), 
('3292ed9b-28a5-4a8f-85e1-0b5559a943d5', 'ebjwohzuiw'), 
('2cbd1d9f-5e70-4128-9ee1-c2458ac073bd', 'nqoovpdoyj'), 
('636666ab-eb41-4519-a9fe-2389e7ddc049', 'pqdrelkhip'), 
('adb30b74-e582-4dce-9d91-84f4f751401c', 'pwlzejwath'), 
('7303d19b-a6a0-4a19-aec0-6545ca999fb3', 'qblvltrgyz'), 
('3e1f2ab8-d705-4e51-87dd-f5582fff00ec', 'tzgfplwjbg'), 
('5495c1e9-04b1-4d68-bdcd-34aa80f83d04', 'xxhdofuszy')]), 
('fc4613a7-795c-4d1c-ba57-e4af32f4ebdf', 'pnwrmmnbnd', []), 
('8528d7f6-972c-4a71-8e3c-4e8c17710bbd', 'pozsewhplc', [('41a4fb49-8f51-4bbc-8493-fc44ec9664e3', 'ngqmdzunqw'), 
('b10aa4bc-1fd5-4e19-837f-c1a99abaabe3', 'orucsjzvkn'), 
('dff7aee6-d806-456f-985b-275403b153c4', 'rdowsiuyxr'), 
('1dc51a9e-3bae-4c4f-81dd-8af5d4131fd6', 'syxpzmmdvj'), 
('0d9432af-ed39-456e-8ebf-c97782df68e2', 'ubztkhhrbf'), 
('ff08c4e7-81c2-4f05-bcec-3740e6835b5c', 'wamxmlyvcy')]), 
('a410e715-249c-4bcb-a0f6-a4ab3d3bc217', 'ppvzeyqcpd', [('59101bda-db51-481b-b3ba-183e336fcf39', 'cuzyjlnmae'), 
('e72b238c-5b78-4422-948c-8e89911b35b8', 'ejzcggwenu'), 
('709fe647-2c75-4733-9b7a-9f12a0d37d55', 'hehixqgufq'), 
('80c534cc-c67b-49fc-8cde-30d6e1e18a78', 'jwvinfsxho'), 
('7d96dafc-5fb6-4913-865b-1206774e34d5', 'kvgprjglox'), 
('e050d722-ec5a-4d7e-9139-57d700e12041', 'lkzykayblf'), 
('90de806a-a3cd-486b-8c2c-1c4a162903c9', 'rdsvamrqku'), 
('3795da9a-6555-4445-ac53-ffab1f940d0c', 'waccjmkjzo')]), 
('e16c11a0-9d4f-4a16-8fd6-cea836293f4a', 'pubwqsqryv', [('b304c2f4-21f1-4517-b51c-52506a3d5e19', 'dfkncdqstu'), 
('f94f5c2f-5310-4985-b9d4-12a1a6d1d31a', 'doejbtvcrd'), 
('53bfe378-ca58-43bd-8f58-919975e1f801', 'iewumoqrum'), 
('e3655262-8e7d-4efb-901e-cecca0fc0b95', 'ijphsatbym'), 
('4dacc5f5-35c4-46bd-96d0-2a185bb60a87', 'mqtketzdpr'), 
('fa24f036-f0b8-4b08-b083-fba9deba170a', 'tyqyhgbbcc'), 
('974b31e1-a793-4e50-a1e7-6a86b9f6fcc1', 'vpywftvzwc'), 
('735f8c33-5d72-4999-bf68-88817ddd21b5', 'wknsfzqlzq')]), 
('b56e8d16-5caf-42d3-a95a-74008fd4f662', 'qghbazjipt', [('d61ee194-0a33-4ccb-aba5-086e6ff5f699', 'eaoudqapzx'), 
('8c064953-2526-47f8-a881-a0db8dc0cdcc', 'eiqqwoxyaf'), 
('edfce879-d164-4f2e-ab57-fecd3073c9c7', 'esidlrtchg'), 
('f206ab4d-9598-4dd7-b873-bd1b864b6cd0', 'fjlqqsasyo'), 
('61ac92d6-4c9e-42fd-983a-6422a7ed87a3', 'rnxkiyocmu'), 
('bc9e5507-6fe7-4d54-8acc-8895f6c180eb', 'ugksuobjyg'), 
('dd015865-3ff3-4ebf-8d94-c3aac24407b6', 'ybyohlannb'), 
('a65f65af-bdff-4b74-8996-570ca63680d0', 'yiaqdpbdtq')]), 
('0cf20ed3-3e7c-424b-ac45-5347bad3ef74', 'qgnywbqnzv', [('0eccd094-3f65-4b25-a53c-4c2e4ad32e8d', 'ayifvwwymx'), 
('ac12d15f-2c34-431b-95fa-8b2f6ca21174', 'ezjokesrhj'), 
('d3019058-96d4-4ee6-84ba-e38df27f5316', 'hiyqykyfeq'), 
('c63131e1-4ccf-4497-a702-9d5a24f8d4f8', 'ioxdfzgbmq'), 
('79c50bc5-b8de-48d1-bf43-c5bd2d676298', 'jstxautojf'), 
('9846501f-0cfe-4d77-80b1-439fb708dbb4', 'qqzxcfzjkr')]), 
('c8a76db4-7e56-46f0-99a4-6a672bb2d01f', 'qqzsesfksd', []), 
('da02236c-bdc2-42c8-bbda-eaa8e458d7a6', 'qritpudycj', []), 
('616e0779-3120-4212-84de-896177cfba03', 'qrvnzkksas', [('e1345ed9-0773-475d-8a06-df8eaf790ecb', 'bbqzafutuv'), 
('a3023f3b-39a0-4bf2-8661-ed9e4868dad6', 'biduqtsekx')]), 
('cf4bf6fb-34cd-441f-a73c-1967ef0eca13', 'qtnscfbbmy', [('0117f800-3ab7-4e99-84df-830f2faa372d', 'awjxrlwlvn'), 
('4e2a42c1-4570-4d0c-ace8-d7f6497faf7a', 'hlmdccsmlq'), 
('1df8ae40-7bf1-4058-9bab-3d699b22fe82', 'ktuqgpmvhj'), 
('0bf41dc6-eeae-4512-bdf6-d7d5caa9e853', 'oefkfxbhjm'), 
('72b1d64c-5cbc-43e4-9815-c40d2926ce75', 'synswbsfbh'), 
('c09d04b4-08e4-4755-8262-df07d17d6c60', 'udztjldpne'), 
('42bf4985-c27c-48c5-a01a-31312a8fed28', 'uwzcgxgkkp'), 
('13a699d0-0939-4f10-a7bc-e2cb4e8b99b3', 'xpimboygcx')]), 
('60f7ab5c-da30-484e-9ccb-dc303f296bcd', 'qzfaozhkiw', [('bb97685d-1e58-47dd-819f-7be3203a33bf', 'drfeldsmfj'), 
('83de3748-76d1-40fb-92d2-c58e8610588b', 'vsuzorevzq')]), 
('6c632de6-387a-4d3a-9eb0-a9764400b532', 'rnvgxgqoxj', [('df0d79a9-a6c6-45d5-a153-b5f724cf8e8b', 'gmeayvsvqu'), 
('2392bcb6-444a-4e8c-8c25-88edd9c7e262', 'johevjluee'), 
('2198a0a8-678c-4525-93c6-6b0781248c82', 'llzmrpzqjd'), 
('dfd14b8e-4317-4990-9341-77f3edf7fe02', 'mjhiofwyzq')]), 
('17e601cf-db89-4d18-92ad-6000d012c35c', 'sahtyzghip', [('f387cbba-462d-41d4-bd89-4f35130c7a61', 'bggubdvvbh'), 
('35521759-abfe-4135-b6c8-4d1bb6d10b97', 'fibmhettrm'), 
('a9fa5769-f7b9-48e8-b35b-64a0bf91c0ec', 'jmxmlbdhuy'), 
('ffe4e65e-5312-493f-b653-ba19c88935a7', 'pefobrtpaw'), 
('23979ce8-3773-4427-87ec-c3b8c8664468', 'vnjrmchvul'), 
('733879bf-1d81-4498-8f57-4a0526c49181', 'yeawjmuaap')]), 
('63faf1f9-6a92-415e-b23f-20e33d13546b', 'scbfawpwuc', [('80c31b53-b58b-4418-aa48-27d410e38c05', 'cjquputswn'), 
('e8189b38-3967-4de7-847d-6695532be524', 'kivnnzuwee'), 
('c6ea24b5-8117-4589-b6cb-2612da3b4d12', 'lpxptvgvxe'), 
('24d96889-595c-4fe3-9d3d-257260ec1151', 'mheiuxlrok'), 
('3ebebb76-8132-4242-8085-e8805eedff59', 'mvqygpwryj'), 
('72708056-1634-4436-8eff-31e117b4b62a', 'usrsccqpft'), 
('173128f5-11b1-498f-92f6-1a3a4e08441f', 'wykabjvqfs'), 
('6ef672d5-f357-41ba-8e1a-1288b8f94e21', 'xwagwkfylm')]), 
('5b262a6d-b4f3-4b4e-953a-7b9e38d33020', 'scqyjgzqab', [('82257a5b-52c6-435b-9369-699d9ecbfc06', 'bxcvsxpssf'), 
('b09f5af4-78d2-4eee-9388-649e1455e75c', 'byidkqxzcc'), 
('aafafb77-8a69-4104-921d-aa45f1b151a0', 'dkvwgtrrwz'), 
('7ad37992-8b5e-41a9-a2a6-eba12b6a141d', 'hpnzpdoxpg'), 
('7658625f-979c-40d6-a8d5-0cb6dd76601a', 'vrwyachqrd'), 
('5589d4b9-2994-4706-909f-403d9d30b301', 'zteklqbenw')]), 
('736fea70-7b5c-40d7-98af-ab8937af0100', 'sdbaiyewel', []), 
('06e5fa3e-2fc7-4f73-90cf-4dc9d92e6405', 'skyoedwfxd', [('cb19131e-a092-41f2-86f5-01aa6e96adfc', 'futkgbelkn'), 
('b0e01334-1444-4547-aa13-fd53feb366b2', 'gsbsluntej'), 
('b36ce744-9c9d-4285-83c6-c5a8e94ce7ea', 'ihncjvkjij'), 
('4b73fd01-c90a-4302-8b31-2dfe3a1c505a', 'rrdszgzkgf'), 
('09b4de77-c11f-4e60-b4a9-3591c1836e09', 'vlzxfmgzaa'), 
('af89b35d-bc10-4843-91e3-5040c8cb342f', 'yskgevxzii')]), 
('f076116c-1a94-4ed1-9284-a1bb064c66df', 'stgfddpcnq', []), 
('bab2eea2-ddcc-41da-b64e-8e45f797950a', 'syxcsmqddn', [('39680475-af55-45ed-9308-c6d4d4bed7bc', 'crveulftns'), 
('70a4579e-f9da-4541-b3c7-933d8c79a70b', 'hjmrnfpemn'), 
('e0c9a07c-9b68-45a7-a21c-04f0e10921dd', 'oomypnhxsa'), 
('ed6f345c-e3cc-4adb-8a55-32d1737fa689', 'pfsyrnxnvl')]), 
('4e30bf22-753a-4370-8595-94e64e40025f', 'thvmpuhexs', [('a046bb6d-e754-4205-9775-1aa9c7c32c15', 'agasnueigv'), 
('2d23611b-3dd5-463f-9f14-0d1be8563ab8', 'xrafsdthjj')]), 
('0eeb61ef-18b8-4913-8028-086b0d6b637d', 'ticrtpljil', [('cdc8bb15-0629-484f-b0de-ddaabbe094fd', 'bxukgjvvym'), 
('8898b7d6-3993-43c5-91cc-48d16e5d7b05', 'esruygcwxa'), 
('23ec1e5e-076a-4874-892b-a6f11154564d', 'gpagxnhljl'), 
('e9d64a51-1ab3-4c4b-8ed9-c900a2181929', 'lufvevcpfy'), 
('0c236297-3b25-451b-8c61-5753fe904a25', 'vgftobbvrw'), 
('4472bb7e-e208-495e-bf2f-98019e4b2066', 'ygvaqngygk')]), 
('e1e80cc3-0cec-46e9-8862-2c2775bd56c4', 'tikzedzmwz', []), 
('517ea3bf-a0b3-4e03-b7b6-a0d890c752f0', 'ubycxcyakh', []), 
('dba09bad-4b3f-41dd-897b-d0ccb6b4e85d', 'uevvnlxmoj', [('707fd617-8c0f-4fd8-8ec6-2287d9c31831', 'lbezoanqan'), 
('c34e60fd-50a4-41e7-89a6-6f08860058a8', 'masdajdjld'), 
('addc26db-ea1b-48cd-893c-61913aa8941c', 'yzxlmoexvc'), 
('b6109f3a-a051-4c63-af37-715e3f512ac1', 'zxgxghwtkp')]), 
('d8dbd0b6-ad87-4248-8418-fe16be8146b1', 'ukfuobeqig', [('f839a0d1-ed81-4292-882e-cf62644bfbd5', 'hlscfvvgvq'), 
('702996da-4b64-4770-9ffa-5c26b0b68696', 'lnkltacecw'), 
('154599b4-79e4-4295-81d0-8462d333dd28', 'rqsbetwxgg'), 
('7ef8cecd-7ff5-449b-99a3-d415c1c46543', 'yomfsykcxi')]), 
('b5226b7d-ed09-455c-8d54-00f26c4c5589', 'ulnroyousp', [('80fd4895-5377-4d83-b7ff-0bfcc457b8b4', 'xybwikslqv'), 
('a19ad081-22c9-4b55-8d37-5c4bb66c28c1', 'yuuujjjapg')]), 
('b781fcd8-f0ea-4e5b-b559-55376ea7aabc', 'uuezrubczo', [('4b0c0b7b-a5dc-4c5a-b038-79e119e678da', 'fboipwqqdv'), 
('12e2b782-6d0d-4220-9c58-bb88dbed06d1', 'fwuwgbfzkb'), 
('be19a8a6-1877-4bdf-b61a-6920ee11d729', 'gtuikjqmzx'), 
('20052c1f-6625-479e-b2fa-c5a4c291e87d', 'hkshmrwdln'), 
('01d5db7e-1e27-4b24-88ac-0e31299192a0', 'kdlepbygvx'), 
('b1ce0ea1-e47a-4676-9f42-32683d82468c', 'puuiusmccy'), 
('5852208a-dceb-401a-8205-d88f7be5b1a7', 'tvtlhqejnl'), 
('a7cababd-e213-40fc-af9a-3369ba925d05', 'tzoujvxuzt')]), 
('aeea6f22-4491-48e9-b5ee-686c422228aa', 'vtrhsurdkn', [('cd640ca6-6389-4a45-97f8-d9e23d3acce9', 'fwwtamyzte'), 
('5bdaeb87-50cc-4288-8ee1-4a28fabf6b5f', 'jbwftdpfwa'), 
('da8a987f-352a-4e59-8652-b43c8c3c9ee2', 'lsljlxlosh'), 
('7db35cb5-1500-49de-becf-e2821f6b2d1c', 'mzibsvoiln'), 
('68a61b91-39c0-497a-acda-acf84c311409', 'skplubhpht'), 
('a922cb87-5f9f-4598-90f4-db9b1b707158', 'uwbrphemmb')]), 
('0ccad930-35d7-4dae-8ec8-a4897547c425', 'wbtbxykspq', [('7457624f-517d-40a7-9aaf-099d96b0c337', 'cpjnuhgvzd'), 
('9819a48f-0238-4d1c-962a-3bb32010745b', 'mipcvqekbt'), 
('678749f8-9239-4a4a-bbd7-402feb7a62aa', 'ttmujqmswb'), 
('2fa3775b-f381-4ce2-a1e7-7de2df71537e', 'xoklwpbesz'), 
('1f8cd375-625b-43d8-adc1-5f571075d86d', 'xtrbtqjnrz'), 
('be0ae75e-85f0-42b8-93dd-1046f5195486', 'zorepwvxyx')]), 
('78bee649-cb93-49c1-aa8e-5cc1ae6d7294', 'wdzuhfeeqi', []), 
('087f823f-ec50-4c8b-b2b3-f0242549de54', 'weerytpqno', [('c6994605-1234-4c96-9948-d56825966ea2', 'akrcvnxogo'), 
('2694593e-3fca-4104-b7ed-db0bfc27314e', 'hyldifioim'), 
('1c96e36c-d772-4106-9c18-1a0cda964fd6', 'pxuhtakuqs'), 
('d5d8c823-0ea1-4979-bf49-ae6d18175725', 'qreswyeump'), 
('efa932d0-512b-4cd4-b1b8-4e425de70609', 'qutxsondgl'), 
('f439bf3b-6dc2-40a6-b31b-08b19583e586', 'vhwttzpsqj')]), 
('61f2bf40-eea7-4e60-b67a-2374db20b36b', 'xgplqevgux', []), 
('c68949cd-9301-45d3-97ba-0f9b448f5a7b', 'xjruvjbcgv', [('fc6a5e7d-9af2-498a-9c46-028f4f6690b6', 'ftqndrpzpi'), 
('ca270a9c-826f-4598-9bbf-0b14f5f7d7d0', 'ixoxpbmemw'), 
('66d6d5be-f78d-4317-92e9-cf3d9a6fcfca', 'majwmpsfrl'), 
('04ecbadb-de54-419e-a13d-65bc50c15016', 'ojmhgmgvuz'), 
('aac40c31-8cf7-4ce7-9ad8-93f4c3f03678', 'pcrnjexzyj'), 
('c38695e3-7b5a-40bb-adf4-563e2cc8a363', 'qqdeyqosfx'), 
('7aa1cc92-4fa6-4c1d-b9ef-ae7790414e27', 'xigxefoygn'), 
('8c9fa3a2-1d4f-4213-a745-fe3886d12240', 'zhqiizszdo')]), 
('6ba8ad24-0045-4f2a-9eaa-176bbb9dccfb', 'xmscofxgmf', []), 
('9ec5c6e0-9858-404d-99cf-fd7ba5703c5e', 'xwxenvubri', [('3b12f84a-7cdb-4675-aeb0-e7c4afd41288', 'atjzdgvyef'), 
('e024c4b1-c465-40b2-bdc2-2827bdc1d116', 'ggothiqddq'), 
('ac0e16cf-1a83-4b3b-bc95-9f319c994972', 'ivieeeqauw'), 
('ce82fbd3-d9ff-45bf-b9ef-66e766c7aa8f', 'ntlwutdcld'), 
('f7962426-aa0a-4779-9178-cb422fbf4d41', 'tvmwlkhyya'), 
('172bb24f-e02f-41e0-891f-78cf90f10f71', 'ugjmosuivd'), 
('5d030a0f-f3e9-4964-bb0a-69789043f755', 'upivcrfxip'), 
('3726449a-2b9d-4ccf-b703-46e350fec6dc', 'ytcfnxylgp')]), 
('b237b719-120b-4188-8da9-dfd2e62cd435', 'ytuwlgtgiz', []), 
('2080985b-cab9-4992-b560-06f5e21e5ce4', 'yxhgcnuafv', [('96ffa666-a09c-45a8-8ccb-4418effad5f6', 'lvjdreyfsh'), 
('43b4d4ae-ef65-4861-8000-77121a499ce9', 'pwcjazdxuo'), 
('14a03ecb-8510-4758-a371-a02156469a61', 'sdbtmljguy'), 
('346999ea-9780-4b5d-9ada-580c3b327e18', 'uorwrvzshd'), 
('a5094d3c-72f6-44cf-a5d8-a31893421a94', 'zuwcxmrqdr'), 
('2403466c-8004-4ec2-8e14-4276c01a7ca0', 'zxnopqrjvd')]), 
('8db67a9c-a08f-49aa-95a9-39187d798b1a', 'zdbnlpdqut', [('9f2304c1-20cc-431c-b368-aa84f6c8fa3f', 'ohkiufsyae'), 
('a75392e4-b2cf-4350-8587-393a5a6167a8', 'wgxehdipzy'), 
('f08a1acf-b337-4522-9283-863b136bbc54', 'xwxgvsxeuc'), 
('3d668b92-e397-486c-8e4b-0aa4f63feed6', 'zborrycxsp')]), 
('3c63e939-efcf-4a64-a634-c8c07203d843', 'zdvmpxlwvd', [('fe23ecc6-537e-41e2-91b1-95bc5b8f3ced', 'exviglexty'), 
('715ff0bd-0c70-40fc-9618-a31024f7a592', 'kammyfhyod'), 
('87c81288-f3d3-4149-a4a1-0f9b3f4f5c3d', 'prawwveqzf'), 
('7d6e0ec0-87f0-4af1-b5e8-559387b94edc', 'qkmfdowpzr'), 
('4ba64901-3925-4f5e-b3e4-ce8040fea198', 'sixyzhufgx'), 
('54888520-068a-4014-92f4-6c017be9bfd4', 'skslxjhwuy'), 
('1187475a-1490-4ee4-9394-d45902ec5add', 'vkriqjypcz'), 
('dbd1a834-a5c2-4292-8ebd-ca34ebacce62', 'whxsahhkyl')]), 
('c25ed7f8-3533-42f5-8b9b-663d90abfd34', 'zdxgxgrpgy', [('46ac5e23-b81c-404a-a645-b07b925a4906', 'jgtwlhchtl'), 
('18ce1086-1391-493e-9244-36813912537f', 'pqznifwijo'), 
('f8babbae-9d6d-44b3-890c-e960228bc41a', 'rlomdmcbdv'), 
('5e12d757-ebe3-4560-8194-de16b2312102', 'tldqmliidz'), 
('a8a74f60-ac81-42af-af06-13020fcbcd58', 'wnsoqhrluy'), 
('4ff3ff3e-257a-440e-9a13-b5dd86f6a444', 'wreinyzfxs')]), 
('6bb11760-720b-4699-bd3a-30ff5c044666', 'zgqqzpdibt', [('8f34b720-6649-46e4-9646-0ab9b279de5b', 'aoohyuooor'), 
('8ce1ea77-5b9f-4e8f-8b7d-53a6353edf24', 'bjvxdmbolo'), 
('cb5d7abd-bb94-47e1-880e-a6159b42c777', 'enqdzjwbnj'), 
('14ed180f-b382-4a1f-8385-830c881720cf', 'fzjjwqrnlp'), 
('fbc4d555-3ee1-4cf9-b46e-9319cba6dbb1', 'maeydrvhgl'), 
('77045f62-7e83-4cc7-91b9-f3e00072d06b', 'upefvacfpk'), 
('53b5cf04-ebf6-4b13-b4c8-d20a6c8e8e97', 'woifxqeodn'), 
('f33ced1d-b5a5-45db-adc1-9706828f8b90', 'ydpoblhwrt')]), 
('838bc4b7-f63f-4b20-b1e4-9c77291749b3', 'zicdfzpfhq', [])]

NO_PROXY = {
    'no': 'pass',
}


## Request
page = requests.get('http://0.0.0.0:5000/cities_by_states', proxies=NO_PROXY)
if int(page.status_code) != 200:
    print("Status fail: {}".format(page.status_code))
    sys.exit(1)

## Parsing
tree = html.fromstring(page.content)
if tree is None:
    print("Can't parse page")
    sys.exit(1)

## H1
h1_tags = tree.xpath('//body/h1/text()')
if h1_tags is None or len(h1_tags) == 0:
    print("H1 tag not found")
    sys.exit(1)

if not re.search(r".*States.*", h1_tags[0]):
    print("Title `States` doesn't found")
    sys.exit(1)

## LI state ID
li_tags = list(filter(None, [x.replace(" ", "").strip(" ").strip("\n").strip("\t") for x in tree.xpath('//body/ul/li/text()')]))
if li_tags is None or len(li_tags) != len(states):
    print("Doesn't find {} LI tags (found {})".format(len(states), len(li_tags)))
    sys.exit(1)

for li_tag in li_tags:
    is_found = False
    for state_tuple in states:
        is_found = re.search(r".*{}.*".format(state_tuple[0]), li_tag)
        if is_found:
            break
    if not is_found:
        print("{} not found".format(li_tag))
        sys.exit(1)
            
## LI state name sorted
li_tags_b = list(filter(None, [x.replace(" ", "").strip(" ").strip("\n").strip("\t") for x in tree.xpath('//body/ul/li/b/text()')]))
if li_tags_b is None or len(li_tags_b) != len(states):
    print("Doesn't find {} LI tags with B tag (found {})".format(len(states), len(li_tags_b)))
    sys.exit(1)

idx = 0
for li_tag in li_tags_b:
    if not re.search(r".*{}.*".format(states[idx][1]), li_tag):
        print("{} not found or not sorted".format(li_tag))
        sys.exit(1)
    idx += 1


## LI city ID
li_tags_el = tree.xpath('//body/ul/li')
if li_tags_el is None or len(li_tags_el) != len(states):
    print("Doesn't find {} LI tags (found {})".format(len(states), len(li_tags_el)))
    sys.exit(1)

state_idx = 0
for li_tag_el in li_tags_el:
    state_name = li_tag_el.xpath("text()")[0]
    cities = states[state_idx][2]
    cities_li_tags = list(filter(None, [x.replace(" ", "").strip(" ").strip("\n").strip("\t") for x in li_tag_el.xpath('ul/li/text()')]))
    if cities_li_tags is None or len(cities_li_tags) != len(cities):
        print("Doesn't find {} LI tags (found {}) for state {}".format(len(cities), len(cities_li_tags), state_name))
        sys.exit(1)

    for cities_li_tag in cities_li_tags:
        is_found = False
        for city_tuple in cities:
            is_found = re.search(r".*{}.*".format(city_tuple[0]), cities_li_tag)
            if is_found:
                break
        if not is_found:
            print("{} not found".format(cities_li_tag))
            sys.exit(1)
    
            
    ## LI city name sorted
    cities_li_tags_b = list(filter(None, [x.replace(" ", "").strip(" ").strip("\n").strip("\t") for x in li_tag_el.xpath('ul/li/b/text()')]))
    if cities_li_tags_b is None or len(cities_li_tags_b) != len(cities):
        print("Doesn't find {} LI tags with B tag (found {}) for state {}".format(len(cities), len(cities_li_tags_b), state_name))
        sys.exit(1)

    city_idx = 0
    for cities_li_tag_b in cities_li_tags_b:
        if not re.search(r".*{}.*".format(cities[city_idx][1]), cities_li_tag_b):
            print("{} not found or not sorted".format(cities_li_tag_b))
            sys.exit(1)
        city_idx += 1

    state_idx += 1

print("OK", end="")