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

viz.disable(viz.LIGHTING)