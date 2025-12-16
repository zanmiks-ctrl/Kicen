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

viz.mouse.setVisible(False)
viz.mouse.setTrap(True)

kruze = viz.add('kruze.glb', parent=obj)
kruze.setPosition([35, 0, -32])
kruze.setScale([0.1, 0.1, 0.1])

cukurs = viz.add('cukurs.glb', parent=obj)
cukurs.setPosition([47.5, 75, -41.5])
cukurs.setScale([0.2, 0.2, 0.2])


kafija = viz.add('kafija.glb', parent=obj)
kafija.setPosition([23.5, 93.5, -41.8])
kafija.setScale([0.4, 0.4, 0.4])


piens = viz.add('piens.glb', parent=obj)
piens.setPosition([-80, 35, -41])
piens.setScale([0.2, 0.2, 0.2])
piens.setEuler([0, 0, 70])

viz.disable(viz.LIGHTING)