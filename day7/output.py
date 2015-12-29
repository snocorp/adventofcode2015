
memo = {}

def ls():
    if 'ls' in memo:
        return memo['ls']
    val = lf() & lq()
    memo['ls'] = val
    return val


def jn():
    if 'jn' in memo:
        return memo['jn']
    val = iu() >> 1
    memo['jn'] = val
    return val


def bv():
    if 'bv' in memo:
        return memo['bv']
    val = bo() | bu()
    memo['bv'] = val
    return val


def hc():
    if 'hc' in memo:
        return memo['hc']
    val = gj() >> 1
    memo['hc'] = val
    return val


def eu():
    if 'eu' in memo:
        return memo['eu']
    val = et() >> 2
    memo['eu'] = val
    return val


def by():
    if 'by' in memo:
        return memo['by']
    val = bv() & bx()
    memo['by'] = val
    return val


def iu():
    if 'iu' in memo:
        return memo['iu']
    val = is1() | it()
    memo['iu'] = val
    return val


def o():
    if 'o' in memo:
        return memo['o']
    val = b() | n()
    memo['o'] = val
    return val


def gg():
    if 'gg' in memo:
        return memo['gg']
    val = gf() | ge()
    memo['gg'] = val
    return val


def ku():
    if 'ku' in memo:
        return memo['ku']
    val = ~ kt()
    memo['ku'] = val
    return val


def ed():
    if 'ed' in memo:
        return memo['ed']
    val = ea() & eb()
    memo['ed'] = val
    return val


def ks():
    if 'ks' in memo:
        return memo['ks']
    val = kl() | kr()
    memo['ks'] = val
    return val


def hl():
    if 'hl' in memo:
        return memo['hl']
    val = hi() & hk()
    memo['hl'] = val
    return val


def ax():
    if 'ax' in memo:
        return memo['ax']
    val = au() & av()
    memo['ax'] = val
    return val


def lg():
    if 'lg' in memo:
        return memo['lg']
    val = lf() >> 2
    memo['lg'] = val
    return val


def df():
    if 'df' in memo:
        return memo['df']
    val = dd() >> 3
    memo['df'] = val
    return val


def fc():
    if 'fc' in memo:
        return memo['fc']
    val = eu() & fa()
    memo['fc'] = val
    return val


def di():
    if 'di' in memo:
        return memo['di']
    val = df() & dg()
    memo['di'] = val
    return val


def it():
    if 'it' in memo:
        return memo['it']
    val = ip() << 15
    memo['it'] = val
    return val


def em():
    if 'em' in memo:
        return memo['em']
    val = ~ el()
    memo['em'] = val
    return val


def ff():
    if 'ff' in memo:
        return memo['ff']
    val = et() | fe()
    memo['ff'] = val
    return val


def fn():
    if 'fn' in memo:
        return memo['fn']
    val = fj() << 15
    memo['fn'] = val
    return val


def u():
    if 'u' in memo:
        return memo['u']
    val = t() | s()
    memo['u'] = val
    return val


def ma():
    if 'ma' in memo:
        return memo['ma']
    val = ly() | lz()
    memo['ma'] = val
    return val


def kr():
    if 'kr' in memo:
        return memo['kr']
    val = ko() & kq()
    memo['kr'] = val
    return val


def fy():
    if 'fy' in memo:
        return memo['fy']
    val = ~ fx()
    memo['fy'] = val
    return val


def fm():
    if 'fm' in memo:
        return memo['fm']
    val = et() >> 1
    memo['fm'] = val
    return val


def fb():
    if 'fb' in memo:
        return memo['fb']
    val = eu() | fa()
    memo['fb'] = val
    return val


def de():
    if 'de' in memo:
        return memo['de']
    val = dd() >> 2
    memo['de'] = val
    return val


def gp():
    if 'gp' in memo:
        return memo['gp']
    val = ~ go()
    memo['gp'] = val
    return val


def ke():
    if 'ke' in memo:
        return memo['ke']
    val = kb() & kd()
    memo['ke'] = val
    return val


def hi():
    if 'hi' in memo:
        return memo['hi']
    val = hg() | hh()
    memo['hi'] = val
    return val


def kg():
    if 'kg' in memo:
        return memo['kg']
    val = jm() << 1
    memo['kg'] = val
    return val


def co():
    if 'co' in memo:
        return memo['co']
    val = ~ cn()
    memo['co'] = val
    return val


def jq():
    if 'jq' in memo:
        return memo['jq']
    val = jp() >> 2
    memo['jq'] = val
    return val


def js():
    if 'js' in memo:
        return memo['js']
    val = jp() >> 5
    memo['js'] = val
    return val


def ip():
    if 'ip' in memo:
        return memo['ip']
    val = 1 & io()
    memo['ip'] = val
    return val


def es():
    if 'es' in memo:
        return memo['es']
    val = eo() << 15
    memo['es'] = val
    return val


def jk():
    if 'jk' in memo:
        return memo['jk']
    val = 1 & jj()
    memo['jk'] = val
    return val


def j():
    if 'j' in memo:
        return memo['j']
    val = g() & i()
    memo['j'] = val
    return val


def ck():
    if 'ck' in memo:
        return memo['ck']
    val = ci() >> 3
    memo['ck'] = val
    return val


def gq():
    if 'gq' in memo:
        return memo['gq']
    val = gn() & gp()
    memo['gq'] = val
    return val


def fv():
    if 'fv' in memo:
        return memo['fv']
    val = fs() & fu()
    memo['fv'] = val
    return val


def lm():
    if 'lm' in memo:
        return memo['lm']
    val = lj() & ll()
    memo['lm'] = val
    return val


def jo():
    if 'jo' in memo:
        return memo['jo']
    val = jk() << 15
    memo['jo'] = val
    return val


def iw():
    if 'iw' in memo:
        return memo['iw']
    val = iu() >> 3
    memo['iw'] = val
    return val


def ij():
    if 'ij' in memo:
        return memo['ij']
    val = ~ ii()
    memo['ij'] = val
    return val


def cd():
    if 'cd' in memo:
        return memo['cd']
    val = 1 & cc()
    memo['cd'] = val
    return val


def bp():
    if 'bp' in memo:
        return memo['bp']
    val = bn() >> 3
    memo['bp'] = val
    return val


def gx():
    if 'gx' in memo:
        return memo['gx']
    val = ~ gw()
    memo['gx'] = val
    return val


def fu():
    if 'fu' in memo:
        return memo['fu']
    val = ~ ft()
    memo['fu'] = val
    return val


def jp():
    if 'jp' in memo:
        return memo['jp']
    val = jn() | jo()
    memo['jp'] = val
    return val


def jc():
    if 'jc' in memo:
        return memo['jc']
    val = iv() | jb()
    memo['jc'] = val
    return val


def hw():
    if 'hw' in memo:
        return memo['hw']
    val = hv() | hu()
    memo['hw'] = val
    return val


def b():
    if 'b' in memo:
        return memo['b']
    val = 16076
    memo['b'] = val
    return val

def gm():
    if 'gm' in memo:
        return memo['gm']
    val = gj() >> 5
    memo['gm'] = val
    return val


def ht():
    if 'ht' in memo:
        return memo['ht']
    val = hq() & hs()
    memo['ht'] = val
    return val


def er():
    if 'er' in memo:
        return memo['er']
    val = dy() >> 1
    memo['er'] = val
    return val


def ap():
    if 'ap' in memo:
        return memo['ap']
    val = ao() | an()
    memo['ap'] = val
    return val


def lf():
    if 'lf' in memo:
        return memo['lf']
    val = ld() | le()
    memo['lf'] = val
    return val


def ce():
    if 'ce' in memo:
        return memo['ce']
    val = bk() << 1
    memo['ce'] = val
    return val


def cc():
    if 'cc' in memo:
        return memo['cc']
    val = bz() & cb()
    memo['cc'] = val
    return val


def bm():
    if 'bm' in memo:
        return memo['bm']
    val = bi() << 15
    memo['bm'] = val
    return val


def io():
    if 'io' in memo:
        return memo['io']
    val = il() & in1()
    memo['io'] = val
    return val


def ai():
    if 'ai' in memo:
        return memo['ai']
    val = af() & ah()
    memo['ai'] = val
    return val


def bl():
    if 'bl' in memo:
        return memo['bl']
    val = as1() >> 1
    memo['bl'] = val
    return val


def lh():
    if 'lh' in memo:
        return memo['lh']
    val = lf() >> 3
    memo['lh'] = val
    return val


def et():
    if 'et' in memo:
        return memo['et']
    val = er() | es()
    memo['et'] = val
    return val


def ay():
    if 'ay' in memo:
        return memo['ay']
    val = ~ ax()
    memo['ay'] = val
    return val


def db():
    if 'db' in memo:
        return memo['db']
    val = ci() >> 1
    memo['db'] = val
    return val


def fg():
    if 'fg' in memo:
        return memo['fg']
    val = et() & fe()
    memo['fg'] = val
    return val


def ln():
    if 'ln' in memo:
        return memo['ln']
    val = lg() | lm()
    memo['ln'] = val
    return val


def n():
    if 'n' in memo:
        return memo['n']
    val = k() & m()
    memo['n'] = val
    return val


def ia():
    if 'ia' in memo:
        return memo['ia']
    val = hz() >> 2
    memo['ia'] = val
    return val


def lb():
    if 'lb' in memo:
        return memo['lb']
    val = kh() << 1
    memo['lb'] = val
    return val


def ez():
    if 'ez' in memo:
        return memo['ez']
    val = ~ ey()
    memo['ez'] = val
    return val


def dj():
    if 'dj' in memo:
        return memo['dj']
    val = ~ di()
    memo['dj'] = val
    return val


def eg():
    if 'eg' in memo:
        return memo['eg']
    val = dz() | ef()
    memo['eg'] = val
    return val


def a():
    if 'a' in memo:
        return memo['a']
    val = lx()
    memo['a'] = val
    return val

def ja():
    if 'ja' in memo:
        return memo['ja']
    val = ~ iz()
    memo['ja'] = val
    return val


def hd():
    if 'hd' in memo:
        return memo['hd']
    val = gz() << 15
    memo['hd'] = val
    return val


def cf():
    if 'cf' in memo:
        return memo['cf']
    val = ce() | cd()
    memo['cf'] = val
    return val


def ft():
    if 'ft' in memo:
        return memo['ft']
    val = fq() & fr()
    memo['ft'] = val
    return val


def bb():
    if 'bb' in memo:
        return memo['bb']
    val = at() & az()
    memo['bb'] = val
    return val


def hb():
    if 'hb' in memo:
        return memo['hb']
    val = ha() | gz()
    memo['hb'] = val
    return val


def fx():
    if 'fx' in memo:
        return memo['fx']
    val = fp() & fv()
    memo['fx'] = val
    return val


def gc():
    if 'gc' in memo:
        return memo['gc']
    val = ~ gb()
    memo['gc'] = val
    return val


def ii():
    if 'ii' in memo:
        return memo['ii']
    val = ia() & ig()
    memo['ii'] = val
    return val


def gn():
    if 'gn' in memo:
        return memo['gn']
    val = gl() | gm()
    memo['gn'] = val
    return val


def c():
    if 'c' in memo:
        return memo['c']
    val = 0
    memo['c'] = val
    return val

def cb():
    if 'cb' in memo:
        return memo['cb']
    val = ~ ca()
    memo['cb'] = val
    return val


def cg():
    if 'cg' in memo:
        return memo['cg']
    val = bn() >> 1
    memo['cg'] = val
    return val


def t():
    if 't' in memo:
        return memo['t']
    val = c() << 1
    memo['t'] = val
    return val


def iy():
    if 'iy' in memo:
        return memo['iy']
    val = iw() | ix()
    memo['iy'] = val
    return val


def kh():
    if 'kh' in memo:
        return memo['kh']
    val = kg() | kf()
    memo['kh'] = val
    return val


def ek():
    if 'ek' in memo:
        return memo['ek']
    val = dy() | ej()
    memo['ek'] = val
    return val


def kp():
    if 'kp' in memo:
        return memo['kp']
    val = km() & kn()
    memo['kp'] = val
    return val


def fd():
    if 'fd' in memo:
        return memo['fd']
    val = ~ fc()
    memo['fd'] = val
    return val


def ib():
    if 'ib' in memo:
        return memo['ib']
    val = hz() >> 3
    memo['ib'] = val
    return val


def dr():
    if 'dr' in memo:
        return memo['dr']
    val = ~ dq()
    memo['dr'] = val
    return val


def fh():
    if 'fh' in memo:
        return memo['fh']
    val = ~ fg()
    memo['fh'] = val
    return val


def dz():
    if 'dz' in memo:
        return memo['dz']
    val = dy() >> 2
    memo['dz'] = val
    return val


def kl():
    if 'kl' in memo:
        return memo['kl']
    val = kk() >> 2
    memo['kl'] = val
    return val


def fj():
    if 'fj' in memo:
        return memo['fj']
    val = 1 & fi()
    memo['fj'] = val
    return val


def hs():
    if 'hs' in memo:
        return memo['hs']
    val = ~ hr()
    memo['hs'] = val
    return val


def ki():
    if 'ki' in memo:
        return memo['ki']
    val = jp() >> 1
    memo['ki'] = val
    return val


def bn():
    if 'bn' in memo:
        return memo['bn']
    val = bl() | bm()
    memo['bn'] = val
    return val


def gz():
    if 'gz' in memo:
        return memo['gz']
    val = 1 & gy()
    memo['gz'] = val
    return val


def gu():
    if 'gu' in memo:
        return memo['gu']
    val = gr() & gt()
    memo['gu'] = val
    return val


def dd():
    if 'dd' in memo:
        return memo['dd']
    val = db() | dc()
    memo['dd'] = val
    return val


def dl():
    if 'dl' in memo:
        return memo['dl']
    val = de() | dk()
    memo['dl'] = val
    return val


def av():
    if 'av' in memo:
        return memo['av']
    val = as1() >> 5
    memo['av'] = val
    return val


def li():
    if 'li' in memo:
        return memo['li']
    val = lf() >> 5
    memo['li'] = val
    return val


def hp():
    if 'hp' in memo:
        return memo['hp']
    val = hm() & ho()
    memo['hp'] = val
    return val


def ci():
    if 'ci' in memo:
        return memo['ci']
    val = cg() | ch()
    memo['ci'] = val
    return val


def gw():
    if 'gw' in memo:
        return memo['gw']
    val = gj() & gu()
    memo['gw'] = val
    return val


def gi():
    if 'gi' in memo:
        return memo['gi']
    val = ge() << 15
    memo['gi'] = val
    return val


def g():
    if 'g' in memo:
        return memo['g']
    val = e() | f()
    memo['g'] = val
    return val


def fw():
    if 'fw' in memo:
        return memo['fw']
    val = fp() | fv()
    memo['fw'] = val
    return val


def fe():
    if 'fe' in memo:
        return memo['fe']
    val = fb() & fd()
    memo['fe'] = val
    return val


def ch():
    if 'ch' in memo:
        return memo['ch']
    val = cd() << 15
    memo['ch'] = val
    return val


def v():
    if 'v' in memo:
        return memo['v']
    val = b() >> 1
    memo['v'] = val
    return val


def ba():
    if 'ba' in memo:
        return memo['ba']
    val = at() | az()
    memo['ba'] = val
    return val


def bo():
    if 'bo' in memo:
        return memo['bo']
    val = bn() >> 2
    memo['bo'] = val
    return val


def lk():
    if 'lk' in memo:
        return memo['lk']
    val = lh() & li()
    memo['lk'] = val
    return val


def do():
    if 'do' in memo:
        return memo['do']
    val = dl() & dn()
    memo['do'] = val
    return val


def ej():
    if 'ej' in memo:
        return memo['ej']
    val = eg() & ei()
    memo['ej'] = val
    return val


def fa():
    if 'fa' in memo:
        return memo['fa']
    val = ex() & ez()
    memo['fa'] = val
    return val


def kq():
    if 'kq' in memo:
        return memo['kq']
    val = ~ kp()
    memo['kq'] = val
    return val


def ll():
    if 'll' in memo:
        return memo['ll']
    val = ~ lk()
    memo['ll'] = val
    return val


def ak():
    if 'ak' in memo:
        return memo['ak']
    val = x() & ai()
    memo['ak'] = val
    return val


def kb():
    if 'kb' in memo:
        return memo['kb']
    val = jp() | ka()
    memo['kb'] = val
    return val


def je():
    if 'je' in memo:
        return memo['je']
    val = ~ jd()
    memo['je'] = val
    return val


def jb():
    if 'jb' in memo:
        return memo['jb']
    val = iy() & ja()
    memo['jb'] = val
    return val


def jr():
    if 'jr' in memo:
        return memo['jr']
    val = jp() >> 3
    memo['jr'] = val
    return val


def ga():
    if 'ga' in memo:
        return memo['ga']
    val = fo() | fz()
    memo['ga'] = val
    return val


def dh():
    if 'dh' in memo:
        return memo['dh']
    val = df() | dg()
    memo['dh'] = val
    return val


def gk():
    if 'gk' in memo:
        return memo['gk']
    val = gj() >> 2
    memo['gk'] = val
    return val


def gv():
    if 'gv' in memo:
        return memo['gv']
    val = gj() | gu()
    memo['gv'] = val
    return val


def ji():
    if 'ji' in memo:
        return memo['ji']
    val = ~ jh()
    memo['ji'] = val
    return val


def bj():
    if 'bj' in memo:
        return memo['bj']
    val = ap() << 1
    memo['bj'] = val
    return val


def lt():
    if 'lt' in memo:
        return memo['lt']
    val = ~ ls()
    memo['lt'] = val
    return val


def jl():
    if 'jl' in memo:
        return memo['jl']
    val = ir() << 1
    memo['jl'] = val
    return val


def ca():
    if 'ca' in memo:
        return memo['ca']
    val = bn() & by()
    memo['ca'] = val
    return val


def lz():
    if 'lz' in memo:
        return memo['lz']
    val = lv() << 15
    memo['lz'] = val
    return val


def bd():
    if 'bd' in memo:
        return memo['bd']
    val = ba() & bc()
    memo['bd'] = val
    return val


def dc():
    if 'dc' in memo:
        return memo['dc']
    val = cy() << 15
    memo['dc'] = val
    return val


def lq():
    if 'lq' in memo:
        return memo['lq']
    val = ln() & lp()
    memo['lq'] = val
    return val


def aq():
    if 'aq' in memo:
        return memo['aq']
    val = x() >> 1
    memo['aq'] = val
    return val


def gr():
    if 'gr' in memo:
        return memo['gr']
    val = gk() | gq()
    memo['gr'] = val
    return val


def ky():
    if 'ky' in memo:
        return memo['ky']
    val = ~ kx()
    memo['ky'] = val
    return val


def jj():
    if 'jj' in memo:
        return memo['jj']
    val = jg() & ji()
    memo['jj'] = val
    return val


def bz():
    if 'bz' in memo:
        return memo['bz']
    val = bn() | by()
    memo['bz'] = val
    return val


def gf():
    if 'gf' in memo:
        return memo['gf']
    val = fl() << 1
    memo['gf'] = val
    return val


def br():
    if 'br' in memo:
        return memo['br']
    val = bp() | bq()
    memo['br'] = val
    return val


def hq():
    if 'hq' in memo:
        return memo['hq']
    val = he() | hp()
    memo['hq'] = val
    return val


def ew():
    if 'ew' in memo:
        return memo['ew']
    val = et() >> 5
    memo['ew'] = val
    return val


def iv():
    if 'iv' in memo:
        return memo['iv']
    val = iu() >> 2
    memo['iv'] = val
    return val


def go():
    if 'go' in memo:
        return memo['go']
    val = gl() & gm()
    memo['go'] = val
    return val


def aj():
    if 'aj' in memo:
        return memo['aj']
    val = x() | ai()
    memo['aj'] = val
    return val


def he():
    if 'he' in memo:
        return memo['he']
    val = hc() | hd()
    memo['he'] = val
    return val


def lo():
    if 'lo' in memo:
        return memo['lo']
    val = lg() & lm()
    memo['lo'] = val
    return val


def lj():
    if 'lj' in memo:
        return memo['lj']
    val = lh() | li()
    memo['lj'] = val
    return val


def du():
    if 'du' in memo:
        return memo['du']
    val = da() << 1
    memo['du'] = val
    return val


def fp():
    if 'fp' in memo:
        return memo['fp']
    val = fo() >> 2
    memo['fp'] = val
    return val


def gs():
    if 'gs' in memo:
        return memo['gs']
    val = gk() & gq()
    memo['gs'] = val
    return val


def bk():
    if 'bk' in memo:
        return memo['bk']
    val = bj() | bi()
    memo['bk'] = val
    return val


def lr():
    if 'lr' in memo:
        return memo['lr']
    val = lf() | lq()
    memo['lr'] = val
    return val


def cr():
    if 'cr' in memo:
        return memo['cr']
    val = cj() & cp()
    memo['cr'] = val
    return val


def hy():
    if 'hy' in memo:
        return memo['hy']
    val = hu() << 15
    memo['hy'] = val
    return val


def bi():
    if 'bi' in memo:
        return memo['bi']
    val = 1 & bh()
    memo['bi'] = val
    return val


def fq():
    if 'fq' in memo:
        return memo['fq']
    val = fo() >> 3
    memo['fq'] = val
    return val


def lp():
    if 'lp' in memo:
        return memo['lp']
    val = ~ lo()
    memo['lp'] = val
    return val


def iq():
    if 'iq' in memo:
        return memo['iq']
    val = hw() << 1
    memo['iq'] = val
    return val


def dw():
    if 'dw' in memo:
        return memo['dw']
    val = dd() >> 1
    memo['dw'] = val
    return val


def dx():
    if 'dx' in memo:
        return memo['dx']
    val = dt() << 15
    memo['dx'] = val
    return val


def el():
    if 'el' in memo:
        return memo['el']
    val = dy() & ej()
    memo['el'] = val
    return val


def ar():
    if 'ar' in memo:
        return memo['ar']
    val = an() << 15
    memo['ar'] = val
    return val


def as1():
    if 'as1' in memo:
        return memo['as1']
    val = aq() | ar()
    memo['as1'] = val
    return val


def s():
    if 's' in memo:
        return memo['s']
    val = 1 & r()
    memo['s'] = val
    return val


def fz():
    if 'fz' in memo:
        return memo['fz']
    val = fw() & fy()
    memo['fz'] = val
    return val


def in1():
    if 'in1' in memo:
        return memo['in1']
    val = ~ im()
    memo['in1'] = val
    return val


def ev():
    if 'ev' in memo:
        return memo['ev']
    val = et() >> 3
    memo['ev'] = val
    return val


def dt():
    if 'dt' in memo:
        return memo['dt']
    val = 1 & ds()
    memo['dt'] = val
    return val


def ef():
    if 'ef' in memo:
        return memo['ef']
    val = ec() & ee()
    memo['ef'] = val
    return val


def al():
    if 'al' in memo:
        return memo['al']
    val = ~ ak()
    memo['al'] = val
    return val


def jm():
    if 'jm' in memo:
        return memo['jm']
    val = jl() | jk()
    memo['jm'] = val
    return val


def eo():
    if 'eo' in memo:
        return memo['eo']
    val = 1 & en()
    memo['eo'] = val
    return val


def lc():
    if 'lc' in memo:
        return memo['lc']
    val = lb() | la()
    memo['lc'] = val
    return val


def jh():
    if 'jh' in memo:
        return memo['jh']
    val = iu() & jf()
    memo['jh'] = val
    return val


def ix():
    if 'ix' in memo:
        return memo['ix']
    val = iu() >> 5
    memo['ix'] = val
    return val


def bw():
    if 'bw' in memo:
        return memo['bw']
    val = bo() & bu()
    memo['bw'] = val
    return val


def da():
    if 'da' in memo:
        return memo['da']
    val = cz() | cy()
    memo['da'] = val
    return val


def jd():
    if 'jd' in memo:
        return memo['jd']
    val = iv() & jb()
    memo['jd'] = val
    return val


def iz():
    if 'iz' in memo:
        return memo['iz']
    val = iw() & ix()
    memo['iz'] = val
    return val


def ly():
    if 'ly' in memo:
        return memo['ly']
    val = lf() >> 1
    memo['ly'] = val
    return val


def jg():
    if 'jg' in memo:
        return memo['jg']
    val = iu() | jf()
    memo['jg'] = val
    return val


def dn():
    if 'dn' in memo:
        return memo['dn']
    val = ~ dm()
    memo['dn'] = val
    return val


def lx():
    if 'lx' in memo:
        return memo['lx']
    val = lw() | lv()
    memo['lx'] = val
    return val


def ha():
    if 'ha' in memo:
        return memo['ha']
    val = gg() << 1
    memo['ha'] = val
    return val


def lu():
    if 'lu' in memo:
        return memo['lu']
    val = lr() & lt()
    memo['lu'] = val
    return val


def fo():
    if 'fo' in memo:
        return memo['fo']
    val = fm() | fn()
    memo['fo'] = val
    return val


def hg():
    if 'hg' in memo:
        return memo['hg']
    val = he() >> 3
    memo['hg'] = val
    return val


def am():
    if 'am' in memo:
        return memo['am']
    val = aj() & al()
    memo['am'] = val
    return val


def la():
    if 'la' in memo:
        return memo['la']
    val = 1 & kz()
    memo['la'] = val
    return val


def eb():
    if 'eb' in memo:
        return memo['eb']
    val = dy() >> 5
    memo['eb'] = val
    return val


def jf():
    if 'jf' in memo:
        return memo['jf']
    val = jc() & je()
    memo['jf'] = val
    return val


def cp():
    if 'cp' in memo:
        return memo['cp']
    val = cm() & co()
    memo['cp'] = val
    return val


def gy():
    if 'gy' in memo:
        return memo['gy']
    val = gv() & gx()
    memo['gy'] = val
    return val


def ex():
    if 'ex' in memo:
        return memo['ex']
    val = ev() | ew()
    memo['ex'] = val
    return val


def kc():
    if 'kc' in memo:
        return memo['kc']
    val = jp() & ka()
    memo['kc'] = val
    return val


def fl():
    if 'fl' in memo:
        return memo['fl']
    val = fk() | fj()
    memo['fl'] = val
    return val


def ea():
    if 'ea' in memo:
        return memo['ea']
    val = dy() >> 3
    memo['ea'] = val
    return val


def bt():
    if 'bt' in memo:
        return memo['bt']
    val = ~ bs()
    memo['bt'] = val
    return val


def ah():
    if 'ah' in memo:
        return memo['ah']
    val = ~ ag()
    memo['ah'] = val
    return val


def eh():
    if 'eh' in memo:
        return memo['eh']
    val = dz() & ef()
    memo['eh'] = val
    return val


def cz():
    if 'cz' in memo:
        return memo['cz']
    val = cf() << 1
    memo['cz'] = val
    return val


def cw():
    if 'cw' in memo:
        return memo['cw']
    val = ~ cv()
    memo['cw'] = val
    return val


def cy():
    if 'cy' in memo:
        return memo['cy']
    val = 1 & cx()
    memo['cy'] = val
    return val


def dm():
    if 'dm' in memo:
        return memo['dm']
    val = de() & dk()
    memo['dm'] = val
    return val


def cn():
    if 'cn' in memo:
        return memo['cn']
    val = ck() & cl()
    memo['cn'] = val
    return val


def aa():
    if 'aa' in memo:
        return memo['aa']
    val = x() >> 5
    memo['aa'] = val
    return val


def ep():
    if 'ep' in memo:
        return memo['ep']
    val = dv() << 1
    memo['ep'] = val
    return val


def hf():
    if 'hf' in memo:
        return memo['hf']
    val = he() >> 2
    memo['hf'] = val
    return val


def bx():
    if 'bx' in memo:
        return memo['bx']
    val = ~ bw()
    memo['bx'] = val
    return val


def cm():
    if 'cm' in memo:
        return memo['cm']
    val = ck() | cl()
    memo['cm'] = val
    return val


def bs():
    if 'bs' in memo:
        return memo['bs']
    val = bp() & bq()
    memo['bs'] = val
    return val


def be():
    if 'be' in memo:
        return memo['be']
    val = as1() | bd()
    memo['be'] = val
    return val


def hr():
    if 'hr' in memo:
        return memo['hr']
    val = he() & hp()
    memo['hr'] = val
    return val


def ey():
    if 'ey' in memo:
        return memo['ey']
    val = ev() & ew()
    memo['ey'] = val
    return val


def lv():
    if 'lv' in memo:
        return memo['lv']
    val = 1 & lu()
    memo['lv'] = val
    return val


def km():
    if 'km' in memo:
        return memo['km']
    val = kk() >> 3
    memo['km'] = val
    return val


def p():
    if 'p' in memo:
        return memo['p']
    val = b() & n()
    memo['p'] = val
    return val


def kd():
    if 'kd' in memo:
        return memo['kd']
    val = ~ kc()
    memo['kd'] = val
    return val


def lw():
    if 'lw' in memo:
        return memo['lw']
    val = lc() << 1
    memo['lw'] = val
    return val


def ko():
    if 'ko' in memo:
        return memo['ko']
    val = km() | kn()
    memo['ko'] = val
    return val


def ig():
    if 'ig' in memo:
        return memo['ig']
    val = id() & if1()
    memo['ig'] = val
    return val


def ik():
    if 'ik' in memo:
        return memo['ik']
    val = ih() & ij()
    memo['ik'] = val
    return val


def ju():
    if 'ju' in memo:
        return memo['ju']
    val = jr() & js()
    memo['ju'] = val
    return val


def cl():
    if 'cl' in memo:
        return memo['cl']
    val = ci() >> 5
    memo['cl'] = val
    return val


def is1():
    if 'is1' in memo:
        return memo['is1']
    val = hz() >> 1
    memo['is1'] = val
    return val


def kf():
    if 'kf' in memo:
        return memo['kf']
    val = 1 & ke()
    memo['kf'] = val
    return val


def gt():
    if 'gt' in memo:
        return memo['gt']
    val = ~ gs()
    memo['gt'] = val
    return val


def az():
    if 'az' in memo:
        return memo['az']
    val = aw() & ay()
    memo['az'] = val
    return val


def y():
    if 'y' in memo:
        return memo['y']
    val = x() >> 2
    memo['y'] = val
    return val


def ae():
    if 'ae' in memo:
        return memo['ae']
    val = ab() & ad()
    memo['ae'] = val
    return val


def fi():
    if 'fi' in memo:
        return memo['fi']
    val = ff() & fh()
    memo['fi'] = val
    return val


def cv():
    if 'cv' in memo:
        return memo['cv']
    val = ci() & ct()
    memo['cv'] = val
    return val


def fk():
    if 'fk' in memo:
        return memo['fk']
    val = eq() << 1
    memo['fk'] = val
    return val


def gl():
    if 'gl' in memo:
        return memo['gl']
    val = gj() >> 3
    memo['gl'] = val
    return val


def ao():
    if 'ao' in memo:
        return memo['ao']
    val = u() << 1
    memo['ao'] = val
    return val


def bc():
    if 'bc' in memo:
        return memo['bc']
    val = ~ bb()
    memo['bc'] = val
    return val


def hk():
    if 'hk' in memo:
        return memo['hk']
    val = ~ hj()
    memo['hk'] = val
    return val


def kz():
    if 'kz' in memo:
        return memo['kz']
    val = kw() & ky()
    memo['kz'] = val
    return val


def bf():
    if 'bf' in memo:
        return memo['bf']
    val = as1() & bd()
    memo['bf'] = val
    return val


def dy():
    if 'dy' in memo:
        return memo['dy']
    val = dw() | dx()
    memo['dy'] = val
    return val


def bu():
    if 'bu' in memo:
        return memo['bu']
    val = br() & bt()
    memo['bu'] = val
    return val


def kx():
    if 'kx' in memo:
        return memo['kx']
    val = kk() & kv()
    memo['kx'] = val
    return val


def eq():
    if 'eq' in memo:
        return memo['eq']
    val = ep() | eo()
    memo['eq'] = val
    return val


def hx():
    if 'hx' in memo:
        return memo['hx']
    val = he() >> 1
    memo['hx'] = val
    return val


def kk():
    if 'kk' in memo:
        return memo['kk']
    val = ki() | kj()
    memo['kk'] = val
    return val


def jv():
    if 'jv' in memo:
        return memo['jv']
    val = ~ ju()
    memo['jv'] = val
    return val


def en():
    if 'en' in memo:
        return memo['en']
    val = ek() & em()
    memo['en'] = val
    return val


def kn():
    if 'kn' in memo:
        return memo['kn']
    val = kk() >> 5
    memo['kn'] = val
    return val


def ei():
    if 'ei' in memo:
        return memo['ei']
    val = ~ eh()
    memo['ei'] = val
    return val


def hz():
    if 'hz' in memo:
        return memo['hz']
    val = hx() | hy()
    memo['hz'] = val
    return val


def ec():
    if 'ec' in memo:
        return memo['ec']
    val = ea() | eb()
    memo['ec'] = val
    return val


def w():
    if 'w' in memo:
        return memo['w']
    val = s() << 15
    memo['w'] = val
    return val


def gh():
    if 'gh' in memo:
        return memo['gh']
    val = fo() >> 1
    memo['gh'] = val
    return val


def kw():
    if 'kw' in memo:
        return memo['kw']
    val = kk() | kv()
    memo['kw'] = val
    return val


def bq():
    if 'bq' in memo:
        return memo['bq']
    val = bn() >> 5
    memo['bq'] = val
    return val


def ee():
    if 'ee' in memo:
        return memo['ee']
    val = ~ ed()
    memo['ee'] = val
    return val


def hu():
    if 'hu' in memo:
        return memo['hu']
    val = 1 & ht()
    memo['hu'] = val
    return val


def cx():
    if 'cx' in memo:
        return memo['cx']
    val = cu() & cw()
    memo['cx'] = val
    return val


def f():
    if 'f' in memo:
        return memo['f']
    val = b() >> 5
    memo['f'] = val
    return val


def kt():
    if 'kt' in memo:
        return memo['kt']
    val = kl() & kr()
    memo['kt'] = val
    return val


def ir():
    if 'ir' in memo:
        return memo['ir']
    val = iq() | ip()
    memo['ir'] = val
    return val


def cj():
    if 'cj' in memo:
        return memo['cj']
    val = ci() >> 2
    memo['cj'] = val
    return val


def cq():
    if 'cq' in memo:
        return memo['cq']
    val = cj() | cp()
    memo['cq'] = val
    return val


def r():
    if 'r' in memo:
        return memo['r']
    val = o() & q()
    memo['r'] = val
    return val


def dg():
    if 'dg' in memo:
        return memo['dg']
    val = dd() >> 5
    memo['dg'] = val
    return val


def d():
    if 'd' in memo:
        return memo['d']
    val = b() >> 2
    memo['d'] = val
    return val


def kv():
    if 'kv' in memo:
        return memo['kv']
    val = ks() & ku()
    memo['kv'] = val
    return val


def e():
    if 'e' in memo:
        return memo['e']
    val = b() >> 3
    memo['e'] = val
    return val


def k():
    if 'k' in memo:
        return memo['k']
    val = d() | j()
    memo['k'] = val
    return val


def q():
    if 'q' in memo:
        return memo['q']
    val = ~ p()
    memo['q'] = val
    return val


def cs():
    if 'cs' in memo:
        return memo['cs']
    val = ~ cr()
    memo['cs'] = val
    return val


def dv():
    if 'dv' in memo:
        return memo['dv']
    val = du() | dt()
    memo['dv'] = val
    return val


def kj():
    if 'kj' in memo:
        return memo['kj']
    val = kf() << 15
    memo['kj'] = val
    return val


def ad():
    if 'ad' in memo:
        return memo['ad']
    val = ~ ac()
    memo['ad'] = val
    return val


def fr():
    if 'fr' in memo:
        return memo['fr']
    val = fo() >> 5
    memo['fr'] = val
    return val


def il():
    if 'il' in memo:
        return memo['il']
    val = hz() | ik()
    memo['il'] = val
    return val


def ka():
    if 'ka' in memo:
        return memo['ka']
    val = jx() & jz()
    memo['ka'] = val
    return val


def gj():
    if 'gj' in memo:
        return memo['gj']
    val = gh() | gi()
    memo['gj'] = val
    return val


def ld():
    if 'ld' in memo:
        return memo['ld']
    val = kk() >> 1
    memo['ld'] = val
    return val


def ic():
    if 'ic' in memo:
        return memo['ic']
    val = hz() >> 5
    memo['ic'] = val
    return val


def at():
    if 'at' in memo:
        return memo['at']
    val = as1() >> 2
    memo['at'] = val
    return val


def jz():
    if 'jz' in memo:
        return memo['jz']
    val = ~ jy()
    memo['jz'] = val
    return val


def an():
    if 'an' in memo:
        return memo['an']
    val = 1 & am()
    memo['an'] = val
    return val


def cu():
    if 'cu' in memo:
        return memo['cu']
    val = ci() | ct()
    memo['cu'] = val
    return val


def hj():
    if 'hj' in memo:
        return memo['hj']
    val = hg() & hh()
    memo['hj'] = val
    return val


def jx():
    if 'jx' in memo:
        return memo['jx']
    val = jq() | jw()
    memo['jx'] = val
    return val


def x():
    if 'x' in memo:
        return memo['x']
    val = v() | w()
    memo['x'] = val
    return val


def le():
    if 'le' in memo:
        return memo['le']
    val = la() << 15
    memo['le'] = val
    return val


def dk():
    if 'dk' in memo:
        return memo['dk']
    val = dh() & dj()
    memo['dk'] = val
    return val


def ds():
    if 'ds' in memo:
        return memo['ds']
    val = dp() & dr()
    memo['ds'] = val
    return val


def jy():
    if 'jy' in memo:
        return memo['jy']
    val = jq() & jw()
    memo['jy'] = val
    return val


def aw():
    if 'aw' in memo:
        return memo['aw']
    val = au() | av()
    memo['aw'] = val
    return val


def bg():
    if 'bg' in memo:
        return memo['bg']
    val = ~ bf()
    memo['bg'] = val
    return val


def ab():
    if 'ab' in memo:
        return memo['ab']
    val = z() | aa()
    memo['ab'] = val
    return val


def gd():
    if 'gd' in memo:
        return memo['gd']
    val = ga() & gc()
    memo['gd'] = val
    return val


def im():
    if 'im' in memo:
        return memo['im']
    val = hz() & ik()
    memo['im'] = val
    return val


def jw():
    if 'jw' in memo:
        return memo['jw']
    val = jt() & jv()
    memo['jw'] = val
    return val


def ac():
    if 'ac' in memo:
        return memo['ac']
    val = z() & aa()
    memo['ac'] = val
    return val


def jt():
    if 'jt' in memo:
        return memo['jt']
    val = jr() | js()
    memo['jt'] = val
    return val


def hv():
    if 'hv' in memo:
        return memo['hv']
    val = hb() << 1
    memo['hv'] = val
    return val


def hm():
    if 'hm' in memo:
        return memo['hm']
    val = hf() | hl()
    memo['hm'] = val
    return val


def id():
    if 'id' in memo:
        return memo['id']
    val = ib() | ic()
    memo['id'] = val
    return val


def fs():
    if 'fs' in memo:
        return memo['fs']
    val = fq() | fr()
    memo['fs'] = val
    return val


def ct():
    if 'ct' in memo:
        return memo['ct']
    val = cq() & cs()
    memo['ct'] = val
    return val


def ih():
    if 'ih' in memo:
        return memo['ih']
    val = ia() | ig()
    memo['ih'] = val
    return val


def dp():
    if 'dp' in memo:
        return memo['dp']
    val = dd() | do()
    memo['dp'] = val
    return val


def l():
    if 'l' in memo:
        return memo['l']
    val = d() & j()
    memo['l'] = val
    return val


def ie():
    if 'ie' in memo:
        return memo['ie']
    val = ib() & ic()
    memo['ie'] = val
    return val


def au():
    if 'au' in memo:
        return memo['au']
    val = as1() >> 3
    memo['au'] = val
    return val


def bh():
    if 'bh' in memo:
        return memo['bh']
    val = be() & bg()
    memo['bh'] = val
    return val


def dq():
    if 'dq' in memo:
        return memo['dq']
    val = dd() & do()
    memo['dq'] = val
    return val


def m():
    if 'm' in memo:
        return memo['m']
    val = ~ l()
    memo['m'] = val
    return val


def ge():
    if 'ge' in memo:
        return memo['ge']
    val = 1 & gd()
    memo['ge'] = val
    return val


def ag():
    if 'ag' in memo:
        return memo['ag']
    val = y() & ae()
    memo['ag'] = val
    return val


def gb():
    if 'gb' in memo:
        return memo['gb']
    val = fo() & fz()
    memo['gb'] = val
    return val


def if1():
    if 'if1' in memo:
        return memo['if1']
    val = ~ ie()
    memo['if1'] = val
    return val


def h():
    if 'h' in memo:
        return memo['h']
    val = e() & f()
    memo['h'] = val
    return val


def z():
    if 'z' in memo:
        return memo['z']
    val = x() >> 3
    memo['z'] = val
    return val


def af():
    if 'af' in memo:
        return memo['af']
    val = y() | ae()
    memo['af'] = val
    return val


def hn():
    if 'hn' in memo:
        return memo['hn']
    val = hf() & hl()
    memo['hn'] = val
    return val


def i():
    if 'i' in memo:
        return memo['i']
    val = ~ h()
    memo['i'] = val
    return val


def ho():
    if 'ho' in memo:
        return memo['ho']
    val = ~ hn()
    memo['ho'] = val
    return val


def hh():
    if 'hh' in memo:
        return memo['hh']
    val = he() >> 5
    memo['hh'] = val
    return val


print str(a())