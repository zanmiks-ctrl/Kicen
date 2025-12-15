import viz
import vizcam

viz.go()


# Ielādē objektu AR MATERIĀLIEM
obj = viz.add('kicen.obj')

# Samazina objektu (ja par lielu)
obj.setScale([0.1, 0.1, 0.1])

# Pagriež par 90 grādiem
obj.setEuler([0, 90, 0])

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
kruze = viz.add('kruze.obj', parent=obj)
kruze.setPosition([35, 0, -32])
kruze.setScale([0.1, 0.1, 0.1])
kruze.setEuler([0, 0, -100])

cukurs = viz.add('cukurs.obj', parent=obj)
cukurs.setPosition([46, 75, -41])
cukurs.setScale([0.2, 0.2, 0.2])
cukurs.setEuler([0, 0, -100])

kafija = viz.add('kafija.obj', parent=obj)
kafija.setPosition([33, 83, -41])
kafija.setScale([0.4, 0.4, 0.4])
kafija.setEuler([0, 0, -100])

piens = viz.add('piens.obj', parent=obj)
piens.setPosition([-80, 35, -41])
piens.setScale([0.2, 0.2, 0.2])
piens.setEuler([0, 0, 70])