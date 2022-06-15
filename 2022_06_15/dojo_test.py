import unittest
from dojo import *

# aa bb cc dd ee - True
# aa bb cc dd aa - False
# aa bb cc dd aaa - True

example = '''aa bb cc dd ee
aa bb cc dd aa
aa bb cc dd aaa'''

example_2 = '''
pphsv ojtou brvhsj cer ntfhlra udeh ccgtyzc zoyzmh jum lugbnk
vxjnf fzqitnj uyfck blnl impo kxoow nngd worcm bdesehw
caibh nfuk kfnu llfdbz uxjty yxjut jcea
'''.strip()

input = '''
pphsv ojtou brvhsj cer ntfhlra udeh ccgtyzc zoyzmh jum lugbnk
vxjnf fzqitnj uyfck blnl impo kxoow nngd worcm bdesehw
caibh nfuk kfnu llfdbz uxjty yxjut jcea
qiho qif eupwww avyglnj nxzotsu hio lws
xjty usocjsh pivk qnknunc yjcgh bwya djw zpyr
ycfmfe mgq sjiomg nfzjul bjwkmgu yvsnvgj dcjupu wzz blmn
rdowgbt vpwfdoi blzl laghnk gsa vhnpo cztxzlb rtz hvwonhb eciju pfjtbo
bqs bqs dbutvgf mmzb izpyud rap izpyud xlzeb mnj hjncs
xpu vwp nujcos piu irindir tpmfd umtvlm gznu
sfpuxar qcnbte omouazv cnh uaxspfr sepolf rusafpx
xbmaf iceyqqq sabpt gliexel muubepe qqiyqce fmrcc eazk obkeonl fmccr kgk
apg gbycwe gap pag
gagv saqbk lwtllc wnhzz khxsjc
lgc alen rlmsp anel gcbvg
bujlaz rks rlqf deknmee yrp
scqvl weusbc bgvaz vgg cjwsfno vqy zbq aqy tvf bgzav
hbki vei fxdwljs myjuba elbsib pvy xxjxgi dtgv
linzaeu qbwdke fdg pykw
qvtdd aco aav bpu mvkcuc kjfj japgfki jfdl gem hog bdzsiea
wpbigkb lzhwba jssjkn qvb kmwu qddv
iny osyvqnt tumunzb torq bdeneg wywank poza ipp iggorw
tuko mhdbsf vmjdop jomaqpj rcdsud hmgspr lsas nzmwc
cirkjq nmjuu xtgejv gtexvj vjcmtqq unjmu
xsdmezq xvqjvqp exhygy qahju hvd qadmdh lok
wvvys kax rohrrar rwhnvi lhnmefp lsktouy bxilosp
wayf diobnl zvu obnidl oibnld
cewil ygsf ffzp ruxhu vah lnvwt aef lnnjc kgkb gxtlx feko
uti epphrin pywths cpzzh csjei nczhamy gayxmb bdcytq xkx fgmt
qvzyuwi dwo swkw bwjdrn dasgd ijgw vzabaop yefyhmc wgij
dyg sugrf vid etz weyqg nyntx dwfgwm khon hnzzzn xfyra
ofbh bdrsk rdrjj elaxvk jrjdr
msxau rsocvx zxdda mxz lknl
qktaywx dirpdbf unqnd wbrwkuu fvmqwl emxr big
xwz kvsydc ayokjyy qiah omw neo htltxx fxhwqwj colqvbb sxmo ephfkex
ncjxoaf fwjkc czmhv ylg axcjofn dvj bzqjku opvcr jiwzucg vmhzc
gmmnrt zqar twdwrg qiwwki fcbr lixm hjdwwe moiva
roinlxg cxeezve whannk cxeezve pyoj boweioy cpkgxsz
qkct qso xlb xyy aellfet rzt cbboow devfb nih fhbfxzi
qyc ltxia alixt atilx xtgrv
svruz ufvo rvesnxv dik vzurs jjg idk
xeudhrg hudn cilo ljplosb
kpb oyzvywx vldko qhfkwod bkeutk zqcqug pbriu wqocos
qkngzfy whobyri aze jvipdty ocirbep icqwc
kzxxlab sjr zhymws xkbx
nnxs gkwtld dwhkry snuibq dtdl aicug bhtlfzp qzk jctos
regvro mxcq hqof yraucxi jhkol iuxineo pbtnk rfjwc szgjpr ndqqj vfgm
yqrfox xoqrfy utbryu utubyr
jdubjt wqrl wnk rlqw nwiq pnbn qinw uaff ftdo htfrav
rum mur umr tij ovbahl losao imawwpb wadhww tbteyqc
napxd kzeiqcp ppgqucm xkityt frq hugrp gjgtt gmuqppc zwqme
xyuzs ysch howlzgu dkqppbs nvbiz mks mtxv vivouex uvawq
ffe lfsn nlq mpulheq ikcfo wdtz cnwsbph zkib muu
bqkxav wtecb lxwdhr kqbavx aqxvbk
czwswqx ldkxapd pfwd bdkkj iqohla cwosw ihqpd pcc ckhabbn
foiip hau rbqiyhh htm omeubgh symh evfcqg
lqx xlq rsgf izu esetis
npsrkdj fvulgkw eovw mzr uobcze azb tij ihoer ehori jit wknsqhm
gnrksh xwggt oosi bpnmhx qqaa mpmryu jhzyz
yad gbexqcr gbexqcr gbexqcr
ldca xxhznn twyy ytwy zhxnnx xfmpi
floioot kfyh dhibv ezyznar sfg sfg ezyznar
cinioim iiocmin ypla aypl
mhwcjbz dftuqsy wswop eizbf ptsd
ehx mlh nfxgfkz uuw xftmn ptlkbo vsnyo ttwce
oexvf orcg cncnkfk comvhl
lqewsj lyulrcl efixd qvd fhznqnz yvrkwyi xmhgc vzbp
dmr wrxqh thcm giomp rtvl ssc gwq rbklw hcmt fjvud
teozhb dmzwfv qkq pvcqfqq
hvlebc qqmg repxk zwrjdx ztruwb such tyligs ybg
psa rqznokd lgc jstqres yiqt mbiody xazb xjuk dtb
lea ncm rnh myzqzwm
wjml eums ueflvbr cjpgnl qduunu zfxaai jwlm lprzzg vrn ttetyr sume
uwkgeu uiahd plyewgi vveo nwhsitz mcitc uvk zsxehgs sewl
lnbdrka sgtivn sozzq mgd vhxfnlr twrfpk
gadphmk mbx lmlbrf tsnehnr lawdpm fnima gxgl
umty vrn dpow fsnnpjv fsnvnjp nnsvpjf cioaio
euu uue zeskmtk hob stekkzm
ypqpri qwdju ypriqp iprqyp jnoxqa
lkppi ingfxw wlulvp yhwrli nxwigf oyuhq ggfslx
kdd ypvr pyvr waw vyrp khqq mamxca bapq gobfm
iuq upvdpv zxef bfwns lmq lxswr kpsqo pwde iaaou nsw udy
lgzo nil ovgrmt omgtrv jrqp pqrj lit
uumyu iiakfj gvdtzz qbux yxn ejs dvlts
hcm ghutxq zswi tmyhqef hgxtuq
shkhkdk kad seubeax kdl mzu
cpykgr skx rfhpor xsk moyhlai ogv ophfrr dxipuuh
beyw jvrre opodn zdoajhx fhg ijs drczy drczy hjungq
jrzieja gfg yzdn yxm wshibsn fgg
xtylh vxscmvp rfymq uzhpyea spxcmvv dlni msj yxhlt
eov awql miv miv eov
mmvrfbg fjiyf hvqz zpuqmbf fszyuz ldfgni wemfjl fjjpl rbnpy rfb
ppzpeh nam ntv xnchtyk hja hpepzp foj bibvx nmmdlff bsrkp
qiy qiy umhlnh qiy
tyds oepk wae tdsy sdty
ukawr rkwau ghtjhm axy
wtbjiv btjivw ewaf hwk ttq
kdpun myve sqv rhvpy fnjwt puw ujhf thsp nkdadqr
vyw wkkpdpy xlgz lmmcuve ncuq lmotk
pmsfw vxd jpe qxlyasx ejp gwuv
pmgyndm ezofbvx nicbwrw kwnlj yjvnas fdpkfo mqcsyhn pyjpf fbexvzo vkftm erl
trmwvk rywuzoz hbidea kicohfz heidab deaibh
sogf govd dknpk vxrvk rlm vwhjk
xnxbfmw wguzrhd zbmkz piwppa mkbzz xvwrdgy flusfqb
cgduq hbnwr xfx mrejb ckw zkbaihf cloow cwk wuvthv iwqctx
vugx qbucd gxuv ocb cob
ilmet fbelxxz qratdfn unoj hbc duv srmikz
vnzuw zgpbqgf uzm thysyxd dinfh bgvr olungg ksd dsetwqz hpg
omagsf zpr coa kknx bzithq pewp flvoz xiiq weojqr wpep
aagj gcglqt gqcglt xbfx dhdx lbx
pljq plxuscw ilh wfk lhi hli fouieyw
hvnh zvm aqy dzitirm veq ctux
lglhs aqibdii hjbn cfgc qrg pnbntcx owoks ebz
jozngde lwne mbo omb fnyzvvj gndozje
bbdgc igtdj uhahgp sqduko
uuspedu fgnspm ewc slly jbs chl heanm abqijx kadvgxu
akfsft skna kusjqr rkqujs
erc vrljpu lruvjp lpvjur
iors hcdr fsqtcj vop vmn dtqnz tov oscjlw cdrh ctfjsq lrnts
fxp mczo sjlcxa mzoc jmsq hcxybow dmrr bcoxhyw
aac ewraerq odmxpz aac aac
zzio zebmxa szeej poordr gmi owwnnh xfx rzrab lfey jesze
akc yyoj vqod drtne
joxhvyf ymasnbr omouvq isxdrr
qyi ayrkzu jsk vqvvno jkkuxi zufnnwu mrsszdf
ocqi htfb tzjna cdt wkzhynm eergf
yokzugl usyuqu qvotq uweqyow lygkzuo kpmqmb uglyzok
glvshl imqv jrv xlpnsy gcg psj irtiamg wkl
bjcpc nvyloa dkkan efj okubpc cxlowm eone kmpny
cyxqys nmuaftv gqxj gtvsc
beouh dioxiah kizdy hyi cozrray rave fqxmxmj gdm
frjz amrsat lxvhzj azhevtu vxlzhj
zwmnrk sbk txzrcsj sbk oosgfej cvh zuthibi onvwd sbk nhwpzq
gzamt vraw kuk ugayl lyaug bww rwav ijah
bdjirxg vifjr rhbxpa oao yrhjxoi pbn
navb umesiys yhix phuhu aekkciu nlnsiq wjf idqdwp
cmhw rsu urs ziprlfe
kyhxitv cgty bnwjyq cygt sgjn pdab imarvhg yjbnqw
axaa ejancv yau njpc jvwy bpft kwjvg qzrbvtm diu njpc bpft
ambj upe rmqr yudbiqf krudp pqyf
tnb mobnpv vep ohxoc cyip wxyccfo jrbi rwsws kls zlv oohxc
fjh dmb hlbq bqc jhf kax suz fjjg rkpc
wjnn byfirm goeyh xtjmdka
tgyfxx hefpxln mveobqr yeo ftfn srt vim vlcu hevoi xtaaff
imyql xotcl poql rlueapq bkwykm hlalk bkwykm
gkec zff hbmtq rjxjbcf arerlu pvz cdaqi nijmhv uodwjh
mpctof mopftc ksfbat sbkatf
nvdd jub bvi kyggdbx nwtiok gjt mgsm dbhsn rzibgjm dvdn eqi
ysd iirp dfgzza wiyeoou ysd ispkv bcqg wwzqgq xphse
ntq ivposb gsd ezl tlkztp lez qyurp vxsmg dgs
wijs rydbj onm usiyqzb hwrol giusanb kewukl yziuqbs doojam nom
lfacyy xwwast truqtt tzneimn uxsydc ktu eqyaj ndszak
ffleooc kikif fohgop aucy moubqxu
iaxc pnwexdl ncy vmwm xrqoi wpgftq rofx utyzjuf stdxq twpgfq
ppmlp etsvi cjdx poly ynx vfxpslg mqjo qnpsage flpsxvg jwsxiqt
lbyhnb kflrpeq ssoti webxr embbjd kbnx ubzqco
khhc vwuqzb ebocbko rwmonkz edfqn hzh qhncoq gbwdi wjeg ocwow
ghzhd kcxblp lzwkkr gzhdh umk pblcxk
wyajtw jiff ouylv sni lwhlrg avqjiis igzx wbl lhrwgl
glhh kaxha tqii hwzx rgic kaxha rgyidmt qdgxfl ynjc oibfij
bapj bix rjniw ynbql idlvnmt wynpzbl zlpuoix kvn kakwys
aldpxxu iojxp rif xbyqtr jffdvy qnrq tqwsdiu
ulssco ktbymjw bfj zhkg zgc ctyri
ilrmq wfahcgk mrlqi bguad inj
cjzc rekuy ifr wfkg sple
cvjkp qbmumnp mprg ltmwxxh zpemtyb ozzssfd ksu mgrp
nvc sxp mpkxz bhlctq hguaa yrdkm iwsgfg qjssh gobbies hucdh
jdxrjw qmo qmo vobhnu
dnjib wtjp rfdjqdj skpvrb vkwevb kxxovp
fzi kicta zkuvr rfaawv ehklq cfdjsyb tukahwr zkuvr kicta ouq
aba ytdguk gqmpn hvxabff hvxabff dckj
fna wxyqhxd hvy khsu yypoyy lvvue medheua gim slf drdbeh ikihf
jquz wwo wwo ghlz jrbvb jrbvb
jwzvkl yjw ouwla yjw ouwla
zsvlgyf rzqbtj qygynem ukdgjm lbsyh tmdzp fbcaim eymzr
pvw sbs dvsa plmepl pwv ayxk vpw dwt
inayadn pnti yzhxk azga gxq aznbciu gjnmyqm
isgf ndqmk beyqq ebyqq srtzxo aiiw oqfuwp uoqwfp buejctv pxbk
pzl irv tzvzdb wcy eszm ybwiw ycw riizifd iybww
btpu cua azzqffy owcr
ofwq sqlpzat lozdxlc aevjmpc lcolzxd wbbysn qwfo vcrx gdzgi
dbpfmxu ydsxwl ijn svxtop csep ldqeog ffye zcrl soh aclw
wyiyyhv vyhiywy obgi hiyywvy
ddvaoc lhv spurn rgxyy onjw illvn yryxg xyyrg
vid wdttqq kajr myip
wolqlue phlunpt dcmmkfm sgxk dmmckmf sfng jlbsntq dxp
zmneyho fswj xdgsjc oefwjdi htgxvbd tgqrq xodoa
ynw bygqdnh hhmnkuw cojqrke qszzdjo orskwq mdfae asabn
vvpm vkj pcxghao caoxphg axhblxb vvmp
txox nzy eqn zgir dytsi girz ffa ugjjbzj brob fll
kbz pukqbd fiwmuh umwihf bkz dvz
vgs vejs vejs vejs mbkyjjy
viqmnmu bitkyw nddnk dknnd cldnpp hipub plcdpn fdzzpb mmyomn
ndylnfx gozlrx ngptk rnpteb wtacx xmtcjy xldha
fey doyxis ampmtr ycqh syw cqhlj hnngx
dijf nac tvkq ayo akbj lzmngdm wfxpn bpyvrf cvdqpa
zsofz lhho hgat wqskga mnt
mylwm zxsd omzpa waz hcrr lxmpq jsw sqtwak pzoma
rwhgsgt ysdq ztihici mpwcawv alkqg wsxiwx
snldn bcb anjdv cbb awsscc cqxult hjmjew mcycb fdpdg sesrh
kukrqm fawafz qdim wyobtqx bnvjnqg dcvqxta yptr nnpu ughldqp duo zafwaf
knb yjqb bscpnt nzg sqeu zkahna ttuf nsbtpc ixwit vucwj idix
bfqyx xlnpc ijrxu zkqi kjxtahr fgag orusms adi bfqyx bfqyx
dqddc ncbv bvfk hefikb dqddc hqjl otpx zfiu
ntkv qunrzx eztzure ctt rjo bkdt znvd jwdf gqhf mmhrzgt
zeavm hkbf rawqwuf pis dojlkt vnjhmi uvk cufmn qginezd xyut
hnidzk chlctc yst pepd dxntbxg vqk daxfpmu wshyddl
jgd vesqgo bdyqy igl ahstdm wjtd lrtkjsv tjsj sccxbih esn gkkzj
iisiswh jll rhlaf jqwwgfa wmhyo izva vrg zjkak nlxxfer rvhx
mkrkd jlqtpy ukstro ktuors wsj ynqpbp kpiyxzv nxeiwg xpzvkiy
jbr gnct fwklekg cmfqnm ctn gqobrs kwht
pztmjs yiffc kfhsblx yiffc yiffc
biezil iiezbl bzeiil smocoju
viiigm gmmmk yeiv dxzogro qsmzsur hukzwjn lcle syo mdj uruf rxfseu
extchsd adeff ouikoj fyaclr rwwvqsd dooe tcxheds zrdqqhm fdoxv kbxi tlcj
aycnydq qlxhka zoi shplo qll
bfry lbwckm ltq rbfy gpn vojp ruj dpxcve geq
svtvfwh lca lac qia vhwsftv nookdfz xgjiaf yvcdlt
aspgqym fryuzhx bbydf tbn bwutsc fqgi zij lmxhog qnmse
rbb gsys volnas onvlas lonasv vwjdso lnteapy
got iauk kficn jvfuy yvoe jcxwui hyamqx mke mwh jcxwui hyamqx
avutfi ggmha dkopc kothnnb syoi xsd wjedywy
oziejyz yzeijoz hnthyn knj juuq qujtp kgq bymlnlf yicf
zsejuy dybeap hvowmvn okxb yoi epadby cnzjk xfwprzc
lacg iiix fblhxvf nrkkol lnafzw qspzsn gvdy ipj zub uouseo
evukwkh ycjxxc lptwmf pmd izxdsos zrkavf pgjoy zwokg mpjiej
vqw ijwoy eaw wvq svmcq ccxi nyub ynlq eqornax uprt pygfe
plue okbbm btvm gba kutn jacjx ysqt lvx pcxxu qcf
pyw ffjfudq bvk hsdwdva fjnivhf odbmw krpgrj
hziesm bxa dceiwt tmvivjk snl fkh dahsxyx kqlhak lurtk
xss sswyxrg yqff dbkx kbxd mpzbmnl bzplnmm
uvz pjm ilrol pmj uzct ztcu brhkv
heiz jcn syjt zfvlvaq aflvqvz amcjh rxnitw
cxl nxvrn vjnz aewtr cxtko nnvcp ltptd adpxt zvjn fntklj
aymmm tuirj hzngq zhbh paqs kvpfo aqsp kmo acprw sabrso kdqmp
ndqjspv mmhp pndjsvq rti usm
ije oad mvelyg jadz ekm dao zdcmv
qwww tmwmdbb oxxfoza rgmf eonku brh gcgiuoi ojscn
fjedeek ohlax fiydku rbnxpg wfivg cdgs
axwbni hojye mwfe oyqknxp whdgfy ihku mbhr gagnz hehagxj
hibautd blnayq lnayqb gepml mgpel qunw
ircx oeb kujtip zbu ebo cmmn
upyqvot wbponp hnn vav avv tvrky omm
yzqsnf agbfsw dbxoya sfnqzy hqrxek qsnyzf oagyerm xxhukm
xzvk mvcwz oujr hell hoe xexa dqlpqt xdqz ucola hsvv tcmybhl
skldxr mzyol ybzyzd jnnxb rxncdy nkpwy fwlnsw omylz oiwieu fshv ngvha
jkwqf yxrox hejfoq orxyx
rijken xiwf mawqcfu erinjk jsi yyg mmu mdkfqb
ornjes krp eornjs enjros pyqp nnwwjl
wzd uqqo kyeli tikdle aykdjog uiz rbpnw mjxezf ihiz rlgyg
cjm ajqgvkz kfgyy dmczlc mjc kxcm zctyqgh ymsk jwhqfd czpqgan
vxkzvco owo qogj uyictoj kfr pyoo ejrru npluynx bvv jhhzu kuciwc
eqk pcsly kelu arzgoe trfo fotr cuaax
lagonw qvcssqz sdoklh uvovi sfrkmd hnvafj ltg wfjj
viwbkm hpwe kzzwrbr axjtlq mznin wwpjg unlwur
nuzorgo qfoz ydisca qxdfutv hzg
nqgge tobtt hjocx ntyqyi rxzkynw wrnxzyk ciscy trjt ottbt
yuii srawx gljxe eteogz kcu jlgxe tjik ktsnp agudqok jwol vfnyv
vgicg dhnrmxz sjhozy hlalx rutwq
nyoyoje kco hoyam hoyam tta iflud amh gdxcsj vqr fvsqcgv
xdmbtph ueen cskerl rxjvpdc
nricn addljzg obq rikez igq bxygkmv qmgojou uheubk qor
snzd ztusvr vrstzu mceddga hgu
vvrbfjg mcdhmsf ldtwl otuna gmjurrx jgrurxm rxmurjg yrioq
iotkvo sftfvn vvoit lllju xvlg rdsb ywmdf mzxigu kzq
sgqw gqsw lqfu wgqs xpiwou jurgucd azq wgaqpm
ijntzi chlnfj yjqatz hjflcn vys ofq oqf oadthe jrfw
mmc motjo vcwmod rpaszfk zgkkua bpja vjb htrk
bpfvvka kmger mnvvfl hakudy yfprdoo mvnlfv rgmek evnwg
mykpu juavkn cecdvi aszbi lxm hmps oaqoif
fshizd fsdzhi lvcq hhpb eavwno auqlwz rpv owcdojx amsmf qgnddd
pohmcn hlcxk qsesxh rncr
fgyrsis ldem avxmnh frpodq oefzn
plfpu qdyojz xdrzrjy kpv abkh fge bbnotvp liikmcu czvwl oyh
ovha muitw pzy edfjoo fhsxuh dliyruc dikcd cqem ywfy
exyry jtzqn tscr qbtxno cikk poqgr tnjzq eofe sxea anlikep kick
zcie purpw dmhhms bcdo prwup uprpw wfejgjd
kwtjc cmixp dodfwj hcgmmat pkeyspo ubnl ajxvj ffkh xvw
nvlgq oduus psufiqg lrwpn dleftn xtllqvf usgz
liarf sczsf sczsf wky qtzq qvve qvve
cit vtjsh jrhkyvi txj urmq hppx
rhblmxn rhblmxn lkgow dylurwc beyk gfcewxj ehpl disoe tjbjy lkgow
nbkrm jvk ffux ars agns bebic jzjfm kmnbr gptvtsa ufxf
hrlvup jaz tafyr qcgq wkd fiz bgsrx jmtcvo qkbvj
eontk djf tiafrng mtwat puainel nyjoh meynxbf eqdw
aspvmbx tgzuszm fpj xkl nzpr fjp vnomk byx sbtov tnu utn
ldyww gwmiddv hwyh gcgsdit gtgdisc suufl xsw dlwyw
sye dgbd wyf ixqzthx dgdb esy
nsdgera fqz xwbdgui ngdgbcd bcn qrdxml cwcmxws tncm mqsodj cqgk
estayas cocmbpv cdcf vygtswo aplwa estayas
ndc ndc wntr sfls sfls
gse svv esmi lcdii lnr kemrk gnk ildic blnqy wvn
mwlpm awkr sxsudub yauwww hnktbog fpnqc nmxoq yoparu tqjpkug nbipft
czwnkk hrodtmx yyzpil ooqjb cvxzfh
kwa wak gipak gsgrw
jyy fja jjk kuvoqdy urqx
doyu chgn gvtxi qjdigvy kxr dizwrjc sll zenl yyblj
epxeqih kfi hlog pakk kkiidrh hiufw wuhif baqzxzi bgcd phi jzjdxjp
hllhyad sodc nyrtfe kygof hyyqi txddqg wcwxvnt ewqmj wwv
vxymuoe caat diqwbo vfruxdf sqniefn hetcbl nvtttu ouesb
yvoez pvthzc tdowuci wjijicn fhpmq kfobag yctdwj
xaugkb rprkg tidpx pjk tpwwm pbcfhr wmwpt sfynrl iouaw zbnyu
auakc culuxg bffg rodyhea ixlmtfb jdurl szoa
xgona fjzho buh khbvti ddh mgj ptgaqps
dqldupd udpldqd poku gfgpcg zsvk grvk kntx jih uwvxdvq sivk
mwdnq wmqdn uzto mdqnw
alvfm qxqo thwru xqqo jilnsgs rnonk fwntuby ogbha
gvxlxyf cdpv khvpka kgt gshlaa tenb
mtgvvxh mrjrsd truk rrerzx tujweaz
ozepw gsqkr rtmmc cmrtm
spnthg xhlzuu xwcrxz aqqejhh bpzh
ectdftk rgp mkp vxp pevriz wkgfkaw vfygj peg gep wjn
bksbu ywsszf tsbrps vxicr hfustju ynnlbo
sio urbvf ujezjk vkyc ukjezj bvrfu qwwgqmw uqfekvx bzipxus qfumwh
druru kycweog ycmef rjyy fkgp
rmf ifbip rsztco coju wlr bfbmsug lwr bsufbgm nwmp
jjuxtyd yif rkldsvu binq spepa mfg aszm
ghilaau ncm sgbavz omzeotz azukf bgjw zqzo gjbw pld
gtog iqheik budeu guvljmi
qqlj jqql ttk xcxu
cfq cfq kpagib dxfxufw hhksbjh gpcp
xkeax acnia jjubfc mhot uxlhh gnkj pavta rciondm rkquh xudqian
wqhqzg psqh rnnc uujlgq
hpjpaoa maa rdndl xewqj nmagwx xewqj hxuyvou xziv rdndl fbxmbz hmfwghy
dtwnrca hbfcptw qrmvat sdatx les zwizogq
bodiwzg sgoas fsf wgkrn zgbdowi wfkz
ngcsg grtao wcfxpyl gngcs fxwycpl fkpt
txvngo vxngot tkoap zqjc qzcj oeruix myh ihgdfik qtt
rxeh fcbnoo rxeh lve wvoc pmnxej dlcbrh rztt noibg
zyvq lwxqu oyjv bvidmf wxuql
wzc zcw czw dnhkvrg nzslrf
cfgl uwhxu qnsfmt tgyabes mqnq nkitq hmcvxlt qqmn yzmb uomqp
lwziur hgmdmv zuvipkp vir apr gfaq zeo dunat mqgafzg
prq pqkr xlrw njf ncqni kgpoma cmtklv
jwfuc poz opz fuple
fgleub lcgnifu lkwo kftbc onvwvdx lukpod xgmh rnj
rwqvv ezjmoni llq ekd cdvv kzcci gzsj vuipv fnw
rtnua gbnzg kqtogns iozzwc kjpzz kiiurey yzlvzx cpy xrue
fexcjmw ebwssx ewbcgwd uwolou nfdhic vupiykn jss djoo xftbkgo
idf ipvmez qyevwd wfsjxja dif dig
szpbtsa bssaztp sptzasb qppgz odur cpmn wpmg
pxn zjmq rbnr azwstzm mln upaqyty nxp oge nlm
bfaryqv hag phtvh ypi
epeeog lip zqio wuehlnb bau sbd dsb
xbrrp sej agrqnpa aarpnqg bnwyi jbn
uqmsvd asmuyy czxviw pznnmvc
sddwmek wnaea iwphupk sabo
cingdks ksh mtyip zltgafm dflkcd wbdnqup uokm gmxpyd libz svv akce
qge ewv dkabkmb xcpi nrkmsu mkmb djvamg mhhrwjh
krjt etfhm bxzatw zdkvz ehov seyxbw mkiirs plzoplu sogmwb wodfcle
qwea adibdp emo homrd pjcrhlc eqaw kqsrp rphjlcc
gajzo nwjg qxjra jztcnir ijvjwez avxb afz zyywqz kcszgh elmlkfh
lbz ozia bctf bumoji anhil rta xvit
ejybire ypjl qevak fzalx mlh qxlei zib
xmzas kwojjz ntrnrw nbmxlv mdgxs xjhxg suo zdcrxl qkujisz pxmu
eezyd unrtm wyu vhufvto rpb isfcy ygh hgy
nszvbzv ebtt memrsva ebtt qwcaq bhbas pvzfbov ppjbdy nszvbzv jabvrp
rlo zbmi lugvu yeby
tfcd tvl faaq mnural nyarh xnxk ctdf bodz
vwdrhc gub bgu fpcovx rcvwhd jukwsue
aekrhi lpknnrh bett tkib ioqrap igwnst aekrhi lhha
acg mknhazp pcgjuk tajplv
masq fyjkn agq qhxbbl qga npzj fme xtihic rntisg iqv aqg
ipagh fjth mswztpi iexd cocojy vhqrla joe wrsrmw
njztu tsh auqrxca zpp
jctn webxi haq irrr qox irrr webxi
reaw axmnvd voakf lnz ftbxfh zjyxzl pryfjpv sistgb pov mshs
gsy ctsngl ptmnyx vpjx zpvtori pfu ioycdrq
aobdtlj osdnrth sgqe geqs qegs
oamrlxk ygbb rkamoxl nztl sarbmtj yqupjt plu sbtarmj vpa rxea
yvhgp yznko epwpza gqrsod rilukp cglhomj wnaplu ugvdko qdr
cggztg ajw gggzct ubmiefj kpa
rel lvasbh kobm mdnzla pwnyj ehep gzx nhjdnsg rxa
qaz gook rplqwh vsht
dhe aneq ivrn awekad ckcbt zsqca ehd rvni oulwfuu
oxgzzow wntz tkqaoi oxgzzow lwkdpgy lhd aekjasp tkqaoi dnhaw
alxghco cpanoa onjh hyeyebe whxn zfu zozbll gojn
zdqulsa dlqsazu zqudals sfedw
rydtrsv rrtvysd fvyza drdgh lsfzt blnxr cnxe tslzf iijyds ylcxn
cczea nxx kwol kopaza wuvr cyvoo whlicv
zbmrwdq tlzbevx jwzpsc uvkwpd bmss rbzblj
jogx jgi gji hypmtkg ijg oscjv
flkoqja kwmrqv wzehel fvmcfap mkwqvr ivwxg jqfwdvo hweezl
vgjg nzucho nuohcz ggvj tmxci
fqaqx zeybhtg bxeic lftuqp wzuerz sww qfltxk
keiy myrvp blkxcg lncqmsu diittlg fqrf digrel cpwrk ipan dkxb bymlzo
owm irygdz pyhj mow wmo
noul pbvvt zcv ueqyjl zhetlw lpjfhli
felvwb wdykz kyibdz haq qkouj vuav oztyqh
dyxo njcr hcuk ysrr pucw qbajztc
ooyaz pmt hqwu gjx tmp tpm pwz
lyhzajz dfot avyifo kdwka pwypcep kyyw tirlku zdpjmft
aexle hfxo dacwvcy xsiotyg cifq ibupshj aktt rzvf pgafj
pxubhw ibpm jxtxg iwnssf osbpj
exmtfyx blbfg emrunru zkuhoi lfzn zrj unmcece phuppi
icomb rmy mvsqqkh zwjubz lumq wekx
cmdgs gsr pfhqx pfhqx cmdgs pga
rpyf jejc adaiou dutv imbenyu dqw zhebjhu pryf vtxs yprf
cxj roprjn rqoh qacagru snxd
rczvi hfpl luc yowgj nvavlhw vjudkmv dwu teq
klwc cktzh ksnvswl nsgeu xyohp mhs fxnjhm fwrcg rdeadkx cim
ounvb vzqje ujctzzk iyy vxck ebtvbqr uswsmcr jveqz qejzv jmi pboq
lwffygh mqsh vnnj ufz qhms gqfuxo lurzmu
buf psdluck gapwoo wgll sbfavbc lljfvzx cdgo rpt sfvabcb
svefr kubbri fervs nboi zkvq
jwr vtc zkcpzb kczbzp cdned pzbzkc wigjuak fszgweu odflfek
vwdqm khnnj plokjg vnce venc vecn yzxtgb
tawl yrhoz tawl yrhoz
vvehsl kdhzgme rix rcs btm pxnlsps vlhesv sxpnslp yqjtool
eqpyw kpmkcyw wqhglxg ajfzo hbd qvmhy nhokah iisqvad kxuyd fxek
jsz txhwhah hxt djnvl srylveu pxp dzmmn epek tzs
joyzql jqczueb rtdyw fyc fjirfyn tjcalz joyzql fyc
pjrmiz xwnmwns kcqjuut zfgxhdr octwn kqppg zhfgxrd wmwnnxs
ema yqxqs aljjo ajloj wozb
urgmhiz epqj vhhaxdm ptlsvig qzbmm cumbho lkg gyzmg eaopyzf ncfy mqe
ijvwvo oszkees ugvyk hjdj ftip itfp
ylfw qutzdj mgqp cyjss yzsdqqi iykvs fyor sthyqp mrjtzee hgo zwqbtgk
bkfkns gco bykzc mje dwmkrwt ljegqor yxjxp oaleuu
xeltq ggyqis aud frtyxhx iwz wiz fwoxz fozxw
zdu nwduqsa nced iphaaxo
bqjj oah ezd brhgxrc pmkz kdog exw
ihatt hck iepn egemprp wrz wzcuo xjzeaa wku ivjvihh
cwkuof bmj qmxd qbtms zgdei bsqmt ssndhw eeenku lcsqy bvvodr
tek zsgytci vgoun kwwu
jcxvp ijxc buqgix uil zfoku
ggndshq bmjeo yqaxtik blspz yofh edaroy
ipvtxh ouye elln dllvx iqza nhwf zyfw pvlky
iydcx gvarm gvarm wegmiy
sfjd liiflle mulboe qywzs tzbns trojl pad mnfcrhb sltb
gthqj jvpsof jwlfyeg jwhlfj
qckv umzrge gnzc mnr xde
gvgxmhv txnait taxint ius iboqdj
vsfex kbpvsby qembkb efxvs vhflzvm eaazg dyg bbmekq
wxpfk xwfpk xwkpf cjsyi
knzg eefq feqe seppop ttxz qnqfn atgsy cch mkjlbwt uyhct
quzw jbiw miqehe qvf jyipqh kzcjxyh
teuvzf tdtwoi pcuafa cwgjk ccur lgmqv jpjdkk efrnw uloqn dpkjkj lwloeph
yaffjy xntstsv gygq sxttvsn tvnstxs
cvbmdf pfrfkna wupv van iocb hsiyke obspj ytyfkl hbsqtij hkcw
oeddmnu koso mdodeun ybe mhjbmwy ubejz soko yxvuv
nylhy ylnyh olb vcdik
gsp ilba llnu jjk urbvuma qzypf bkceotg ezxq hyvjngf
tfnegyq rue waeif tfnegyq mvqm
wvgnsk cpd oib wrdfaz kohwgkc kzzig hogkwck gkizz
fecuuyp yfq bvanvxb cjeqwf unw dccr qzh zqu voakj
utoazh bjuq kmhcre izmny mirorsy twnl jyoc
fnnpd dmr ccgu eqgewc zuqivf
kkxiba qdabuen oikaz dnuywmm
aogud adugo uzcglpj lucv dgoua mdsqa mvrg
lymhv sof hvyml mlvhy nit
chu bwxp xpbw ghaix seklnc ola zofnrwt uch
wtt abob vblijtd oabb qjws
uozrpw kgf gxidxm uehdr fta pqakkrq atf fat woaolk
gaee voshd ghlyy emvzlkg cmcgk tuwlsj jwtsul znrta mjieqph glker
qiugxas gkg cbzmoz kahs obzzcm
puz omcokz gjc heuqb
dgndhb wid wdi scwnrjf juaisgo eivaw hgdndb
mgcrd hnqg pkpeb vprxcp
atlcnzp fyp cpkivxi bzj ypf cqpt bysu
pnd jiitmzs csw mxnpck vxutdrs ivipzy cws xiegsy qut
txlk avcvbuu hnq yyriq ajyswd urgiwc
qgiqut gvblizs giqnfrk tty mvoj wpikl giqnfrk bkdpndu xztmxn hsmqxf
llthg zjslki wilj rcyfois bavz hrqxn
ytbw hlkl vip skycogy ejiirhx
ndmtg bthlbw lsoq cvlvo sqol sqlo bppl sdkbls dtpyzrq vgm
psm xpj xjp lqi spm gqirw aglpj
htg fcchvyt xffev szdu lieadft
nbjo qohgzu vofg vvild dbtyi pdolxn plnoao jxze xlpbxj brajzg
urpp jjv lihmvp ivkwdqr sesyp ypbry qok sesyp ivkwdqr was
yinepzv qvnzdtf apv ucxo bdioo juga hjfsyl hmowo avc
dmiv tplae iiuiaxx tpale pyzkc
giwhst mpexd byfyc swuzkc
yydkwp xuu vjya kav ujmcxy qrtp zvlk
lsvdyn tkw qxu omvlc wwmfvov mrgcoov dhpu tfair hupd zbx njzgwtw
zuz rsxc xsrc gdwwf nycsv zzu kcu
unlvzv jerqqgm nozma ykbflj qihqkx
pctffo begf ivrvy ezru mvqt waocq
tubtuk gxkc ikgw bjrird kxjebbh sbjyc yafkd khqajmt aclpmf gqfo yrpf
rdt vrxa fyudo myeosb ursflwk
wbjras edlbwdp ctobtw jbvtvcd xjgoo cmunxm mjtbpi klovx bypmsab unc
xckml uztr htublq vilabvr jdiwus qejxur evfw qqm
tzqq tzqq wkb wkb
dgmg ljzc dgmg mbmco cgze qsap jccvot uors iiq
rwvac woylk dmn teorprx nyuvz hcwwxlj lvej drbjo asjgq
ljen tpfl vixcivr guaf lnje waim jlen
djgaa janhi adudm yzv zkcb xqw fgvrz
kpkjoon ggzx skp rqcsw xgzg zgxg jtf ghc
rtnyxo qixfd nphekk mouzk gny fpzquw qgywx rpr gqydze
gawdlv vrivoof rte iyp gaih sfzplm
csojx wzojode uzy qulr lylmb guvtkwv
ovxj aamms ftxo ebckdqw wqvsdci jwfqxks jafrcrn yyomrot
qnu jqwr ywudxk qpsez rdc kiyfz iiecf dthxjjb bown
typ zxcvjo rip acjhl paaab qhqipg xkguye sbxy pomkvn
ofvaegv hgak oafevgv hkemar rqkha grklnsp msvkkku rekahm bxmjnw
ahoihju sdyn phi uhz lupbx
lavt jef klmq oqyfpf kis nazul ymezxek xpla fxyrfnt
nwnagwy hvpjqfg sgm ungfstr gso owqqxjh
hey hye ipyrt qxmthg jth wpbr hxgmtq cvfkfux qykdzhk movcfnl vxyoc
zsras abnrj fgaczuk ssazr xzf cnxu gns wnqqy dwjh szars
uhb zanlvh lvdotkb xekl kcofo
lhx iccy ibkjw ciykxaj imsx ehamqlz iwzapxc rhaltv
pofit owmpqej vwrobh jvox gdqehss yyxd styu tfkm fiotp
ecz mdpoqsv mdpoqsv yxx rexok hcfll yvury hdhcfu juhkvpt rspnfj hxvgdir
ohed mtigaoe eodh agmiteo
vjvv hfco cppbxtw hawsjxz ovlsq qgs risgwhg auhj
togivgg czrtvw ccz wzvtrc bse lsk
ndc ndc lrfi iyleol nchx jxpv xdcsfmp nnx wtvq pih tgc
hzpf sur zhfp klfmhx lbuidp xiqimnf
qddpdk trfxpip pnsowj hidgvnf prur rsrautp aamykfm fysqjmq xwzjane mbmtxhf oqctt
lfd eops govslp ultbye vrqai hcjkcf snpape
cbok koumkad otpozb pqcs emilpe wpcyvxd bock
spjb xkkak anuvk ejoklh nyerw bsjp zxuq vcwitnd xxtjmjg zfgq xkpf
juo pmiyoh xxk myphio ogfyf dovlmwm moevao qqxidn
'''.strip()

# part 2

# abcde fghij - True
# abcde xyz ecdab - False
# a ab abc abd abf abj - True
# iiii oiii ooii oooi oooo - True
# oiii ioii iioi iiio - False

class DojoTest(unittest.TestCase):
    def test_validate_phrase1(self):
        self.assertTrue(validate_phrase(['aa', 'bb', 'cc', 'dd', 'ee']))

    def test_validate_phrase2(self):
        self.assertFalse(validate_phrase(['aa', 'bb', 'cc', 'dd', 'aa']))

    def test_validate_phrase2(self):
        self.assertFalse(validate_phrase(['aa', 'bb', 'cc', 'aa']))
    
    def test_day_part_one(self):
        self.assertEqual(day_part_one(example), 2)

    def test_day_part_one_real(self):
        self.assertEqual(day_part_one(input), 466)

    def test_validate_anagram1(self):
        self.assertTrue(validate_phrase2(['abcde','fghij']))

    def test_validate_anagram2(self):
        self.assertFalse(validate_phrase2(['abcde', 'xyz', 'ecdab']))
    
    def test_day_part_two_real(self):
        self.assertEqual(day_part_two(input), 251)

if __name__ == '__main__':
    unittest.main()


# Ingrid
# Raphael
# Claudia
# Luciana
# Leando
# Matheus
# Pedro
# Christian
# Caio
# TCarreira
