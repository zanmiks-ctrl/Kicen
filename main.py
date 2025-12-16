import viz
import vizcam

viz.go()

viz.MainView.getHeadLight().disable()

# Ambient light (brings back color)
viz.disable(viz.LIGHTING)

# Ielādē objektu AR MATERIĀLIEM
obj = viz.add('kicen3.glb')

# Samazina objektu (ja par lielu)
obj.setScale([0.1, 0.1, 0.1])

# Novieto objektu priekšā
obj.setPosition([0, 0, 5])

# WASD + pele
vizcam.WalkNavigate()

# Kameras augstums
viz.MainView.setPosition([0, 6, 0])

# Pele skatam apkārt
viz.mouse.setVisible(False)
viz.mouse.setTrap(True)

# Krūze iekš objekta
kruze = viz.add('kruze.glb', parent=obj)
kruze.setPosition([35, 0, -32])
kruze.setScale([0.1, 0.1, 0.1])
kruze.setEuler([0, 0, -100])

cukurs = viz.add('cukurs.glb', parent=obj)
cukurs.setPosition([47.5, 75, -41.5])
cukurs.setScale([0.2, 0.2, 0.2])
cukurs.setEuler([0, 0, -100])

kafija = viz.add('kafija.glb', parent=obj)
kafija.setPosition([23.5, 93.5, -41.8])
kafija.setScale([0.4, 0.4, 0.4])


piens = viz.add('piens.glb', parent=obj)
piens.setPosition([-80, 35, -41])
piens.setScale([0.2, 0.2, 0.2])
piens.setEuler([0, 0, 70])

viz.disable(viz.LIGHTING)