import viz
import vizcam

viz.go()

viz.MainView.getHeadLight().disable()

viz.disable(viz.LIGHTING)


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

taskText = viz.addText(
    'PAŅEM KRŪZI',
    parent=viz.SCREEN
)
taskText.setPosition(0.5, 0.9)
taskText.alignment(viz.ALIGN_CENTER)
taskText.fontSize(34)
taskText.color(viz.BLACK)

def setTask(text):
    taskText.message(text)
# =====================
# PICK-UP SISTĒMA
# =====================

holdingCup = False
holdingCoffee = False
cupPlaced = False    
kruze_s = None

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
    global holdingCup, holdingCoffee, kruze_s, cupPlaced

    if button != viz.MOUSEBUTTON_LEFT:
        return

    picked = viz.pick()

    # ==================================================
    # 1) PACELT KAFIJU (TIKAI JA KRŪZE IR NOVIETOTA)
    # ==================================================
    if picked == kafija and not holdingCoffee:
        if not cupPlaced:
            setTask("VISPIRMS NOLIEC KRŪZI PIE SMALCINĀTĀJA")
            print("VISPIRMS NOVIETO KRŪZI PIE SMALCINĀTĀJA")
            return

        kafija.setParent(viz.WORLD)
        kafija.visible(False)

        holdingCoffee = True
        setTask("IEBER KAFIJU SMALCINĀTĀJĀ")
        print("KAFIJA PAŅEMTA ROKĀ")
        return


    # ==================================================
    # 2) JA TURAM KAFIJU → KLIKŠĶIS UZ SMALCINĀTĀJA
    # ==================================================
    if holdingCoffee and picked == smalcinatajs:
        print("KAFIJA IEBĒRTA SMALCINĀTĀJĀ")
        holdingCoffee = False

        kruze.visible(False)

        kruze_s = viz.add('kruze_s.glb', parent=smalcinatajs)
        kruze_s.disable(viz.LIGHTING)
        kruze_s.setScale(CUP_ON_GRINDER_SCALE)
        kruze_s.setPosition([0.4, 0, 0.8])
        kruze_s.setEuler([0, 0, 0])

        setTask("KRŪZI NOLIEC ATPAKAĻ UZ GALDA")
        return


    # ==================================================
    # 3) JA TURAM KRŪZI → NOLIEK PIE SMALCINĀTĀJA
    # ==================================================
    if holdingCup:
        kruze.setParent(smalcinatajs)
        kruze.setPosition([2, 0, 0.8])
        kruze.setEuler([0, 0, 0])
        kruze.setScale(CUP_ON_GRINDER_SCALE)
        kruze.visible(True)

        holdingCup = False
        cupPlaced = True   
        
        setTask("PAŅEM KAFIJU")
        print("KRŪZE NOVIETOTA PIE SMALCINĀTĀJA")
        return


    # ==================================================
    # 4) PACELT KRŪZI
    # ==================================================
    if picked == kruze and not holdingCup:
        kruze.setParent(viz.WORLD)
        kruze.setScale(CUP_SCALE)
        kruze.visible(False)

        holdingCup = True
        cupPlaced = False 
        
        setTask("NOLIEC KRŪZI PIE SMALCINĀTĀJA")
        print("KRŪZE PAŅEMTA (NEREDZAMA)")
        return


viz.callback(viz.MOUSEDOWN_EVENT, onMouseDown)