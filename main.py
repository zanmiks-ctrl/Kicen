import viz
import vizcam

viz.go()

viz.MainView.getHeadLight().disable()

obj = viz.add('kicen.glb')
obj.setScale([0.1, 0.1, 0.1])
obj.setPosition([0, 0, 5])

vizcam.WalkNavigate()

viz.MainView.setPosition([0, 6, 0])

viz.mouse.setVisible(True)
viz.mouse.setTrap(True)

kruze = viz.add('kruze.glb', parent=obj)
kruze.setPosition([34.5, 33, -1.8])
kruze.setScale([0.1, 0.1, 0.1])
kruze.setEuler([90, 0, 0])

cukurs = viz.add('cukurs.glb', parent=obj)
cukurs.setPosition([46, 42, 93])
cukurs.setScale([0.2, 0.2, 0.2])


kafija = viz.add('kafija.glb', parent=obj)
kafija.setPosition([23.5, 42, 93.5])
kafija.setScale([0.4, 0.4, 0.4])


piens = viz.add('piens.glb', parent=obj)
piens.setPosition([-80, 42, 25])
piens.setScale([0.2, 0.2, 0.2])
piens.setEuler([110, 0, 0])

tejkanna= viz.add('tejkanna.glb', parent=obj)
tejkanna.setPosition([0, 42, 85])
tejkanna.setScale([0.2, 0.2, 0.2])
tejkanna.setEuler([-60, 0, 0])

smalcinatajs= viz.add('smalcinatajs.glb', parent=obj)
smalcinatajs.setPosition([-80, 42, 70])
smalcinatajs.setScale([0.3, 0.3, 0.3])
smalcinatajs.setEuler([-60, 0, 0])

viz.disable(viz.LIGHTING)

# =====================
# PICK-UP SISTĒMA
# =====================

holdingCup = False
holdingCoffee = False
holdingCupS = False
holdingSugar = False
holdingKettle = False
holdingMilk = False

cupPlaced = False

kruze_s = None
kruze_sc = None
kruze_u = None
kruze_p = None

# ---------------------
# SĀKOTNĒJĀS POZĪCIJAS
# ---------------------

CUP_TABLE_POS = kruze.getPosition()
CUP_TABLE_EULER = kruze.getEuler()

KETTLE_POS = tejkanna.getPosition()
KETTLE_EULER = tejkanna.getEuler()

MILK_POS = piens.getPosition()
MILK_EULER = piens.getEuler()

# ---------------------
# SCALE
# ---------------------

CUP_SCALE = [0.1, 0.1, 0.1]
GRINDER_SCALE = [0.3, 0.3, 0.3]

CUP_ON_GRINDER_SCALE = [
    CUP_SCALE[0] / GRINDER_SCALE[0],
    CUP_SCALE[1] / GRINDER_SCALE[1],
    CUP_SCALE[2] / GRINDER_SCALE[2],
]


def updateHeldCup():
    pass


vizact.onupdate(0, updateHeldCup)


def onMouseDown(button):
    global holdingCup, holdingCoffee, holdingCupS
    global holdingSugar, holdingKettle, holdingMilk
    global kruze_s, kruze_sc, kruze_u, kruze_p
    global cupPlaced, coffeeCupOnTable

    if button != viz.MOUSEBUTTON_LEFT:
        return

    picked = viz.pick()

    # ==================================================
    # 1) PAŅEM PARASTO KRŪZI
    # ==================================================
    if picked == kruze and not any([holdingCup, holdingCoffee, holdingCupS,
                                   holdingSugar, holdingKettle, holdingMilk]):
        kruze.setParent(viz.WORLD)
        kruze.setScale(CUP_SCALE)
        kruze.visible(False)

        holdingCup = True
        cupPlaced = False
        coffeeCupOnTable = False
        print("KRŪZE PAŅEMTA")
        return

    # ==================================================
    # 2) NOLIKT KRŪZI PIE SMALCINĀTĀJA
    # ==================================================
    if holdingCup and picked == smalcinatajs:
        kruze.setParent(smalcinatajs)
        kruze.setPosition([2, 0, 0.8])
        kruze.setEuler([0, 0, 0])
        kruze.setScale(CUP_ON_GRINDER_SCALE)
        kruze.visible(True)

        holdingCup = False
        cupPlaced = True
        print("KRŪZE NOVIETOTA PIE SMALCINĀTĀJA")
        return

    # ==================================================
    # 3) PAŅEM KAFIJU (TIKAI JA KRŪZE IR PIE SMALCINĀTĀJA)
    # ==================================================
    if picked == kafija:
        if holdingCup or not cupPlaced:
            print("Vispirms noliec krūzi pie smalcinātāja!")
            return
        if any([holdingCoffee, holdingSugar, holdingKettle, holdingMilk]):
            return

        kafija.visible(False)
        holdingCoffee = True
        print("KAFIJA PAŅEMTA")
        return

    # ==================================================
    # 4) IEBĒRT KAFIJU SMALCINĀTĀJĀ
    # ==================================================
    if holdingCoffee and picked == smalcinatajs:
        holdingCoffee = False
        kruze.visible(False)

        kruze_s = viz.add('kruze_s.glb', parent=smalcinatajs)
        kruze_s.disable(viz.LIGHTING)
        kruze_s.setScale(CUP_ON_GRINDER_SCALE)
        kruze_s.setPosition([2, 0, 0.8])
        kruze_s.setEuler([0, 0, 0])

        print("KRŪZE → KAFIJAS KRŪZE")
        return

    # ==================================================
    # 5) PAŅEM KAFIJAS KRŪZI
    # ==================================================
    if kruze_s and picked == kruze_s and not any([holdingCupS,
                                                 holdingSugar, holdingKettle, holdingMilk]):
        kruze_s.setParent(viz.WORLD)
        kruze_s.setScale(CUP_SCALE)
        kruze_s.visible(False)

        holdingCupS = True
        coffeeCupOnTable = False
        print("KAFIJAS KRŪZE PAŅEMTA")
        return

    # ==================================================
    # 6) NOLIKT KAFIJAS KRŪZI UZ GALDA
    # ==================================================
    if holdingCupS and picked == obj:
        kruze_s.setParent(obj)
        kruze_s.setScale(CUP_SCALE)
        kruze_s.setPosition(CUP_TABLE_POS)
        kruze_s.setEuler(CUP_TABLE_EULER)
        kruze_s.visible(True)

        holdingCupS = False
        coffeeCupOnTable = True
        print("KAFIJAS KRŪZE NOVIETOTA UZ GALDA")
        return

    # ==================================================
    # 7) PAŅEM CUKURU (TIKAI JA KRŪZE IR UZ GALDA)
    # ==================================================
    if picked == cukurs:
        if not coffeeCupOnTable:
            print("Vispirms noliec kafijas krūzi uz galda!")
            return
        if any([holdingSugar, holdingKettle, holdingMilk]):
            return

        cukurs.visible(False)
        holdingSugar = True
        print("CUKURS PAŅEMTS")
        return

    # ==================================================
    # 8) IEBĒRT CUKURU KRŪZĒ
    # ==================================================
    if holdingSugar and picked == kruze_s:
        holdingSugar = False
        kruze_s.visible(False)

        kruze_sc = viz.add('kruze_sc.glb', parent=obj)
        kruze_sc.disable(viz.LIGHTING)
        kruze_sc.setScale(CUP_SCALE)
        kruze_sc.setPosition(CUP_TABLE_POS)
        kruze_sc.setEuler(CUP_TABLE_EULER)

        print("KRŪZE → KAFIJA + CUKURS")
        return

    # ==================================================
    # 9) PAŅEM TEJKANNU
    # ==================================================
    if picked == tejkanna and kruze_sc and not any([holdingKettle, holdingMilk]):
        tejkanna.setParent(viz.WORLD)
        tejkanna.visible(False)

        holdingKettle = True
        print("TEJKANNA PAŅEMTA")
        return

    # ==================================================
    # 10) IELIET ŪDENI KRŪZĒ
    # ==================================================
    if holdingKettle and picked == kruze_sc:
        holdingKettle = False

        tejkanna.setParent(obj)
        tejkanna.setPosition(KETTLE_POS)
        tejkanna.setEuler(KETTLE_EULER)
        tejkanna.visible(True)

        kruze_sc.visible(False)

        kruze_u = viz.add('kruze_u.glb', parent=obj)
        kruze_u.disable(viz.LIGHTING)
        kruze_u.setScale(CUP_SCALE)
        kruze_u.setPosition(CUP_TABLE_POS)
        kruze_u.setEuler(CUP_TABLE_EULER)

        print("KRŪZE → KAFIJA AR ŪDENI")
        return

    # ==================================================
    # 11) PAŅEM PIENU
    # ==================================================
    if picked == piens and kruze_u and not holdingMilk:
        piens.setParent(viz.WORLD)
        piens.visible(False)

        holdingMilk = True
        print("PIENS PAŅEMTS")
        return

    # ==================================================
    # 12) IELIET PIENU KRŪZĒ
    # ==================================================
    if holdingMilk and picked == kruze_u:
        holdingMilk = False

        piens.setParent(obj)
        piens.setPosition(MILK_POS)
        piens.setEuler(MILK_EULER)
        piens.visible(True)

        kruze_u.visible(False)

        kruze_p = viz.add('kruze_p.glb', parent=obj)
        kruze_p.disable(viz.LIGHTING)
        kruze_p.setScale(CUP_SCALE)
        kruze_p.setPosition(CUP_TABLE_POS)
        kruze_p.setEuler(CUP_TABLE_EULER)

        print("☕ KAFIJA AR PIENU GATAVA!")
        return




viz.callback(viz.MOUSEDOWN_EVENT, onMouseDown)




















