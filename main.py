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
