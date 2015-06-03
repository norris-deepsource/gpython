tenE5 = 10**5
tenE30 = 10**30
minInt = -9223372036854775807 - 1
negativeMinInt = 9223372036854775808
minIntMinus1 = -9223372036854775809
maxInt = 9223372036854775807
maxIntPlus1 = 9223372036854775808
def assertRaises(expecting, s, base=None):
    try:
        if base is None:
            int(s)
        else:
            int(s, base=base)
    except expecting as e:
        pass
    else:
        assert False, "%s not raised" % (expecting,)

doc="test overflow"
assert int("1000000000000000000") == 10**18
assert int("-1000000000000000000") == -(10**18)

doc="test int, base given"
assert(int("0")) == 0
assert int("100000") == tenE5
assert int("1000000000000000000000000000000") == tenE30
assert int("100000", 10) == tenE5
assert int("1000000000000000000000000000000", 10) == tenE30
assert int("11000011010100000", 2) == tenE5
assert int("1100100111110010110010011100110100000100011001110100111011011110101001000000000000000000000000000000", 2) == tenE30
assert int("303240", 8) == tenE5
assert int("1447626234640431647336510000000000", 8) == tenE30
assert int("186a0", 16) == tenE5
assert int("c9f2c9cd04674edea40000000", 16) == tenE30

doc="test int, base=0"
assert int("100000", 0) == tenE5
assert int("1000000000000000000000000000000", 0) == tenE30
assert int("0b11000011010100000", 0) == tenE5
assert int("0b1100100111110010110010011100110100000100011001110100111011011110101001000000000000000000000000000000", 0) == tenE30
assert int("0o303240", 0) == tenE5
assert int("0o1447626234640431647336510000000000", 0) == tenE30
assert int("0x186a0", 0) == tenE5
assert int("0xc9f2c9cd04674edea40000000", 0) == tenE30

doc="test int, base given, -ve"
assert int("-100000") == -tenE5
assert int("-1000000000000000000000000000000") == -tenE30
assert int("-100000", 10) == -tenE5
assert int("-1000000000000000000000000000000", 10) == -tenE30
assert int("-11000011010100000", 2) == -tenE5
assert int("-1100100111110010110010011100110100000100011001110100111011011110101001000000000000000000000000000000", 2) == -tenE30
assert int("-303240", 8) == -tenE5
assert int("-1447626234640431647336510000000000", 8) == -tenE30
assert int("-186a0", 16) == -tenE5
assert int("-c9f2c9cd04674edea40000000", 16) == -tenE30

doc="test int, base=0, -ve"
assert int("-100000", 0) == -tenE5
assert int("-1000000000000000000000000000000", 0) == -tenE30
assert int("-0b11000011010100000", 0) == -tenE5
assert int("-0b1100100111110010110010011100110100000100011001110100111011011110101001000000000000000000000000000000", 0) == -tenE30
assert int("-0o303240", 0) == -tenE5
assert int("-0o1447626234640431647336510000000000", 0) == -tenE30
assert int("-0x186a0", 0) == -tenE5
assert int("-0xc9f2c9cd04674edea40000000", 0) == -tenE30

doc="test int, base given, +ve"
assert int("+100000") == +tenE5
assert int("+1000000000000000000000000000000") == +tenE30
assert int("+100000", 10) == +tenE5
assert int("+1000000000000000000000000000000", 10) == +tenE30
assert int("+11000011010100000", 2) == +tenE5
assert int("+1100100111110010110010011100110100000100011001110100111011011110101001000000000000000000000000000000", 2) == +tenE30
assert int("+303240", 8) == +tenE5
assert int("+1447626234640431647336510000000000", 8) == +tenE30
assert int("+186a0", 16) == +tenE5
assert int("+c9f2c9cd04674edea40000000", 16) == +tenE30

doc="test int, base=0, +ve"
assert int("+100000", 0) == +tenE5
assert int("+1000000000000000000000000000000", 0) == +tenE30
assert int("+0b11000011010100000", 0) == +tenE5
assert int("+0b1100100111110010110010011100110100000100011001110100111011011110101001000000000000000000000000000000", 0) == +tenE30
assert int("+0o303240", 0) == +tenE5
assert int("+0o1447626234640431647336510000000000", 0) == +tenE30
assert int("+0x186a0", 0) == +tenE5
assert int("+0xc9f2c9cd04674edea40000000", 0) == +tenE30

doc="whitespace"
assert int(" +100000", 0) == +tenE5
assert int("+100000 ", 0) == +tenE5
# FIXME broken in lexer? assert int("\t\t\t\t100000\t\t\t\t", 0) == tenE5
assert int("	100000	", 0) == tenE5

doc="sigils"
assert int("7") == 7
assert int("07", 10) == 7

assert int("F", 16) == 15
assert int("0xF", 16) == 15
assert int("0XF", 0) == 15
assertRaises(ValueError, "0xF", 10)

assert int("77", 8) == 63
assert int("0o77", 0) == 63
assert int("0O77", 8) == 63
assertRaises(ValueError, "0o77", 10)

assert int("11", 2) == 3
assert int("0b11", 0) == 3
assert int("0B11", 2) == 3
assertRaises(ValueError, "0b11", 10)

doc="errors"
assertRaises(ValueError, "07", 0)
assertRaises(ValueError, "", 0)
assertRaises(ValueError, "  ", 0)
assertRaises(ValueError, "+", 0)
assertRaises(ValueError, "-", 0)
assertRaises(ValueError, "0x", 0)
assertRaises(ValueError, "+ 1", 0)
assertRaises(ValueError, "- 1", 0)
assertRaises(ValueError, "a", 0)
assertRaises(ValueError, "a", 10)
assertRaises(ValueError, "£", 0)
assertRaises(ValueError, "100000000000000000000000000000000000000000000000000000a", 0)
assertRaises(ValueError, "10", base=1)
assertRaises(ValueError, "10", base=-1)
assertRaises((OverflowError, ValueError), "10", base=100000000000000000000000000000000000000000000)
assertRaises(TypeError, 1.5, 10)
assertRaises(TypeError, 1.5, 0)
assertRaises(TypeError, ...)
assertRaises(TypeError, ..., 10)

doc="conversions"
i = int(1E30)
e = 10**(30-16)
assert i > tenE30-e and i < tenE30+e
assert int(1E5) == tenE5
assert int(b"100000") == tenE5

doc='unop -'
assert (-3641149227530018725) == -3641149227530018725
assert (--292603994644321966505444317896) == 292603994644321966505444317896
assert (-4904044993697762927) == -4904044993697762927
assert (--632185230151707693891374184935) == 632185230151707693891374184935
assert -minInt == negativeMinInt

doc='unop +'
assert (+4719256603434449864) == 4719256603434449864
assert (+195374739125443499408085954061) == 195374739125443499408085954061
assert (+-137092745724873690) == -137092745724873690
assert (+-430653255201251344638775153640) == -430653255201251344638775153640

doc='unop abs'
assert (abs(-7673338730320487519)) == 7673338730320487519
assert (abs(431474133520832215634480054884)) == 431474133520832215634480054884
assert (abs(-8320419210463143380)) == 8320419210463143380
assert (abs(-871729681639787335406279216780)) == 871729681639787335406279216780

doc='unop ~'
assert (~7925672294126702091) == -7925672294126702092
assert (~993193843674866651947808856918) == -993193843674866651947808856919
assert (~-6763809348657986856) == 6763809348657986855
assert (~-874993321372974196107431462962) == 874993321372974196107431462961

doc='unop float'
assert (float(-6450284370390530229)) == -6.45028437039053e+18
assert (float(499622087565400960139933324516)) == 4.99622087565401e+29
assert (float(-2669664172783636500)) == -2.6696641727836365e+18
assert (float(586226139343958088885818537791)) == 5.862261393439581e+29

doc='unop complex'
assert (complex(8933717091386849423, -1231948596602428130)) == (8.933717091386849e+18+-1.2319485966024282e+18j)
assert (complex(-112003440633045743638450994095, -870659418246097554269256403682)) == (-1.1200344063304574e+29+-8.706594182460975e+29j)

doc='unop int'
assert (int(2996679482204208157)) == 2996679482204208157
assert (int(-636881448634320701973025729785)) == -636881448634320701973025729785
assert (int(-399006150144049561)) == -399006150144049561
assert (int(740151207744511492800159495328)) == 740151207744511492800159495328

doc='binop +'
assert (5043896883918350915+6496176714601634408) == 11540073598519985323
assert (-176718547129178599967375295570+7678395671186597946) == -176718547121500204296188697624
assert (-5879237725499463452+889376233866105569867940154332) == 889376233860226332142440690880
assert (98658199509207548571836763459+387058448750433331636504801219) == 485716648259640880208341564678
assert maxInt + 1 == maxIntPlus1

doc='binop -'
assert (4772705708577961331-5705965083165035349) == -933259374587074018
assert (499315272741938423066045562929-926208313550490229) == 499315272741012214752495072700
assert (633856083481094280-159764016488340676251173465833) == -159764016487706820167692371553
assert (-759163582033099930583898215388--622263396021282398807422972137) == -136900186011817531776475243251
assert minInt - 1 == minIntMinus1

doc='binop *'
assert (7585194605759361091*-8295333006057173661) == -62921715170522459096653183904593424151
assert (-211632533027288521429006868069*-5653252500022028208) == 1196412146422513287446928630654295043023252490352
assert (-2705655979939764051*498507611145963097629681977143) == -1348790099142561628919972802250477720678595086293
assert (12870925392758904855337167358*-178373424945516810458926560056) == -2295831044524626990552921549255668683393970507650109852048

def approxEqual(a, b):
    assert abs(a/b - 1) < 1E-15

doc='binop /'
approxEqual((-3532857779759245605/-5673394357858672063), 0.6227061890851289)
approxEqual((-178492911371678086128436750100/4194391310236118458), -42555140464.85806)
approxEqual((8320894759108355333/688889843982879461528409053334), 1.2078701452470752e-11)
approxEqual((647075625851211057828684328038/-326063662711018305247049652642), -1.9845070145847477)

doc='Int divide signs'
assert (123//20) == 6
assert (123//-20) == -7
assert (-123//20) == -7
assert (-123//-20) == 6
assert (123%20) == 3
assert (123%-20) == -17
assert (-123%20) == 17
assert (-123%-20) == -3

doc='Int divide signs exact'
assert (200//20) == 10
assert (200//-20) == -10
assert (-200//20) == -10
assert (-200//-20) == 10
assert (200%20) == 0
assert (200%-20) == 0
assert (-200%20) == 0
assert (-200%-20) == 0

doc='Int divide zero'
assert (200//201) == 0
assert (200//-201) == -1
assert (-200//201) == -1
assert (-200//-201) == 0
assert (200%201) == 200
assert (200%-201) == -1
assert (-200%201) == 1
assert (-200%-201) == -200

doc='BigInt divide zero'
assert (2000000000000000000000//2000000000000000000001) == 0
assert (2000000000000000000000//-2000000000000000000001) == -1
assert (-2000000000000000000000//2000000000000000000001) == -1
assert (-2000000000000000000000//-2000000000000000000001) == 0
assert (2000000000000000000000%2000000000000000000001) == 2000000000000000000000
assert (2000000000000000000000%-2000000000000000000001) == -1
assert (-2000000000000000000000%2000000000000000000001) == 1
assert (-2000000000000000000000%-2000000000000000000001) == -2000000000000000000000

doc='BigInt divide signs'
assert (1000000000000000000000000000001//100000000000000000001) == 9999999999
assert (1000000000000000000000000000001//-100000000000000000001) == -10000000000
assert (-1000000000000000000000000000001//100000000000000000001) == -10000000000
assert (-1000000000000000000000000000001//-100000000000000000001) == 9999999999
assert (1000000000000000000000000000001%100000000000000000001) == 99999999990000000002
assert (1000000000000000000000000000001%-100000000000000000001) == -9999999999
assert (-1000000000000000000000000000001%100000000000000000001) == 9999999999
assert (-1000000000000000000000000000001%-100000000000000000001) == -99999999990000000002

doc='BigInt divide signs equal'
assert (1000000000000000000000000000000//100000000000000000000) == 10000000000
assert (1000000000000000000000000000000//-100000000000000000000) == -10000000000
assert (-1000000000000000000000000000000//100000000000000000000) == -10000000000
assert (-1000000000000000000000000000000//-100000000000000000000) == 10000000000
assert (1000000000000000000000000000000%100000000000000000000) == 0
assert (1000000000000000000000000000000%-100000000000000000000) == 0
assert (-1000000000000000000000000000000%100000000000000000000) == 0
assert (-1000000000000000000000000000000%-100000000000000000000) == 0

doc='binop //'
assert (5744409969029584448//-1220411214895984398) == -5
assert (801848568806426077475668423535//-8085312908136062722) == -99173473918
assert (-5721542802125298347//-987715757830780227623113033880) == 0
assert (457897615381227167341108005859//-353379489795893751557547859364) == -2

doc='binop %'
assert (7341566843809298600%3978427562660778191) == 3363139281148520409
assert (294375077667396199949508874162%7786366607165572976) == 345835433804354002
assert (6316821303028268687%-707212250464589439185037502466) == -707212250458272617882009233779
assert (-119459441634706255601601571546%17130399946665545258117887219) == 453357991952561205223638987

doc='binop &'
assert (-6956530093671002017&-1100238534807351779) == -8056622384673947619
assert (712141139855031028826808567100&-3466734559984678908) == 712141139853870138059506319364
assert (-958344426204952855&303542205609898406718869854750) == 303542205609319632402841076232
assert (355034581684588784693862572442&287772036208920781632348286363) == 10219276708218799276098101658

doc='binop |'
assert (7965431001389611619|1849846454287559969) == 9199725731967893347
assert (683172859749258174808945136942|2247131280186245284) == 683172859750844075909444507054
assert (-5116595344598559097|-131652429399965032737131618852) == -4828083109504639009
assert (-339775496144585975617578653951|-184446805349712628578851904802) == -20380762284375296564171659297

doc='binop ^'
assert (2545829758095679914^8055640288882183490) == 5521404917032201448
assert (480980618054282503813772524041^2353633394259153960) == 480980618051947606252269530657
assert (-8232850711436597206^602431520096850242713292386624) == -602431520100182785464423949974
assert (-241755526833236442590948256392^-809507466694559910195393295880) == 731177214830218925010940271744

doc='binop <'
assert (7940136388260479232<-2087992292719724893) == False
assert (-761658560632114946921324188115<-4855041057001917563) == True
assert (2709307496615609646<524706887321736910977030614590) == True
assert (-478654018968085006374520805012<-205760262333647629025159523193) == True

doc='binop <='
assert (-2960454357022229165<=7018183421775698190) == True
assert (-892948923157158517053771781709<=-6622708745679384977) == True
assert (-1514894179518983839<=750787353379252731354931179885) == True
assert (-846946116133133230665953505989<=284650312428627609386919918324) == True

doc='binop =='
assert (2955997980781661862==-1499357928395595538) == False
assert (-302271288319099570091787176653==2015027968383056819) == False
assert (3011752727817158863==577731280510805856117314968162) == False
assert (907092104740266583526590529148==-799571854410979196284475879498) == False

doc='binop !='
assert (3386015315988032852!=-5608508942137887730) == True
assert (-745305895464077650266851470408!=-8539685374022941321) == True
assert (-5317317313090021681!=-114212774855216737469170172753) == True
assert (-908995212536626797570404026271!=-147697378208618615522451550378) == True

doc='binop >'
assert (-190916179417055978>-6299240474781674786) == True
assert (57574013199287063157373829904>-4023693064770928217) == True
assert (-6106342554898627674>-474789685238266097593786231577) == True
assert (-790384769302161802686899845423>-495246291234156026839257836584) == False

doc='binop >='
assert (-1470779481516181109>=-6348900824003652472) == True
assert (-440551450479675290557908914936>=-6472730597673555201) == False
assert (-6556625884400083995>=782436112302036748240769291524) == False
assert (-574488083164911538611688743004>=-853994965828610256633190646608) == True

doc='augop +'
a = 8664105629443693284
a += 7113883675992104545
assert a == 15777989305435797829
a = 978339526228162862292057781093
a += -2522622159398673012
assert a == 978339526225640240132659108081
a = 2680614542928150822
a += -825936231041977519481809439923
assert a == -825936231039296904938881289101
a = -772174371503797792823707468916
a += -47481568609158952841069881994
assert a == -819655940112956745664777350910

doc='augop -'
a = 3700728350381052414
a -= -4539747672590686710
assert a == 8240476022971739124
a = -879375568286136979365527364963
a -= 239823184847376978
assert a == -879375568286376802550374741941
a = -2852077928926906952
a -= -756153282423717242985372373350
assert a == 756153282420865165056445466398
a = 640391618793916787825857766812
a -= -502217520639072327834011438121
assert a == 1142609139432989115659869204933

doc='augop *'
a = -5536570711931389036
a *= 3566226886331832531
assert a == -19744667330967094839909486618161530116
a = -248442852356045238077580833251
a *= -2694546452526643205
assert a == 669440806471582277037570200285850884121877209455
a = -6080372945234953573
a *= 650799868747677831332786597102
assert a == -3957105914695839071682346858402145768425626345446
a = 140666035072350752635321722445
a *= -938395150219259672214812866267
assert a == -132000325112466234113556619504113932122933901024097877262815

doc='augop /'
a = 5069783398047525860
a /= 6462058788020393130
approxEqual(a, 0.7845461584852927)
a = -496438599010924977014433151307
a /= -5295935637927610606
approxEqual(a, 93739545370.53056)
a = -5904567046213407597
a /= 463384043422614648161788362438
approxEqual(a, -1.2742275289847076e-11)
a = -643428879815902445901862650298
a /= -705476577911651649854533260835
approxEqual(a, 0.9120485356446241)

doc='augop //'
a = -2955145545873784447
a //= -8398154603067315189
assert a == 0
a = 764874707978666366468709717939
a //= -637453031923767022
assert a == -1199891866026
a = -3225133016360684087
a //= -106830573980181067612866984034
assert a == 0
a = -1017486275496211203702167393
a //= 707873786594465355113033731247
assert a == -1

doc='augop %'
a = -4898359889955701722
a %= 2586537256564406544
assert a == 274714623173111366
a = 165600857868102801319021818388
a %= -5550996453372617970
assert a == -525692049140908922
a = -1667139790609035866
a %= 132512297800301099457101240885
assert a == 132512297798633959666492205019
a = 1223018728310354788098388057
a %= 756727576419043673398940776835
assert a == 1223018728310354788098388057

doc='augop &'
a = -926347478023783305
a &= -2958038997734684053
assert a == -3305392399101982621
a = -691803630231515156014634566825
a &= -6736510577773221895
assert a == -691803630237949744906139311279
a = -5512195446257941412
a &= -209381620830100815867782757302
assert a == -209381620835584018837378169784
a = -207712289586678908828795978537
a &= 596885457784576388820639638043
assert a == 396295555274571585218510135315

doc='augop |'
a = -1845198749314266854
a |= -2653805823599768653
assert a == -40592131194500165
a = 499789694432688152965491470418
a |= -6552560667513365772
assert a == -191995691798922506
a = 1135630826982630338
a |= 27502936923253416276111159669
assert a == 27502936923776414513069061111
a = 316647332765525694715619309364
a |= -530314999208573746658426751363
assert a == -317079789071547601654674098307

doc='augop ^'
a = 8615064928073168299
a ^= -5670184157960583260
assert a == -4124824036774743537
a = -558550360774792683953403218454
a ^= 3593248379370484836
assert a == -558550360771355514102867328626
a = -6160185234911746084
a ^= -906153857024751632742732815082
assert a == 906153857028009239728516825802
a = -924408397612725457073046580831
a ^= -236051837221964566609479775048
assert a == 737915270162409905551579208985

doc="<< and >>"
assert (-1 << 10) == -1024
assert (-1 >> 10) == -1
assert (3 << 10) == 3072
assert (3 >> 10) == 0
assert (-1 << 100) == -1267650600228229401496703205376
assert (-1267650600228229401496703205376 >> 50) == -1125899906842624
assert (-1267650600228229401496703205376 >> 90) == -1024
assert (1 << 100) == 1267650600228229401496703205376
assert (1267650600228229401496703205376 >> 50) == 1125899906842624
assert (1267650600228229401496703205376 >> 90) == 1024
try:
    1 << 100000000000000000000000000000000000
except OverflowError:
    pass
else:
    assert False, "Overflow error not raised"

doc="<<= and >>="
a = -1
a <<= 10
assert a == -1024
a = -1
a >>= 10
assert a == -1
a = 3
a <<= 10
assert a == 3072
a = 3
a >>= 10
assert a == 0
a = -1
a <<= 100
assert a == -1267650600228229401496703205376
a = -1267650600228229401496703205376
a >>= 50
assert a == -1125899906842624
a = -1267650600228229401496703205376
a >>= 90
assert a == -1024
a = 1
a <<= 100
assert a == 1267650600228229401496703205376
a = 1267650600228229401496703205376
a >>= 50
assert a == 1125899906842624
a = 1267650600228229401496703205376
a >>= 90
assert a == 1024
try:
    a = 1
    a <<= 100000000000000000000000000000000000
except OverflowError:
    pass
else:
    assert False, "Overflow error not raised"

doc="**"
assert (2**10) == 1024
assert ((-2)**10) == 1024
approxEqual(2**(-10), 0.0009765625)
approxEqual((-2)**(-10), 0.0009765625)
assert (3**100) == 515377520732011331036461129765621272702107522001
approxEqual(515377520732011331036461129765621272702107522001**(-1), 1.9403252174826328e-48)
assert ((-1)**100000000000000000000) == 1
assert ((-1)**100000000000000000001) == -1

doc="**="
a = 2
a **= 10
assert a == 1024
a = -2
a **= 10
assert a == 1024
a = 2
a **= -10
approxEqual(a, 0.0009765625)
a = -2
a **= -10
approxEqual(a, 0.0009765625)

a = 3
a **= 100
assert a == 515377520732011331036461129765621272702107522001
a = 515377520732011331036461129765621272702107522001
a **= -1
approxEqual(a, 1.9403252174826328e-48)
a = -1
a **= 100000000000000000000
assert a == 1
a = -1
a **= 100000000000000000001
assert a == -1

doc="pow(x,y)"
assert pow(2,10) == 1024
assert pow(-2,10) == 1024
approxEqual(pow(2,-10), 0.0009765625)
approxEqual(pow(-2,-10), 0.0009765625)
assert pow(3,100) == 515377520732011331036461129765621272702107522001
approxEqual(pow(515377520732011331036461129765621272702107522001,-1), 1.9403252174826328e-48)
assert pow(-1,100000000000000000000) == 1
assert pow(-1,100000000000000000001) == -1

doc="pow(x,y,z)"
assert pow(1938019302983,283019283019238,91283091283012938) == 90917306668848727
pow(193801930298311111111111111111111,28301928301923822222222222222222222,9128309128301293822222222222222222222) == 2810220059867374937460899006752893533
assert pow(True, 10) == 1
try:
    pow(1,-1,1)
except TypeError:
    pass
else:
    assert False, "TypeError not raised"

doc="round"
assert round(12345678, 10) == 12345678
assert round(12345678,  0) == 12345678
assert round(12345678, -2) == 12345700
assert round(12345678, -4) == 12350000
assert round(12345678, -6) == 12000000
assert round(12345678, -8) == 0
assert round(maxInt, -17) == 9200000000000000000
assert round(maxInt, -18) == 9000000000000000000
assert round(maxInt, -19) == 10000000000000000000

assert round(-12345678, 10) == -12345678
assert round(-12345678,  0) == -12345678
assert round(-12345678, -2) == -12345700
assert round(-12345678, -4) == -12350000
assert round(-12345678, -6) == -12000000
assert round(-12345678, -8) == 0
assert round(minInt, -17) == -9200000000000000000
assert round(minInt, -18) == -9000000000000000000
assert round(minInt, -19) == -10000000000000000000

assert round(123456789012345678901, 10) == 123456789012345678901
assert round(123456789012345678901,  0) == 123456789012345678901
assert round(123456789012345678901, -2) == 123456789012345678900
assert round(123456789012345678901, -4) == 123456789012345680000
assert round(123456789012345678901, -6) == 123456789012346000000
assert round(123456789012345678901,-19) == 120000000000000000000
assert round(123456789012345678901,-21) == 0

assert round(-123456789012345678901, 10) == -123456789012345678901
assert round(-123456789012345678901,  0) == -123456789012345678901
assert round(-123456789012345678901, -2) == -123456789012345678900
assert round(-123456789012345678901, -4) == -123456789012345680000
assert round(-123456789012345678901, -6) == -123456789012346000000
assert round(-123456789012345678901,-19) == -120000000000000000000
assert round(-123456789012345678901,-21) == 0

doc="finished"

